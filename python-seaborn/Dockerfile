FROM gcr.io/oss-fuzz-base/base-builder-python

RUN pip install --upgrade pip
RUN git clone https://github.com/mwaskom/seaborn.git python-fuzz

COPY *.sh *py $SRC/

WORKDIR $SRC/python-fuzz
