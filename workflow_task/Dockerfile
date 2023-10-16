FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-jwt -y
RUN mkdir /utilities
COPY ./generate_jwt.py /utilities/
ENTRYPOINT [ "/bin/bash", "-c" ]