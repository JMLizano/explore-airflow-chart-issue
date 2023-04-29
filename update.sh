#! /bin/bash

export RELEASE_NAME=sync-error

helm upgrade $RELEASE_NAME ./airflow  -f values-ok.yaml