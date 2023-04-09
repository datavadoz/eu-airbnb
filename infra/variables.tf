variable "PROJECT" {
  description = "Project ID"
  default = "dtc-airbnb"
  type = string
}

variable "GCS_NAME" {
  description = "Google Cloud Storage name"
  default = "dtc-airbnb"
  type = string
}

variable "REGION" {
  description = "Region for GCP resources"
  default = "us-west1"
  type = string
}

variable "BQ_DATASET_STAGING_1" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  default = "staging"
  type = string
}

variable "BQ_DATASET_STAGING_2" {
  description = "BigQuery Dataset that BQ_DATASET_STAGING_1 will be written to"
  default = "airbnb_staging"
  type = string
}

variable "BQ_DATASET_PROD" {
  description = "BigQuery Dataset for final production"
  default = "airbnb_prod"
  type = string
}
