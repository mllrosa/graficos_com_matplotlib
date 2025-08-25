import matplotlib.pyplot as plt

dados = [30, 50, 10]
# labels = [ f"x{30}", f"y{50}", f"z{10}"]
# labels = [f"x{valor}" for valor in dados]

# resto do código para rodar.
plt.bar(labels, dados) # Cria o gráfico de barras
plt.title("Matplotlib")
plt.show()