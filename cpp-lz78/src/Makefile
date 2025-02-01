CXXFLAGS += -std=c++11

all: compression_fuzzer

clean:
	rm -fv *.a *.o *unittest *_fuzzer *_seed_corpus.zip crash-* *.zip

check: all
	./compression_fuzzer compression_test_data/*

# Fuzz targets.
compression_fuzzer: compression_fuzzer.cpp LZ78.a
	${CXX} ${CXXFLAGS} $< LZ78.a ${LIB_FUZZING_ENGINE} -o $@
	zip -q -r compression_fuzzer_seed_corpus.zip compression_test_data

# The library itself.
LZ78.a: LZ78.cpp LZ78.h
	${CXX} ${CXXFLAGS} $< -c
	ar ruv LZ78.a LZ78.o