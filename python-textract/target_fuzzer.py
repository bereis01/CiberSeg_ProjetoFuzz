#!/usr/bin/python3
import sys
import atheris
import textract
import tempfile
from pypdf import PdfWriter


# Fuzz target definition.
def TestOneInput(data):
    # Generates a PDF with the initial bytes.
    dummy = tempfile.NamedTemporaryFile(suffix=".pdf")
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.add_attachment("smile.png", data)
    writer.write(dummy.name)

    # Executes the target function with the fuzzing input data.
    try:
        dummy.seek(0)
        textract.process(dummy.name)
    except:
        return


# Initializes and executes the fuzzing engine.
def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
