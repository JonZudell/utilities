#!/usr/bin/env python3
import sys
import json

def write_json(path, stations_list):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(stations_list))

def get_id(line):
    return line[0:11]

def get_latitude(line):
    return float(line[12:20])

def get_longitude(line):
    return float(line[21:30])

def get_elevation(line):
    return float(line[31:37])

def get_wmo_id(line):
    return line[80:85].strip()

def get_name(line):
    return line[42:72].strip()

def read_lines(stations_path):
    results = []
    with open(stations_path) as stations:
        for line in stations.readlines():
            station = get_id(line)
            wmo_id = get_wmo_id(line)
            if wmo_id:
                results.append({"station" :station, "wmo_id" : wmo_id, "name" : get_name(line), "latitude" : get_latitude(line), "longitude" : get_longitude(line), "elevation" : get_longitude(line)})
    return results

if __name__ == "__main__":
    stations_path = sys.argv[1]
    output_path = sys.argv[2]
    write_json(output_path, read_lines(stations_path))