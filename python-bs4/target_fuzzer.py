#!/usr/bin/python3
import sys
import bs4
import atheris


# Fuzz target definition.
def TestOneInput(data):
    # Creates a data provider for generating custom data.
    fdp = atheris.FuzzedDataProvider(data)

    # Generates data of a custom type.
    input = fdp.ConsumeString(fdp.ConsumeIntInRange(1, 4096))

    # Executes the target function with the fuzzing input data.
    try:
        soup = bs4.BeautifulSoup(input)
        soup.get_text()
    except:
        return


# Initializes and executes the fuzzing engine.
def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
