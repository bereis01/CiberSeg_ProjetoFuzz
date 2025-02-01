FROM gcr.io/oss-fuzz-base/base-builder-python

# Updating dependencies.
RUN apt-get update
RUN pip3 install --upgrade pip

RUN apt-get -y install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
    flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig zlib1g-dev

# Environment configuration.
COPY *.sh *py $SRC/
WORKDIR $SRC/python-fuzz
