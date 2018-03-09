#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo Usage: ./import_sirivm.sh \<date string\>
    echo e.g. ./import_sirivm.sh 2017/11
    exit
fi

data_directory=/media/tfc/cloudamber/sirivm/data_bin_json/$1

date_start=$(date)

echo $data_directory $date_start: importing data to postgresql

./sirivm_to_db.py /media/tfc/cloudamber/sirivm/data_bin_json/$1

echo $data_directory Started $date_start, Finished $(date)
