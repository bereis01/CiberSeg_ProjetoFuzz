#!/usr/bin/python3
import io
import sys
import atheris
import pymupdf
from pypdf import PdfWriter


# Fuzz target definition.
def TestOneInput(data):
    # Generates a PDF with the initial bytes.
    dummy = io.BytesIO()
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.add_attachment("smile.png", data)
    writer.write(dummy)

    # Executes the target function with the fuzzing input data.
    try:
        doc = pymupdf.open(dummy)
        for page in doc:
            page.get_contents()
    except:
        return


# Initializes and executes the fuzzing engine.
def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
