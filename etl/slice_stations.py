#!/usr/bin/env python3
import sys
import json

def stations_as_string(stations_path):
    result = None
    with open(stations_path) as stations:
        result =stations.read()
    return result

def write_json(path, stations_list):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(stations_list))

if __name__ == "__main__":
    stations_path = sys.argv[1]
    output_path = sys.argv[2]
    slice_index = int(sys.argv[3])
    number_of_slices = int(sys.argv[4])

    stations = json.loads(stations_as_string(stations_path))

    stations_per_slice = len(stations) / number_of_slices

    print("Stations per slice:",stations_per_slice)
    write_json(output_path, stations[slice_index::number_of_slices])