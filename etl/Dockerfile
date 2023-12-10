FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-full python3-pip python3-cassandra-driver -y
RUN mkdir /etl
COPY ./stations_to_json.py /etl/
COPY ./slice_stations.py /etl/
COPY ./transform_station_csv.py /etl/
COPY ./scylla_connection.py /etl/
ENTRYPOINT [ "/bin/bash", "-c" ]
