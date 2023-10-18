FROM debian
RUN apt update
RUN apt install jq curl git bash python3 python3-full python3-pip -y
RUN python3 -m pip install jwt --break-system-packages
RUN mkdir /utilities
COPY ./generate_jwt.py /utilities/
ENTRYPOINT [ "/bin/bash", "-c" ]