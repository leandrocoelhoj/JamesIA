import csv
import re
import os
import requests

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'csv_days', 'custos01-08-2025.csv')


def parse_tempo(tempo_str):
    # Ex: '68.645 min 24 seg'
    match = re.match(r"([\d\.]+)\s*min\s*(\d+)\s*seg", tempo_str)
    if match:
        min_str, seg_str = match.groups()
        minutos = int(min_str.replace('.', ''))
        segundos = int(seg_str)
        return minutos * 60 + segundos
    return 0

def parse_valor(valor_str):
    valor = valor_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
    return float(valor)

def parse_csv_custos(filepath, data_arquivo):
    """
    Lê um CSV de custos, retorna lista de dicts prontos para ingestão.
    data_arquivo: data a ser registrada nos custos (usada no campo data)
    empresa_dominio: domínio da empresa para registro de FK
    """
    result = []
    with open(filepath, newline='', encoding='latin1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        reader.fieldnames = [f.strip() for f in reader.fieldnames]
        for row in reader:
            obj = {
                "techprefix": row['Linha / Techprefix'].replace('#', ''),
                "total_chamadas": int(row['Total'].replace('.', '')),
                "tempo_total_segundos": parse_tempo(row['Tempo Total']),
                "cliente": row['Cliente'],
                "media_chamada": row['Média'],
                "media_chamada_segundos": int(row['Média Seg']),
                "valor_total": parse_valor(row['Valor Total']),
                "data": data_arquivo,
                "empresa": "",
            }
            result.append(obj)
    return result

if __name__ == "__main__":
    dados = parse_csv_custos(csv_path, data_arquivo='2025-08-01')

    # Envie TODOS os dados de uma vez como lista
    response = requests.post(
        'http://localhost:8000/api/ingest_custos/',
        json=dados  # Envia a lista completa
    )

    print("Status code:", response.status_code)
    print("Response:", response.json())