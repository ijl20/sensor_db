# sensor_db: Evaluating the use of Postgresql for sensor data storage

## Overview

The sensor data generated in the Adaptive Cities Platform is generally expected to be both timestamped 
and geo-located, i.e. each data record has a format such as:
```
<timestamp> <latitude> <longitude> <altitude> <sensor identifier> <other stuff>
```

The sensor identifier is likely to be unique only within a given source of sensor data and we need to 
consider how we might handle that - possible approaches include a 'sensor type' property in the 
record or the use of a table per data source (so the table name equates to the 'sensor type' or 
source.

In general we expect to:
1. store the original sensor data as a JSONB column in the table, called 
`info`
2. *promote* some properties in the sensor date to columns in the table (such as timestamp) if that
provides faster access
3. add *indexes* to properties or columns to speed up access
4. consider the use of **PostGIS** to provide multi-dimensional indexes, or alternatively the 
Postgresql *cube* datatype with its index support

We will use a set of standard queries relevant to our use case, to assess performance.

## Standard sensor data queries

The 'big box' is (52.11, -0.1)..(52.3, .25)

The 'small box' is (0.08008, 52.205029)..(0.108576, 52.215548)

#### Big box, one day and "VehicleRef"

```
select info from sensor_data_1 where
cast(info->>'Latitude' as float) > 52.11 and cast(info->>'Latitude' as float) < 52.3 and
cast(info->>'Longitude' as float) > -0.1 and cast(info->>'Longitude' as float) < 0.25 and
to_timestamp(info->>'RecordedAtTime', 'YYYY-MM-DDTHH:MI:SS') >= '2017-12-11 00:00:00+00:00' and
to_timestamp(info->>'RecordedAtTime', 'YYYY-MM-DDTHH:MI:SS') < '2017-12-12 00:00:00+00:00' and
info->>'VehicleRef' = 'WP-106';
```

### Table: sensor_data_1

#### Table information

```
                                             Table "public.sensor_data_1"
 Column |  Type  |                         Modifiers                          | Storage  | Stats target | Description 
--------+--------+------------------------------------------------------------+----------+--------------+-------------
 id     | bigint | not null default nextval('sensor_data_1_id_seq'::regclass) | plain    |              | 
 info   | jsonb  | not null                                                   | extended |              | 

Indexes:
    "sensor_data_1_pkey" PRIMARY KEY, btree (id)
```


