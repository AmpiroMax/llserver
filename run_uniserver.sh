#!/bin/bash
# Set model name
# export MODEL_NAME="llera_api"
# export HF_HOME="/run/user/1004/mpatrat_data/hf"

conda activate llama2
cd /home/mpatratskiy/work/meta_world/llserver/llserver/server
uvicorn uniserver:app --reload --host 0.0.0.0 --port 8000