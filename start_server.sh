#!/bin/bash
## function: start server

## init dirs
dir_upload="upload_data"
mkdir -p ${dir_upload}/OK
mkdir -p ${dir_upload}/NEG

mkdir -p database
mkdir -p logs

python3 scripts/server.py