FROM gcr.io/oss-fuzz-base/base-builder-python

# Updating dependencies.
RUN apt-get update
RUN pip3 install --upgrade pip

# Environment configuration.
COPY *.sh *py $SRC/
WORKDIR $SRC/python-fuzz
