#!/usr/bin/env python3

import sys
import os
import json
import psycopg2

FILE_SUFFIX = ".json"

print("hello world "+sys.argv[0])

db_connect = psycopg2.connect("dbname=test_sensor")

db_cursor = db_connect.cursor()

def process_file(filepath):
    sirivm_count = 0;
    #print(filepath)
    if (filepath.endswith(FILE_SUFFIX)):
        try:
            file_data = json.load(open(filepath));
            for sirivm in file_data["request_data"]:
                sirivm_count += 1
                sirivm_string = json.dumps(sirivm)
                #print(sirivm_string)
                db_cursor.execute("INSERT INTO sensor_data_1(info) values(%s)",[sirivm_string])

            #print("processing "+filepath+" "+str(sirivm_count)+" records")

        except ValueError:
            print("Bad json file "+filepath)

    if (sirivm_count > 0):
       db_connect.commit()

def process_files(dirname):
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        #print("DIRS")
        #for dir in dirnames:
        #    print(dir)
        #print("FILES")
        for file in filenames:
            process_file(os.path.join(dirpath,file))

process_files(sys.argv[1])

db_cursor.close()
db_connect.close()

