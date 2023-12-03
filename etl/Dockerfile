FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-full python3-pip -y
RUN mkdir /etl
COPY ./stations_to_json.py /etl/
COPY ./slice_stations.py /etl/
ENTRYPOINT [ "/bin/bash", "-c" ]
