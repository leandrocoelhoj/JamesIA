# import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
from datetime import datetime, timedelta
import os
import tempfile
from pathlib import Path


# current_dir = os.path.dirname(os.path.abspath('__file__'))
# base_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
# json_path = os.path.join(base_dir, "secrets", "grand-bridge-465614-h2-af35a1b3a984.json")

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
json_path = PROJECT_ROOT / "secrets/grand-bridge-465614-h2-af35a1b3a984.json"


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
def build_drive_client():
    creds = service_account.Credentials.from_service_account_file(str(json_path), scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def find_folders(drive):
    results = drive.files().list(
        pageSize=10,
        fields="files(id, name, mimeType)"
    ).execute()
    return results["files"]

def get_target_filename(files, target_date):
    """
    files: lista retornada pelo Drive
    target_date: datetime.date ou string 'YYYY-MM-DD'
    """
    if isinstance(target_date, str):
        target_date = datetime.strptime(target_date, "%Y-%m-%d").date()

    # Converte para dd-mm-YYYY
    date_str = target_date.strftime("%d-%m-%Y")
    expected_name = f"custos{date_str}.csv"

    for f in files:
        if f["mimeType"] == "text/csv" and f["name"] == expected_name:
            return f  # retorna o dict com id, name...
    return None

def download_drive_file_to_temp(drive, file_id: str, suffix=".csv") -> str:
    """Baixa um arquivo do Drive para um arquivo temporário e retorna o caminho."""
    req = drive.files().get_media(fileId=file_id)
    fd, tmp_path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    with open(tmp_path, "wb") as f:
        downloader = MediaIoBaseDownload(f, req)
        done = False
        while not done:
            _, done = downloader.next_chunk()
    return tmp_path