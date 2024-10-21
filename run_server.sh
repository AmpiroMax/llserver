#!/bin/bash

conda activate llama2
cd /home/mpatratskiy/work/meta_world/src/llserver/server
uvicorn server:app --reload