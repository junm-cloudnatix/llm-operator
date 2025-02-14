#!/usr/bin/env bash

set -euo pipefail

helm repo add llm-operator http://llm-operator-charts.s3-website-us-west-2.amazonaws.com/
helm repo update

helm upgrade \
  --install \
  -n llm-operator \
  llm-operator \
  llm-operator/llm-operator \
  -f llm-operator-values.yaml
