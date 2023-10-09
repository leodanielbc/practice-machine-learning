from matplotlib import cm  # Para manejar colores
import numpy as np # Para el manejo de vectores
import matplotlib.pyplot as plt # Para las graficas


def f(x, y):
    return x**2 + y**2

h = 0.01

def partialDerivate(_p,p):
    return  (f(_p[0],_p[1]) - f(p[0],p[1])) / h

def gradientDescend():

    x_history = []  # Para almacenar las coordenadas x
    y_history = []  # Para almacenar las coordenadas y

    p = np.random.rand(2) * 8 - 4 # generar dos valores aleatorios

    plt.plot(p[0],p[1],'o', c='k')

    lr = 0.01
    # h = 0.01

    grad = np.zeros(2)

    for i in range(10000):
        for idx, val in enumerate(p):
            _p = np.copy(p)

            _p[idx] = _p[idx] + h

            dp = partialDerivate(_p,p)

            grad[idx] = dp

        p = p - lr * grad

        if(i % 10 == 0):
            plt.plot(p[0],p[1],'o', c='r')
            x_history.append(p[0])
            y_history.append(p[1])

    plt.plot(p[0],p[1],'o', c='w')
    plt.colorbar(label='Nivel de Contorno')
    plt.scatter(x_history, y_history, c=range(len(x_history)), cmap=cm.autumn)
    plt.colorbar(label='Paso de Descenso')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    print("El punto mínimo se encuentra en: ", p)


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
    surf = ax.plot_surface(X, Y, Z, cmap=cm.jet)

    fig.colorbar(surf)  # Barra de colores, se difuja la funcion de coste
    plt.show()

    # Curvas de nivel, desenso de gradiente
    level_map = np.linspace(np.min(Z), np.max(Z), res)
    plt.contourf(X, Y, Z, level_map, cmap=cm.jet) # Agregar líneas de contorno

    gradientDescend()

