FROM ubuntu:24.04

# install curl and tools for testing
RUN apt update && apt install curl coreutils -y

# create a low-privilege user to run the app
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m -d /home/appuser -s /bin/false appuser

# copy script into appuser's home directory
COPY --chown=appuser:appgroup --chmod=0700 curl-time.sh /home/appuser/

# change working directory
WORKDIR /home/appuser

# switch to low-privilege user before running the app
USER appuser

# launch the client application
ENTRYPOINT ["/bin/bash", "/home/appuser/curl-time.sh"]
