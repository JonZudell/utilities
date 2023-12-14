FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-full python3-pip -y
RUN mkdir /etl
COPY ./etl/requirements.txt /etl/
COPY ./etl/stations_to_json.py /etl/
COPY ./etl/slice_stations.py /etl/
COPY ./etl/transform_station_csv.py /etl/
COPY ./etl/scylla_idempotent_init.py /etl/
RUN pip install --break-system-packages -r /etl/requirements.txt
ENTRYPOINT [ "/bin/bash", "-c" ]
