import atheris

# Instrumentalizes imported modules.
with atheris.instrument_imports(enable_loader_override=False):
    import sys
    from bs4 import BeautifulSoup

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    code = fdp.ConsumeUnicode(sys.maxsize)  # Gera um código aleatório em Python
    try:
        app = flake8.main.application.Application()
        app.run_checks([code])
    except Exception as e:
        if "Traceback" in str(e):  # Se houver um erro inesperado
            raise RuntimeError("Flake8 crash detected")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
