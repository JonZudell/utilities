#!/usr/bin/env python3
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import WhiteListRoundRobinPolicy, DowngradingConsistencyRetryPolicy
from cassandra.query import tuple_factory
if __name__ == "__main__":


    cluster = Cluster(contact_points=['scylla-us-east-1-us-east-1a-0.scylla.svc.cluster.local'])
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS keyspace1
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """)

    session.execute("USE keyspace1")
    session.execute("""
        CREATE TABLE tbl (pk int PRIMARY KEY, v int)
        WITH per_partition_rate_limit = {'max_writes_per_second': 1}
    """)