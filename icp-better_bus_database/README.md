# Readme

```
tfcapi=# \i table_sizes.sql
Pager usage is off.
Timing is off.
                                    Table "public.siri_vm"
   Column   |           Type           |                      Modifiers                       
------------+--------------------------+------------------------------------------------------
 id         | bigint                   | not null default nextval('siri_vm_id_seq'::regclass)
 acp_id     | text                     | 
 location4d | geography(PointZM,4326)  | 
 acp_ts     | timestamp with time zone | 
 info       | jsonb                    | 
 file_ts    | timestamp with time zone | 
 line_ref   | text                     | 
Indexes:
    "siri_vm_pkey" PRIMARY KEY, btree (id)
    "siri_vm_acp_id" btree (acp_id)
    "siri_vm_info" gin (info)
    "siri_vm_location4d" gist (location4d)
    "siri_vm_location4d_geom" gist ((location4d::geometry))
    "siri_vm_ts" btree (acp_ts)

                                        Table "public.siri_vm2"
       Column        |           Type           |                       Modifiers                       
---------------------+--------------------------+-------------------------------------------------------
 id                  | bigint                   | not null default nextval('siri_vm2_id_seq'::regclass)
 file_ts             | timestamp with time zone | not null
 acp_id              | character(20)            | not null
 acp_ts              | timestamp with time zone | not null
 location4d          | geometry(PointZM,27700)  | 
 line_ref            | character(10)            | not null
 origin_ref          | character(20)            | not null
 origin_departure_ts | timestamp with time zone | not null
 info                | jsonb                    | not null
 temp_geom           | geometry(PointZM,4326)   | not null
Indexes:
    "siri_vm2_pkey" PRIMARY KEY, btree (id)
    "siri_vm2_acp_id" btree (acp_id)
    "siri_vm2_acp_ts" btree (acp_ts)
    "siri_vm2_line_ref" btree (line_ref)
    "siri_vm2_location4d" gist (location4d)
    "siri_vm2_origin_departure_ts" btree (origin_departure_ts)
    "siri_vm2_origin_ref" btree (origin_ref)

               Table "public.siri_vm_3"
    Column     |           Type           | Modifiers 
---------------+--------------------------+-----------
 file_ts       | timestamp with time zone | not null
 location      | geometry(Point,4326)     | not null
 recorded_ts   | timestamp with time zone | not null
 recorded_date | date                     | not null
 departure_ts  | timestamp with time zone | not null
 info          | jsonb                    | not null
Indexes:
    "siri_vm_3_departure_ts" btree (departure_ts)
    "siri_vm_3_info" gin (info)
    "siri_vm_3_location" gist (location)
    "siri_vm_3_recorded_date" btree (recorded_date)
    "siri_vm_3_recorded_ts" btree (recorded_ts)

             Table "public.siri_vm_4"
   Column   |          Type           | Modifiers 
------------+-------------------------+-----------
 acp_id     | character(20)           | not null
 acp_lng    | double precision        | not null
 acp_lat    | double precision        | not null
 acp_ts     | bigint                  | not null
 location2d | geography(Point,4326)   | not null
 location4d | geography(PointZM,4326) | not null
 info       | jsonb                   | not null
Indexes:
    "siri_vm_4_acp_id" btree (acp_id)
    "siri_vm_4_acp_lat" btree (acp_lat)
    "siri_vm_4_acp_lng" btree (acp_lng)
    "siri_vm_4_acp_ts" btree (acp_ts)
    "siri_vm_4_info" gin (info)
    "siri_vm_4_location2d" gist (location2d)
    "siri_vm_4_location2d_geom" gist ((location2d::geometry))
    "siri_vm_4_location4d" gist (location4d)
    "siri_vm_4_location4d_geom_nd" gist ((location4d::geometry) gist_geometry_ops_nd)

             Table "public.siri_vm_5"
   Column    |          Type           | Modifiers 
-------------+-------------------------+-----------
 acp_id      | character(20)           | not null
 acp_lng     | double precision        | not null
 acp_lat     | double precision        | not null
 acp_ts      | bigint                  | not null
 location2d  | geography(Point,4326)   | not null
 location4d  | geography(PointZM,4326) | not null
 info        | jsonb                   | not null
 acp_ts_date | date                    | 
Triggers:
    insert_siri_vm_5_trigger BEFORE INSERT ON siri_vm_5 FOR EACH ROW EXECUTE PROCEDURE siri_vm_5_insert_trigger()
Number of child tables: 38 (Use \d+ to list them.)

         Table "public.siri_vm_5_2017_41"
   Column    |          Type           | Modifiers 
-------------+-------------------------+-----------
 acp_id      | character(20)           | not null
 acp_lng     | double precision        | not null
 acp_lat     | double precision        | not null
 acp_ts      | bigint                  | not null
 location2d  | geography(Point,4326)   | not null
 location4d  | geography(PointZM,4326) | not null
 info        | jsonb                   | not null
 acp_ts_date | date                    | 
Indexes:
    "siri_vm_5_2017_41_acp_id" btree (acp_id)
    "siri_vm_5_2017_41_acp_lat" btree (acp_lat)
    "siri_vm_5_2017_41_acp_lng" btree (acp_lng)
    "siri_vm_5_2017_41_acp_ts" btree (acp_ts)
    "siri_vm_5_2017_41_info" gin (info)
    "siri_vm_5_2017_41_location2d" gist (location2d)
    "siri_vm_5_2017_41_location2d_geom" gist ((location2d::geometry))
    "siri_vm_5_2017_41_location4d" gist (location4d)
    "siri_vm_5_2017_41_location4d_geom_nd" gist ((location4d::geometry) gist_geometry_ops_nd)
Check constraints:
    "siri_vm_5_2017_41_acp_ts_check" CHECK (acp_ts >= 1507507200 AND acp_ts < 1508112000)
Inherits: siri_vm_5

                                             Table "public.journey"
      Column      |           Type           |                            Modifiers                             
------------------+--------------------------+------------------------------------------------------------------
 acp_journey_id   | bigint                   | not null default nextval('journey_acp_journey_id_seq'::regclass)
 vehicle_ref      | text                     | not null
 destination_ref  | text                     | not null
 destination_name | text                     | not null
 direction_ref    | text                     | not null
 line_ref         | text                     | not null
 operator_ref     | text                     | not null
 departure_time   | timestamp with time zone | not null
 origin_ref       | text                     | not null
 origin_name      | text                     | not null
 pos              | pos_report[]             | 
Indexes:
    "journey_pkey" PRIMARY KEY, btree (acp_journey_id)
    "journey_departure_time" btree (departure_time)
    "journey_line_ref" btree (line_ref)
    "journey_lng_lat_ts" gist (enclosing_cube(pos)) WITH (buffering='on')
    "journry_origin_ref" btree (origin_ref)

     tablename     |   records    
-------------------+--------------
 journey           |      773,015
 siri_vm           |   31,589,550
 siri_vm2          |   35,614,880
 siri_vm_3         |   37,214,904
 siri_vm_4         |   37,980,660
 siri_vm_5         |            0
 siri_vm_5_2017_41 |    2,787,489
 siri_vm_5_2017_42 |    4,825,347
 siri_vm_5_2017_43 |    4,722,842
 siri_vm_5_2017_44 |    4,770,544
 siri_vm_5_2017_45 |    4,724,156
 siri_vm_5_2017_46 |    4,746,724
 siri_vm_5_2017_47 |    4,415,179
 siri_vm_5_2017_48 |    4,740,100
 siri_vm_5_2017_49 |    3,904,456
 siri_vm_5_2017_50 |    4,727,818
 siri_vm_5_2017_51 |    4,657,747
 siri_vm_5_2017_52 |    2,923,343
 siri_vm_5_2018_01 |    6,496,855
 siri_vm_5_2018_02 |    4,809,566
 siri_vm_5_2018_03 |    4,625,346
 siri_vm_5_2018_04 |    4,828,573
 siri_vm_5_2018_05 |    4,716,907
 siri_vm_5_2018_06 |    4,705,099
 siri_vm_5_2018_07 |    4,670,226
 siri_vm_5_2018_08 |    4,889,387
 siri_vm_5_2018_09 |    3,393,043
 siri_vm_5_2018_10 |            0
 siri_vm_5_2018_11 |            0
 siri_vm_5_2018_12 |            0
 siri_vm_5_2018_13 |            0
 siri_vm_5_2018_14 |            0
 siri_vm_5_2018_15 |            0
 siri_vm_5_2018_16 |            0
 siri_vm_5_2018_17 |            0
 siri_vm_5_2018_18 |            0
 siri_vm_5_2018_19 |            0
 siri_vm_5_2018_20 |            0
 siri_vm_5_2018_21 |            0
 siri_vm_5_2018_22 |            0
 siri_vm_5_2018_23 |            0
 siri_vm_5_2018_24 |            0
 siri_vm_5_2018_25 |            0
 siri_vm_5_2018_26 |            0
(44 rows)

     tablename     |  main   | free_space_map | visability_map | initialisation |  total  
-------------------+---------+----------------+----------------+----------------+---------
 journey           | 459 MB  | 136 kB         | 0 bytes        | 0 bytes        | 459 MB
 siri_vm           | 30 GB   | 7632 kB        | 432 kB         | 0 bytes        | 30 GB
 siri_vm2          | 67 GB   | 17 MB          | 1080 kB        | 0 bytes        | 67 GB
 siri_vm_3         | 32 GB   | 0 bytes        | 0 bytes        | 0 bytes        | 32 GB
 siri_vm_4         | 32 GB   | 8368 kB        | 528 kB         | 0 bytes        | 32 GB
 siri_vm_5         | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2017_41 | 2423 MB | 632 kB         | 0 bytes        | 0 bytes        | 2424 MB
 siri_vm_5_2017_42 | 4194 MB | 1072 kB        | 0 bytes        | 0 bytes        | 4195 MB
 siri_vm_5_2017_43 | 4103 MB | 1056 kB        | 0 bytes        | 0 bytes        | 4104 MB
 siri_vm_5_2017_44 | 4143 MB | 1064 kB        | 0 bytes        | 0 bytes        | 4144 MB
 siri_vm_5_2017_45 | 4101 MB | 1056 kB        | 0 bytes        | 0 bytes        | 4102 MB
 siri_vm_5_2017_46 | 4121 MB | 1056 kB        | 0 bytes        | 0 bytes        | 4122 MB
 siri_vm_5_2017_47 | 3834 MB | 984 kB         | 0 bytes        | 0 bytes        | 3835 MB
 siri_vm_5_2017_48 | 4280 MB | 1096 kB        | 0 bytes        | 0 bytes        | 4281 MB
 siri_vm_5_2017_49 | 3391 MB | 872 kB         | 0 bytes        | 0 bytes        | 3392 MB
 siri_vm_5_2017_50 | 4108 MB | 1056 kB        | 0 bytes        | 0 bytes        | 4109 MB
 siri_vm_5_2017_51 | 4049 MB | 1040 kB        | 0 bytes        | 0 bytes        | 4050 MB
 siri_vm_5_2017_52 | 2746 MB | 712 kB         | 0 bytes        | 0 bytes        | 2746 MB
 siri_vm_5_2018_01 | 5643 MB | 1440 kB        | 0 bytes        | 0 bytes        | 5644 MB
 siri_vm_5_2018_02 | 4176 MB | 1072 kB        | 0 bytes        | 0 bytes        | 4177 MB
 siri_vm_5_2018_03 | 4018 MB | 1032 kB        | 0 bytes        | 0 bytes        | 4019 MB
 siri_vm_5_2018_04 | 4197 MB | 1080 kB        | 0 bytes        | 0 bytes        | 4198 MB
 siri_vm_5_2018_05 | 4098 MB | 1048 kB        | 0 bytes        | 0 bytes        | 4099 MB
 siri_vm_5_2018_06 | 4088 MB | 1048 kB        | 0 bytes        | 0 bytes        | 4089 MB
 siri_vm_5_2018_07 | 4056 MB | 1040 kB        | 0 bytes        | 0 bytes        | 4057 MB
 siri_vm_5_2018_08 | 4247 MB | 1088 kB        | 0 bytes        | 0 bytes        | 4248 MB
 siri_vm_5_2018_09 | 2946 MB | 760 kB         | 0 bytes        | 0 bytes        | 2946 MB
 siri_vm_5_2018_10 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_11 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_12 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_13 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_14 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_15 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_16 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_17 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_18 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_19 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_20 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_21 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_22 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_23 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_24 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_25 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
 siri_vm_5_2018_26 | 0 bytes | 0 bytes        | 0 bytes        | 0 bytes        | 0 bytes
(44 rows)

     tablename     |              indexname               |    size    
-------------------+--------------------------------------+------------
 journey           | journey_departure_time               | 17 MB
 journey           | journey_line_ref                     | 17 MB
 journey           | journey_lng_lat_ts                   | 106 MB
 journey           | journey_pkey                         | 17 MB
 journey           | journry_origin_ref                   | 23 MB
 siri_vm           | siri_vm_acp_id                       | 1056 MB
 siri_vm           | siri_vm_info                         | 8081 MB
 siri_vm           | siri_vm_location4d                   | 2548 MB
 siri_vm           | siri_vm_location4d_geom              | 1731 MB
 siri_vm           | siri_vm_pkey                         | 816 MB
 siri_vm           | siri_vm_ts                           | 775 MB
 siri_vm2          | siri_vm2_acp_id                      | 1379 MB
 siri_vm2          | siri_vm2_acp_ts                      | 763 MB
 siri_vm2          | siri_vm2_line_ref                    | 1071 MB
 siri_vm2          | siri_vm2_location4d                  | 2020 MB
 siri_vm2          | siri_vm2_origin_departure_ts         | 763 MB
 siri_vm2          | siri_vm2_origin_ref                  | 1379 MB
 siri_vm2          | siri_vm2_pkey                        | 763 MB
 siri_vm_3         | siri_vm_3_departure_ts               | 797 MB
 siri_vm_3         | siri_vm_3_info                       | 4269 MB
 siri_vm_3         | siri_vm_3_location                   | 1972 MB
 siri_vm_3         | siri_vm_3_recorded_date              | 797 MB
 siri_vm_3         | siri_vm_3_recorded_ts                | 797 MB
 siri_vm_4         | siri_vm_4_acp_id                     | 1471 MB
 siri_vm_4         | siri_vm_4_acp_lat                    | 814 MB
 siri_vm_4         | siri_vm_4_acp_lng                    | 814 MB
 siri_vm_4         | siri_vm_4_acp_ts                     | 814 MB
 siri_vm_4         | siri_vm_4_info                       | 4356 MB
 siri_vm_4         | siri_vm_4_location2d                 | 2848 MB
 siri_vm_4         | siri_vm_4_location2d_geom            | 2018 MB
 siri_vm_4         | siri_vm_4_location4d                 | 2841 MB
 siri_vm_4         | siri_vm_4_location4d_geom_nd         | 3482 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_acp_id             | 108 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_acp_lat            | 60 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_acp_lng            | 60 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_acp_ts             | 60 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_info               | 458 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_location2d         | 209 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_location2d_geom    | 156 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_location4d         | 208 MB
 siri_vm_5_2017_41 | siri_vm_5_2017_41_location4d_geom_nd | 258 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_acp_id             | 187 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_acp_lat            | 103 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_acp_lng            | 103 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_acp_ts             | 103 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_info               | 717 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_location2d         | 362 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_location2d_geom    | 269 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_location4d         | 362 MB
 siri_vm_5_2017_42 | siri_vm_5_2017_42_location4d_geom_nd | 444 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_acp_id             | 183 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_acp_lat            | 101 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_acp_lng            | 101 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_acp_ts             | 101 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_info               | 703 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_location2d         | 353 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_location2d_geom    | 265 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_location4d         | 354 MB
 siri_vm_5_2017_43 | siri_vm_5_2017_43_location4d_geom_nd | 424 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_acp_id             | 185 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_acp_lat            | 102 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_acp_lng            | 102 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_acp_ts             | 102 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_info               | 712 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_location2d         | 356 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_location2d_geom    | 266 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_location4d         | 356 MB
 siri_vm_5_2017_44 | siri_vm_5_2017_44_location4d_geom_nd | 426 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_acp_id             | 183 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_acp_lat            | 101 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_acp_lng            | 101 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_acp_ts             | 101 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_info               | 706 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_location2d         | 354 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_location2d_geom    | 263 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_location4d         | 356 MB
 siri_vm_5_2017_45 | siri_vm_5_2017_45_location4d_geom_nd | 435 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_acp_id             | 184 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_acp_lat            | 102 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_acp_lng            | 102 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_acp_ts             | 102 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_info               | 708 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_location2d         | 356 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_location2d_geom    | 266 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_location4d         | 356 MB
 siri_vm_5_2017_46 | siri_vm_5_2017_46_location4d_geom_nd | 438 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_acp_id             | 171 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_acp_lat            | 95 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_acp_lng            | 95 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_acp_ts             | 95 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_info               | 672 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_location2d         | 331 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_location2d_geom    | 246 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_location4d         | 331 MB
 siri_vm_5_2017_47 | siri_vm_5_2017_47_location4d_geom_nd | 417 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_acp_id             | 184 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_acp_lat            | 102 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_acp_lng            | 102 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_acp_ts             | 102 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_info               | 713 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_location2d         | 356 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_location2d_geom    | 263 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_location4d         | 356 MB
 siri_vm_5_2017_48 | siri_vm_5_2017_48_location4d_geom_nd | 438 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_acp_id             | 151 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_acp_lat            | 84 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_acp_lng            | 84 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_acp_ts             | 84 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_info               | 604 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_location2d         | 292 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_location2d_geom    | 219 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_location4d         | 293 MB
 siri_vm_5_2017_49 | siri_vm_5_2017_49_location4d_geom_nd | 353 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_acp_id             | 183 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_acp_lat            | 101 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_acp_lng            | 101 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_acp_ts             | 101 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_info               | 708 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_location2d         | 355 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_location2d_geom    | 262 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_location4d         | 355 MB
 siri_vm_5_2017_50 | siri_vm_5_2017_50_location4d_geom_nd | 439 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_acp_id             | 180 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_acp_lat            | 100 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_acp_lng            | 100 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_acp_ts             | 100 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_info               | 699 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_location2d         | 350 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_location2d_geom    | 258 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_location4d         | 350 MB
 siri_vm_5_2017_51 | siri_vm_5_2017_51_location4d_geom_nd | 420 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_acp_id             | 113 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_acp_lat            | 63 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_acp_lng            | 63 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_acp_ts             | 63 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_info               | 484 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_location2d         | 220 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_location2d_geom    | 164 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_location4d         | 218 MB
 siri_vm_5_2017_52 | siri_vm_5_2017_52_location4d_geom_nd | 271 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_acp_id             | 252 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_acp_lat            | 139 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_acp_lng            | 139 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_acp_ts             | 139 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_info               | 820 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_location2d         | 488 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_location2d_geom    | 358 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_location4d         | 489 MB
 siri_vm_5_2018_01 | siri_vm_5_2018_01_location4d_geom_nd | 590 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_acp_id             | 186 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_acp_lat            | 103 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_acp_lng            | 103 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_acp_ts             | 103 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_info               | 717 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_location2d         | 360 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_location2d_geom    | 265 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_location4d         | 361 MB
 siri_vm_5_2018_02 | siri_vm_5_2018_02_location4d_geom_nd | 451 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_acp_id             | 179 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_acp_lat            | 99 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_acp_lng            | 99 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_acp_ts             | 99 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_info               | 695 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_location2d         | 348 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_location2d_geom    | 259 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_location4d         | 348 MB
 siri_vm_5_2018_03 | siri_vm_5_2018_03_location4d_geom_nd | 430 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_acp_id             | 187 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_acp_lat            | 103 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_acp_lng            | 103 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_acp_ts             | 103 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_info               | 722 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_location2d         | 362 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_location2d_geom    | 268 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_location4d         | 361 MB
 siri_vm_5_2018_04 | siri_vm_5_2018_04_location4d_geom_nd | 449 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_acp_id             | 183 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_acp_lat            | 101 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_acp_lng            | 101 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_acp_ts             | 101 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_info               | 708 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_location2d         | 355 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_location2d_geom    | 263 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_location4d         | 354 MB
 siri_vm_5_2018_05 | siri_vm_5_2018_05_location4d_geom_nd | 441 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_acp_id             | 182 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_acp_lat            | 101 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_acp_lng            | 101 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_acp_ts             | 101 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_info               | 700 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_location2d         | 353 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_location2d_geom    | 262 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_location4d         | 353 MB
 siri_vm_5_2018_06 | siri_vm_5_2018_06_location4d_geom_nd | 431 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_acp_id             | 181 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_acp_lat            | 100 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_acp_lng            | 100 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_acp_ts             | 100 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_info               | 695 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_location2d         | 351 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_location2d_geom    | 259 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_location4d         | 352 MB
 siri_vm_5_2018_07 | siri_vm_5_2018_07_location4d_geom_nd | 426 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_acp_id             | 189 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_acp_lat            | 105 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_acp_lng            | 105 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_acp_ts             | 105 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_info               | 725 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_location2d         | 369 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_location2d_geom    | 273 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_location4d         | 368 MB
 siri_vm_5_2018_08 | siri_vm_5_2018_08_location4d_geom_nd | 446 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_acp_id             | 131 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_acp_lat            | 73 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_acp_lng            | 73 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_acp_ts             | 73 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_info               | 531 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_location2d         | 255 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_location2d_geom    | 191 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_location4d         | 254 MB
 siri_vm_5_2018_09 | siri_vm_5_2018_09_location4d_geom_nd | 313 MB
 siri_vm_5_2018_10 | siri_vm_5_2018_10_acp_id             | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_acp_lat            | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_acp_lng            | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_acp_ts             | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_info               | 16 kB
 siri_vm_5_2018_10 | siri_vm_5_2018_10_location2d         | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_location2d_geom    | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_location4d         | 8192 bytes
 siri_vm_5_2018_10 | siri_vm_5_2018_10_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_acp_id             | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_acp_lat            | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_acp_lng            | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_acp_ts             | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_info               | 16 kB
 siri_vm_5_2018_11 | siri_vm_5_2018_11_location2d         | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_location2d_geom    | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_location4d         | 8192 bytes
 siri_vm_5_2018_11 | siri_vm_5_2018_11_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_acp_id             | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_acp_lat            | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_acp_lng            | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_acp_ts             | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_info               | 16 kB
 siri_vm_5_2018_12 | siri_vm_5_2018_12_location2d         | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_location2d_geom    | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_location4d         | 8192 bytes
 siri_vm_5_2018_12 | siri_vm_5_2018_12_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_acp_id             | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_acp_lat            | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_acp_lng            | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_acp_ts             | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_info               | 16 kB
 siri_vm_5_2018_13 | siri_vm_5_2018_13_location2d         | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_location2d_geom    | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_location4d         | 8192 bytes
 siri_vm_5_2018_13 | siri_vm_5_2018_13_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_acp_id             | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_acp_lat            | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_acp_lng            | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_acp_ts             | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_info               | 16 kB
 siri_vm_5_2018_14 | siri_vm_5_2018_14_location2d         | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_location2d_geom    | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_location4d         | 8192 bytes
 siri_vm_5_2018_14 | siri_vm_5_2018_14_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_acp_id             | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_acp_lat            | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_acp_lng            | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_acp_ts             | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_info               | 16 kB
 siri_vm_5_2018_15 | siri_vm_5_2018_15_location2d         | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_location2d_geom    | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_location4d         | 8192 bytes
 siri_vm_5_2018_15 | siri_vm_5_2018_15_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_acp_id             | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_acp_lat            | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_acp_lng            | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_acp_ts             | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_info               | 16 kB
 siri_vm_5_2018_16 | siri_vm_5_2018_16_location2d         | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_location2d_geom    | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_location4d         | 8192 bytes
 siri_vm_5_2018_16 | siri_vm_5_2018_16_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_acp_id             | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_acp_lat            | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_acp_lng            | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_acp_ts             | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_info               | 16 kB
 siri_vm_5_2018_17 | siri_vm_5_2018_17_location2d         | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_location2d_geom    | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_location4d         | 8192 bytes
 siri_vm_5_2018_17 | siri_vm_5_2018_17_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_acp_id             | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_acp_lat            | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_acp_lng            | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_acp_ts             | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_info               | 16 kB
 siri_vm_5_2018_18 | siri_vm_5_2018_18_location2d         | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_location2d_geom    | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_location4d         | 8192 bytes
 siri_vm_5_2018_18 | siri_vm_5_2018_18_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_acp_id             | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_acp_lat            | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_acp_lng            | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_acp_ts             | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_info               | 16 kB
 siri_vm_5_2018_19 | siri_vm_5_2018_19_location2d         | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_location2d_geom    | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_location4d         | 8192 bytes
 siri_vm_5_2018_19 | siri_vm_5_2018_19_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_acp_id             | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_acp_lat            | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_acp_lng            | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_acp_ts             | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_info               | 16 kB
 siri_vm_5_2018_20 | siri_vm_5_2018_20_location2d         | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_location2d_geom    | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_location4d         | 8192 bytes
 siri_vm_5_2018_20 | siri_vm_5_2018_20_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_acp_id             | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_acp_lat            | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_acp_lng            | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_acp_ts             | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_info               | 16 kB
 siri_vm_5_2018_21 | siri_vm_5_2018_21_location2d         | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_location2d_geom    | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_location4d         | 8192 bytes
 siri_vm_5_2018_21 | siri_vm_5_2018_21_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_acp_id             | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_acp_lat            | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_acp_lng            | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_acp_ts             | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_info               | 16 kB
 siri_vm_5_2018_22 | siri_vm_5_2018_22_location2d         | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_location2d_geom    | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_location4d         | 8192 bytes
 siri_vm_5_2018_22 | siri_vm_5_2018_22_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_acp_id             | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_acp_lat            | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_acp_lng            | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_acp_ts             | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_info               | 16 kB
 siri_vm_5_2018_23 | siri_vm_5_2018_23_location2d         | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_location2d_geom    | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_location4d         | 8192 bytes
 siri_vm_5_2018_23 | siri_vm_5_2018_23_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_acp_id             | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_acp_lat            | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_acp_lng            | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_acp_ts             | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_info               | 16 kB
 siri_vm_5_2018_24 | siri_vm_5_2018_24_location2d         | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_location2d_geom    | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_location4d         | 8192 bytes
 siri_vm_5_2018_24 | siri_vm_5_2018_24_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_acp_id             | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_acp_lat            | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_acp_lng            | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_acp_ts             | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_info               | 16 kB
 siri_vm_5_2018_25 | siri_vm_5_2018_25_location2d         | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_location2d_geom    | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_location4d         | 8192 bytes
 siri_vm_5_2018_25 | siri_vm_5_2018_25_location4d_geom_nd | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_acp_id             | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_acp_lat            | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_acp_lng            | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_acp_ts             | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_info               | 16 kB
 siri_vm_5_2018_26 | siri_vm_5_2018_26_location2d         | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_location2d_geom    | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_location4d         | 8192 bytes
 siri_vm_5_2018_26 | siri_vm_5_2018_26_location4d_geom_nd | 8192 bytes
(374 rows)
```
