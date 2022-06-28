#!/bin/bash
## function: start server

## init dirs
dir_data="data"
dir_upload=${dir_data}/"upload_data"
mkdir -p ${dir_upload}/OK
mkdir -p ${dir_upload}/NEG
mkdir -p ${dir_data}/upload_data
mkdir -p ${dir_data}/predict_data 
mkdir -p ${dir_data}/database 
mkdir -p scripts/static/upload_image

mkdir -p database
mkdir -p logs

python3 scripts/server.py
