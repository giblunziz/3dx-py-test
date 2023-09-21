# %matplotlib qt

import matplotlib.pyplot as plt
import numpy as np

# Créer des données paramétriques pour les axes t
t = np.linspace(0, 10 * np.pi, 1000)

# Calculer les coordonnées x, y et z en fonction de t
x = np.sin(t) * (np.e ** (np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
y = np.cos(t) * (np.e ** (np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
z = t

# Créer un objet Axes3D pour le graphique 3D
plt.figure("Un joli papillon (vu par le haut)")
axes = plt.axes(projection="3d")

# Tracer les spirales paramétriques en 3D
axes.plot(x, y, z, "r")

# Ajouter des étiquettes pour les axes
axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_zlabel("Z")

# Afficher le graphique
plt.show()
