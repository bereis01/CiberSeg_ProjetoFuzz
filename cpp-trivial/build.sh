#!/bin/bash -eu
make clean  # Not strictly necessary, since we are building in a fresh dir.
make -j$(nproc) all    # Build the fuzz targets.
make -j$(nproc) check  # Sanity check, not strictly required, but nice to have.

# Copy the fuzzer executables and zip-ed corpora to $OUT.
find . -name '*_fuzzer' -exec cp -v '{}' $OUT ';'
find . -name '*_fuzzer_seed_corpus.zip' -exec cp -v '{}' $OUT ';'