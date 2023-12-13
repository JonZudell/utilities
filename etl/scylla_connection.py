#!/usr/bin/env python3
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
if __name__ == "__main__":


    cluster = Cluster(contact_points=['scylla-us-east-1-us-east-1a-0.scylla.default.svc.cluster.local'])
    session = cluster.connect()
    session.default_consistency_level = ConsistencyLevel.QUORUM
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS weather
        WITH replication = {'class': 'NetworkTopologyStrategy', 'replication_factor': '2'}
    """)

    session.execute("USE weather")
    session.execute("""
        CREATE TABLE tbl (pk int PRIMARY KEY, v int)
        WITH per_partition_rate_limit = {'max_writes_per_second': 1}
    """)