import atheris
import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def TestOneInput(data):
    """Função chamada pelo fuzzer com dados aleatórios."""
    fdp = atheris.FuzzedDataProvider(data)

    try:
        # Gera um DataFrame aleatório
        num_rows = fdp.ConsumeIntInRange(5, 50)
        num_cols = fdp.ConsumeIntInRange(2, 5)
        df = pd.DataFrame({
            f"col_{i}": fdp.ConsumeIntList(num_rows) for i in range(num_cols)
        })

        # Configura o estilo do Seaborn
        sns.set_theme()

        # Tenta criar diferentes tipos de gráficos
        plt.figure()
        sns.pairplot(df)
        plt.close()

        plt.figure()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        plt.close()

        plt.figure()
        sns.boxplot(data=df)
        plt.close()

    except Exception as e:
        if "Traceback" in str(e):
            raise RuntimeError("Seaborn crash detected")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
