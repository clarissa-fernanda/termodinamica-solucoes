import numpy as np
from scipy.constants import Boltzmann as kB, zero_Celsius
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Constant values
a = 6e-4
delta_S = 17.9 * kB
beta = 2/60

# List of A and B_ values
A_values = [40, 9.64e6, 1.1e6]  #  A values
B_values = [4.3e4, 3.9e5, 4.9e5]  #  B_ values

# List of labels
labels = ["0% de inibidor cinetico", "0.5% de inibidor cinetico ", "1% de de inibidor cinetico"]

# Define the function to find its root
def P(delta_T, A, B_):
    return 1 - np.exp(-a * A * np.exp((delta_S * delta_T) / (kB * T)) * np.exp(-B_ / (T * delta_T ** 2)) * delta_T / beta)

delta_T = np.linspace(0, 13, num=120)
T = (8.7 + zero_Celsius) - delta_T

plt.figure(num=1, dpi=120)
plt.xlim(0, 13)
plt.ylim(-0.1, 1.1)

# Loop through each pair of A and B_ values
for A, B_, label in zip(A_values, B_values, labels):
    plt.scatter(delta_T, P(delta_T, A, B_), label=label, s=6)

plt.legend()  # Add a legend to the plot
plt.xlim(0, 13)
plt.xlabel('Subresfriamento / K')
plt.ylabel('Probabilidade acumulada de formação')
plt.show()

for A, B_, label in zip(A_values, B_values, labels):
    P_values = P(delta_T, A, B_)

    # Interpolar os valores de delta_T correspondentes a P(delta_T) = 0.5
    interp_func = interp1d(P_values, delta_T)
    delta_T_05 = interp_func(0.5)

    print(f"{label}: delta_T at P=0.5 = {delta_T_05:.2f} K")
    print(f"{label}: mean = {np.mean(delta_T[np.where((P_values > 0) & (P_values < 1))[0]])}")
