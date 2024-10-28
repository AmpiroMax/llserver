#!/bin/bash

conda activate llama2
cd /home/mpatratskiy/work/meta_world/llserver/llserver/server
uvicorn server:app --reload