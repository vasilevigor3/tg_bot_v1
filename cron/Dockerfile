FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron
RUN apt-get update && apt-get install -y dos2unix
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y python3.9
RUN apt-get update && apt-get install -y python3-pip
RUN add-apt-repository ppa:deadsnakes/ppa
COPY . .
RUN export PATH="$PATH:/usr/bin/python3"
RUN pip3 install -r requirements.txt

# Add crontab file (from your windows host) to the cron directory
ADD my-crontab /etc/cron.d/my-crontab
ADD update_figi_job.py /etc/

# Change line ending format to LF
RUN dos2unix /etc/cron.d/my-crontab
RUN dos2unix /etc/update_figi_job.py

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/my-crontab
RUN chmod 0644 /etc/update_figi_job.py
RUN chmod -R 755 /usr/bin/python3

# Apply cron job
RUN crontab /etc/cron.d/my-crontab

# Create the log file to be able to run tail
RUN touch /var/log/my-crontab.log

# Run the command on container startup
CMD cron && tail -f /var/log/my-crontab.log