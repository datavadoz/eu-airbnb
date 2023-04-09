terraform {
  required_version = ">= 1.0"
  backend "local" {}
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = var.PROJECT
  region = var.REGION
}

resource "google_storage_bucket" "data-lake" {
  name = var.GCS_NAME
  project = var.PROJECT
  location = var.REGION
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
  force_destroy = true
}

resource "google_bigquery_dataset" "dwh-staging-1" {
  project = var.PROJECT
  dataset_id = var.BQ_DATASET_STAGING_1
}

resource "google_bigquery_dataset" "dwh-staging-2" {
  project = var.PROJECT
  dataset_id = var.BQ_DATASET_STAGING_2
}

resource "google_bigquery_dataset" "dwh-prod" {
  project = var.PROJECT
  dataset_id = var.BQ_DATASET_PROD
}
