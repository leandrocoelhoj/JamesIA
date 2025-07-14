from google.cloud import storage
import json
from datetime import datetime
from pathlib import Path


def save_json_to_gcs(bucket_name: str, module: str, endpoint: str, data: dict):
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"{module}/{endpoint}/{date_str}.json"

    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

    key_path = PROJECT_ROOT / "secrets/grand-bridge-465614-h2-af35a1b3a984.json"
    client = storage.Client.from_service_account_json(str(key_path))
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)

    blob.upload_from_string(json.dumps(data, ensure_ascii=False, indent=2), content_type='application/json')
    print(f"✔ Dados salvos em: gs://{bucket_name}/{filename}/{endpoint}/{date_str}.json")