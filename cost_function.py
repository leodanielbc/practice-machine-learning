from matplotlib import cm  # Para manejar colores
import numpy as np # Para el manejo de vectores
import matplotlib.pyplot as plt # Para las graficas


def f(x, y):
    return x**2 + y**2


if __name__ == "__main__":
    # Espacio tridimensional
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    res = 100 # resolucion de 100 puntos

    # Ejes
    x = np.linspace(-4, 4, res)
    y = np.linspace(-4, 4, res)

    # Pares de X y Y
    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)
    # Superficies
    surf = ax.plot_surface(X, Y, Z, cmap=cm.cool)

    fig.colorbar(surf)  # Barra de colores, se difuja la funcion de coste
    plt.show()

    # Curvas de nivel
    level_map = np.linspace(np.min(Z), np.max(Z), res)
    plt.contourf(X, Y, Z, level_map, cmap=cm.cool)
    plt.colorbar()
    plt.title("Descenso del gradiente")
    plt.show()
