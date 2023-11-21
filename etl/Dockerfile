FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-full python3-pip -y
RUN mkdir /etl
COPY ./etl/stations_to_json.py /etl/
ENTRYPOINT [ "/bin/bash", "-c" ]