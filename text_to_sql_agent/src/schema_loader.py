from google.cloud import bigquery
import json
from config.settings import PROJECT_ID, DATASET_ID

def get_dataset_schema():
    client = bigquery.Client(project=PROJECT_ID)
    dataset_ref = client.dataset(DATASET_ID)
    tables = client.list_tables(dataset_ref)

    schema_info = {}
    for table in tables:
        table_ref = dataset_ref.table(table.table_id)
        table_obj = client.get_table(table_ref)
        schema_info[table.table_id] = [
            {"name": f.name, "type": f.field_type} for f in table_obj.schema
        ]

    # (Optional) Save cache
    with open("data/schema_cache.json", "w") as f:
        json.dump(schema_info, f, indent=2)

    return schema_info
