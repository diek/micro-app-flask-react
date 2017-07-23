FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y memcached && \
    apt-get clean

EXPOSE 11211

CMD ["-u", "root", "-m", "1000"]
USER daemon
ENTRYPOINT memcached
