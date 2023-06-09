# Airbnb Prices in European Cities

## Overview

This project uses [Kaggle dataset](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities) to find story to tell about Airbnb prices in Europe cities.

## Prerequisites

- Terraform
- Docker and docker compose
- Google Cloud Platform (GCP)

## Architecture

Technologies used in this project:

- Containerization: Docker
- Workflow orchestrator: Mage AI
- Tranformation framework: DBT
- Data lake: Google Cloud Storage
- Data warehouse: Google BigQuery
- Infrastructure as Code: Terraform
- BI tool: Google Looker

![Architecture](./images/architecture.png)

1. Terraform launches GCP resources (GCS, BigQuery).
2. Docker launches Mage image where the pipeline runs in.
3. Extract `archive.zip`.
4. Clean and load raw data into GCS.
5. Load cleansed data from GCS to BigQuery (staging).
6. Transform staging data to production ready data.
7. Visualize production data via dashboard.

## Instruction

0. Create GCP project named `dtc-airbnb`.
1. Create service account on GCP inside `dtc-airbnb` project with 4 following roles: **Actions Viewer**, **BigQuery Admin**, **Storage Admin**, **Storage Object Admin**. Then, download this GCP service account credential JSON file to `./cred` (on the same directory level with this README) and set the absolute path to `GOOGLE_APPLICATION_CREDENTIALS` environment variable: `export GOOGLE_APPLICATION_CREDENTIALS=<gcp_credential_json_path>`.
2. Bring GCP infrastructure up:
    ```
    cd infra
    terraform init
    terraform apply
    ``` 
3. Replace `<your_gcp_credential_json>` with your GCP credential JSON file name (e.g: `dtc-airbnb-33c84c172b76.json`) in the environment variable `GOOGLE_APPLICATION_CREDENTIALS` value inside `docker-compose.yml`.
4. Build Docker image: `docker compose build`
5. Bring Mage docker container up: `docker compose up -d`
6. Browse Mage UI `http://localhost:6789/pipelines/etl_end_to_end/triggers` and hit `Run pipeline now` button to run `etl_end_to_end` pipeline.
    ![End to end pipeline](./images/etl_end_to_end.jpg)
## Dashboard
![Dashboard](./images/dashboard.png)

Interactive dashboard is [here](https://lookerstudio.google.com/reporting/99e0048a-190e-475e-8009-66e833552386).

