#! /bin/bash

RELEASE_NAME=sync-error

helm pull apache-airflow/airflow --untar  --version 1.8.0
helm install $RELEASE_NAME ./airflow -f values.yaml
