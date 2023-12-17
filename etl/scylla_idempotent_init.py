#!/usr/bin/env python3
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
if __name__ == "__main__":


    cluster = Cluster(contact_points=['scylla-client.scylla.svc.cluster.local'])
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS weather
        WITH replication = {'class': 'NetworkTopologyStrategy', 'replication_factor': '2'}
    """)

    session.execute("USE weather")
    session.execute("""
        CREATE TABLE IF NOT EXISTS stations (
                    station_id text,
                    name text,
                    latitude float,
                    longitude float,
                    elevation float,
                    PRIMARY KEY (station_id)
        )
    """)