#!/bin/bash
# Set model name
# export MODEL_NAME="llera_api"
# export HF_HOME="/run/user/1004/mpatrat_data/hf"

conda activate llama2
cd llserver/server
uvicorn server:app --reload