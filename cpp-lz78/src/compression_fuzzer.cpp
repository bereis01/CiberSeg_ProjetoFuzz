#include <string>
#include <sstream>

#include "LZ78.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    std::string str(reinterpret_cast<const char *>(data), size);

    std::stringstream input;
    std::stringstream output;

    input << str;
    compress(input, output);

    return 0;
}