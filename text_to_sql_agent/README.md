# Text-to-SQL Agent with Gemini + BigQuery

This project demonstrates how to build a natural language to SQL agent using Gemini (via LangChain/LangGraph) on BigQuery.

## Structure
- `config/settings.py` → GCP project, dataset, model config
- `src/schema_loader.py` → Load schema from BigQuery
- `src/bq_connection.py` → BigQuery SQL connection
- `src/agent.py` → Agent definition
- `src/run_query.py` → Entrypoint to run queries

## Run
```bash
pip install -r requirements.txt
python -m src.run_query
```
