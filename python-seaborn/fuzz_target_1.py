import atheris
import sys
import seaborn as sns

def TestOneInput(data):
    """Função chamada pelo fuzzer com dados aleatórios."""
    if len(data) < 2:  # Evita entradas muito curtas
        return

    try:
        # Usa os bytes como dados numéricos para o Seaborn
        values = [b % 256 for b in data[:10]]  # Limita os valores a um intervalo válido

        # Testa um gráfico simples no Seaborn
        sns.lineplot(x=range(len(values)), y=values)

    except Exception as e:
        if "Traceback" in str(e):
            raise RuntimeError("Seaborn crash detected")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
