FROM gcr.io/oss-fuzz-base/base-builder-python

# Updating dependencies.
RUN apt-get update
RUN pip3 install --upgrade pip

# Fuzzing code.
RUN git clone https://github.com/pymupdf/PyMuPDF python-pymupdf

# Environment configuration.
COPY *.sh *py $SRC/
WORKDIR $SRC/python-pymupdf
