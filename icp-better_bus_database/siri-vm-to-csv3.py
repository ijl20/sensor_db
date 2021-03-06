#!/usr/bin/env python3

'''
Given one or more directories containing SIRI-VM data in Json, spit out
journey records in a format for loading into the database.
'''

import json
import sys
import os
import csv
import datetime
import dateutil.parser

'''
   "request_data": [
        {
            "Bearing": "300",
            "DataFrameRef": "1",
            "DatedVehicleJourneyRef": "119",
            "Delay": "-PT33S",
            "DestinationName": "Emmanuel St Stop E1",
            "DestinationRef": "0500CCITY487",
            "DirectionRef": "OUTBOUND",
            "InPanic": "0",
            "Latitude": "52.2051239",
            "LineRef": "7",
            "Longitude": "0.1242290",
            "Monitored": "true",
            "OperatorRef": "SCCM",
            "OriginAimedDepartureTime": "2017-10-25T23:14:00+01:00",
            "OriginName": "Park Road",
            "OriginRef": "0500SSAWS023",
            "PublishedLineName": "7",
            "RecordedAtTime": "2017-10-25T23:59:48+01:00",
            "ValidUntilTime": "2017-10-25T23:59:48+01:00",
            "VehicleMonitoringRef": "SCCM-19597",
            "VehicleRef": "SCCM-19597",
            "acp_id": "SCCM-19597",
            "acp_lat": 52.2051239,
            "acp_lng": 0.124229,
            "acp_ts": 1508972388
        },
'''


csvwriter = csv.writer(sys.stdout)

for dir in sys.argv[1:]:
    for root, dirs, files in os.walk(dir):
        for filename in files:
            if not filename.endswith(".json"):
                continue
            pathname = os.path.join(root, filename)
            with open(pathname) as data_file:
                data = json.load(data_file)

            file_ts = datetime.datetime.utcfromtimestamp(data["ts"]).isoformat() + '+00:00'

            for record in data["request_data"]:
                # Extract date from the UTC version of RecordedAtTime
                recorded_date = (dateutil.parser.parse(record["RecordedAtTime"])
                    .astimezone(datetime.timezone.utc).date())
                csvwriter.writerow ((
                    file_ts,
                    "SRID=4326;POINT({} {})".format(
                        record["acp_lng"],
                        record["acp_lat"]),
                    record["RecordedAtTime"],
                    recorded_date,
                    record["OriginAimedDepartureTime"],
                    json.dumps(record),
                ))