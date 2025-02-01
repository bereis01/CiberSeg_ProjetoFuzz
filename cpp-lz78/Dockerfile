FROM gcr.io/oss-fuzz-base/base-builder

RUN apt-get update && apt-get install -y make

RUN git clone https://github.com/bereis01/cpp-lz78 my-git-repo

WORKDIR my-git-repo

COPY build.sh $SRC/