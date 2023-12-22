#!/usr/bin/env python3
import sys
import json
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
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

def read_lines(stations_path, session):
    insert_ps = session.prepare(
        query="INSERT INTO stations_v2 (station_id,wmo_id,name,latitude,longitude,elevation) VALUES (?,?,?,?,?,?)"
    )
    results = []
    with open(stations_path) as stations:
        for line in stations.readlines():
            station = get_id(line)
            wmo_id = get_wmo_id(line)
            if wmo_id:
                name =  get_name(line)
                latitude = get_latitude(line)
                longitude = get_longitude(line)
                elevation = get_elevation(line)
                results.append({"station" :station, "wmo_id" : wmo_id, "name" : name, "latitude" : latitude, "longitude" : longitude, "elevation" : elevation})
                session.execute(query=insert_ps, parameters=[station, wmo_id, name, latitude, longitude, elevation])
    return results

if __name__ == "__main__":
    cluster = Cluster(contact_points=['scylla-client.scylla.svc.cluster.local'])
    session = cluster.connect()
    stations_path = sys.argv[1]
    output_path = sys.argv[2]
    write_json(output_path, read_lines(stations_path, session))