# Text-to-SQL Agent with BigQuery

## Project Overview

This project provides an AI-powered agent that converts natural language queries into SQL for BigQuery datasets. It leverages the Google Gemini API via `langchain_google_genai` and supports multi-table queries within a dataset. The agent can also format results into email-ready messages.

## Features

* Converts plain English queries to SQL.
* Supports BigQuery datasets and tables.
* Handles queries involving joins across multiple tables.
* Can wrap generated SQL in an email-friendly format.
* Uses Google Gemini API with API key authentication.

## Requirements

* Python 3.12+
* Google Cloud project with BigQuery and Storage enabled.
* BigQuery dataset and tables with proper access.
* `langchain`, `langchain_google_genai`, and `google-cloud-storage` Python packages.

## Setup

1. Clone the repository.
2. Install required packages using `pip install -r requirements.txt`.
3. Configure your Google Cloud project ID, dataset ID, and Gemini API key in `config/settings.py`.
4. Ensure BigQuery tables exist and have the necessary permissions.
5. Ensure the Cloud Storage bucket exists for any CSV uploads.

## Usage

* Run the agent with the provided scripts to generate SQL queries from natural language.
* Optionally, wrap the query output in email format for notifications or reporting.
* Supports multi-table queries within the same dataset, including joins and filters.

## Notes

* For large data handling, CSV generation and upload to GCS is recommended.
* Ensure API keys have the proper scopes for Generative Language and BigQuery access.
* Follow best practices for API key storage and security.

## References

* [LangChain Documentation](https://www.langchain.com/docs/)
* [Google Cloud BigQuery](https://cloud.google.com/bigquery/docs)
* [Google Gemini API](https://developers.generativeai.google/)



## Problems Faced in the Project

1. **BigQuery Storage Client Warning**

   * Warning: `Cannot create BigQuery Storage client, the dependency google-cloud-bigquery-storage is not installed.`
   * Cause: The optional BigQuery Storage library was missing.
   * Impact: Slower reads and potential feature limitations.

2. **Access Token Scope / Permission Issues**

   * Error: `ACCESS_TOKEN_SCOPE_INSUFFICIENT` and `PermissionDenied: 403`
   * Cause: The Google Gemini API and BigQuery calls required specific scopes or permissions not present in the ADC credentials.
   * Impact: LLM queries to generate SQL failed repeatedly.

3. **Service API Not Enabled**

   * Error: `Service Usage API has not been used in project [...] or it is disabled`
   * Cause: Required APIs like `serviceusage.googleapis.com` were not enabled.
   * Impact: Commands like `gcloud auth application-default login` failed.

4. **API Key / Gemini Model Issues**

   * Errors: `models/gemini-1.5-pro is not found` and `Method doesn't allow unregistered callers`
   * Cause: Either the model was unavailable for the API version or API key/authentication was not properly configured.
   * Impact: Could not call the Generative Language API from code.

5. **Storage / Local Disk Issues**

   * Error: `OSError: [Errno 28] No space left on device`
   * Cause: Generating large CSV files (millions of rows) exceeded local disk capacity in Cloud Shell.
   * Impact: Could not generate 1 billion rows locally.

6. **Incorrect File Handling**

   * Error: `TypeError: write() argument must be str, not bytes`
   * Cause: CSV writing attempted in binary mode with a `csv.writer`.
   * Impact: CSV generation failed until mode and data types were corrected.

7. **BigQuery Access / Permission Errors**

   * Error: `Caller does not have required permission to use project [...] roles/serviceusage.serviceUsageConsumer`
   * Cause: Insufficient IAM roles or permissions on the project/dataset.
   * Impact: SQLDatabaseChain could not connect to BigQuery to fetch table metadata.

8. **Multi-Table SQL Queries**

   * Challenge: Combining `product_details` and `products` tables for a filtered query.
   * Cause: Needed knowledge of SQL joins and correct dataset scoping.
   * Impact: Initial queries did not return the expected results.

9. **LangChain Deprecation Warnings**

   * Warning: `Chain.run` method deprecated.
   * Cause: Code using old API methods.
   * Impact: Needed to switch to `invoke` or updated methods to avoid future breakage.

10. **Email Formatting Requirement**

    * Challenge: Need to send query results in a structured email format.
    * Cause: Not initially included in SQL agent.
    * Impact: Required additional logic to wrap SQL results in an email-friendly template.



I can also create a **slightly more detailed README** including **example queries, table structure descriptions, and workflow diagrams** if you want. Do you want me to do that?
