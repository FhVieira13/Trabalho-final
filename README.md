import numpy as np
from sklearn.cluster import KMeans

dados_produtos = np.array([
    [10, 2], [15, 3], [12, 1],
    [200, 9], [180, 8], [210, 10]
])

modelo_produtos = KMeans(n_clusters=2, random_state=42, n_init=10)
modelo_produtos.fit(dados_produtos)

produtos_ancora = modelo_produtos.cluster_centers_

print(f"Características dos Produtos Âncora (Preço, Popularidade):\n{produtos_ancora}")
