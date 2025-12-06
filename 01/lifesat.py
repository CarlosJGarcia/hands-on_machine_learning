import csv
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

path = Path('data/lifesat.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)

# Muestro la primera fila
header_row = next(reader)
print()
for index, column_header in enumerate(header_row):
    print(f"[{index}] {column_header}", end=" / ")
print()

# Creo dos listas con los datos en las columnas 1 y 2
x = [] # GDP per capita
y = []  # Life satisfaction
for row in reader:
    # Get values and convert to float
    gdp = float(row[1])
    life = float(row[2])
    x.append(gdp)
    y.append(life)

# Gráfico
plt.scatter(x, y)
# plt.show()


# Select a linear model - selecciono el modelo Regresion Lineal de Scikit-learn
model = LinearRegression()

# SVR with RBF kernel (smooth nonlinear)
svr = SVR(kernel='rbf', C=1.0, gamma='scale')




# Train the model
# Create numpy arrays from the lists x and y
x_np = np.array(x).reshape(-1, 1)
y_np = np.array(y).reshape(-1, 1)

"""
print("x =", x)
print("x_np = ", x_np)
print("y =", y)
print("y_np = ", y_np)
"""

model.fit(x_np, y_np)
svr.fit(x_np, y_np.ravel())



# Para cada valor de x, predigo el valor de y usando el modelo entrenado
y_pred = []  # Life satisfaction predicha
for valor in x:
    valor_np = np.array(valor).reshape(-1, 1)
    prediccion = model.predict(valor_np)
    y_pred.append(prediccion[0][0])
y_svr = []  # Life satisfaction predicha
for valor in x:
    valor_np = np.array(valor).reshape(-1, 1)
    prediccion = svr.predict(valor_np)
    y_svr.append(prediccion[0])

# Dibujo la línea de regresión
plt.plot(x, y_pred, color='red')
plt.plot(x, y_svr, color='green')
plt.title("Regresion Lineal vs Support Vector Regression (SVR)")
plt.show()

print("Fin del programa.")
2e3