#!/usr/bin/env python3
import sys
import json

def write_json(path, stations_list):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(stations_list))

def parse_line(line):
    return line[0:11]

def read_lines(stations_path):
    results = { 'stations': []}
    with open(stations_path) as stations:
        for line in stations.readlines():
            results['stations'].append({"station" : parse_line(line) })
    return results

if __name__ == "__main__":
    stations_path = sys.argv[1]
    output_path = sys.argv[2]
    write_json(output_path, read_lines(stations_path))