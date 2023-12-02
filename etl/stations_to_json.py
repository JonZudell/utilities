#!/usr/bin/env python3
import sys
import json

def write_json(path, stations_list):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(stations_list))

def get_id(line):
    return line[0:11]

def get_wmo_id(line):
    return line[80:85].strip()

def read_lines(stations_path):
    results = []
    with open(stations_path) as stations:
        for line in stations.readlines():
            station = get_id(line)
            wmo_id = get_wmo_id(line)
            # if wmo_id:
            results.append({"station" : get_id(line), "wmo_id" : wmo_id})
    return results

if __name__ == "__main__":
    stations_path = sys.argv[1]
    output_path = sys.argv[2]
    write_json(output_path, read_lines(stations_path))