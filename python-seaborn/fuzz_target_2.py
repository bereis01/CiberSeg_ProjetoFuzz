import atheris
import sys
import seaborn as sns
import matplotlib.pyplot as plt

def TestOneInput(data):
    """Função chamada pelo fuzzer com dados aleatórios."""
    if len(data) < 2:  # Garante que há dados suficientes
        return
    
    try:
        # Usa os bytes como dados numéricos para o gráfico
        values = [b for b in data[:10]]  # Usa até 10 valores

        # Tenta criar um gráfico de dispersão simples
        plt.figure()
        sns.scatterplot(x=range(len(values)), y=values)
        plt.close()

    except Exception as e:
        if "Traceback" in str(e):
            raise RuntimeError("Seaborn crash detected")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
