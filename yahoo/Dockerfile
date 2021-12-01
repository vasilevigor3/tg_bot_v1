FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron
# RUN apt-get update && apt-get -y install python

RUN mkdir /src
# Copy hello-cron file to the cron.d directory
COPY . /src

# Give execution rights on the cron job
RUN chmod 0644 /src

# Apply cron job
RUN crontab /src/hello-cron

# Create the log file to be able to run tail
RUN touch /src/cron.log

# Run the command on container startup
CMD cron && tail -f /src/cron.log

# FROM ubuntu:latest
#
# RUN mkdir /src
# WORKDIR /src
# COPY . /src

