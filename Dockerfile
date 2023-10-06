FROM alpine
RUN apk update
RUN apk add jq curl docker git
