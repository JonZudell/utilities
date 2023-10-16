FROM debian
RUN apt update
RUN apt install jq curl git bash python3 pip3 -y
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir /utilities
COPY ./generate_jwt.py /utilities/
ENTRYPOINT [ "/bin/bash", "-c" ]