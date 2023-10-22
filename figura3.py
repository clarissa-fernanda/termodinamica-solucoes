import numpy as np
from scipy.constants import Boltzmann as kB, zero_Celsius
import matplotlib.pyplot as plt

# J values with uncertainties
J_values = [0.80e-4, 1.5e-4, 3.85e-4, 9.15e-4]
labels = ["ΔT=6.0K", "ΔT=6.9K", "ΔT=7.9K", "ΔT=9.0K"]

# Generate an array of t values
t = np.linspace(10**1, 10**5, num=10**4)

# Create a figure and axis
plt.figure()
plt.ylim(0, 1)

# Plot P(t, J) as data points with error bars
for J, label in zip(J_values, labels):
  P = 1 - np.exp(-J * t)
  plt.scatter(t, P, label=label,s=2)

plt.legend()
plt.xscale('log')
plt.xlabel('t(s)')
plt.ylabel('Distribuição de probabilidade acumulada')
plt.title('P vs. t para valores de ΔT ')
plt.show()

A = 0.0021202064985412503
B_ = 41419.21745544927
T = 12.25 + zero_Celsius
delta_S = 20 * kB

def J(delta_T, A, B_):
  return A * np.exp((delta_S * delta_T) / (kB * T)) * np.exp(-B_ / (T * delta_T ** 2))

# Your optimal J values and corresponding delta_T values
delta_T = np.linspace(0, 15, num=10)

# Plotting the J values against delta_T values
plt.figure()  # Create a new figure
plt.plot(delta_T, J(delta_T, A, B_)/1e-3, label='Ajuste', linestyle='--')
plt.scatter(delta_T, J(delta_T, A, B_)/1e-3)
plt.xlabel('ΔT Subresfriamento (K)')
plt.ylabel('J / 10^-3 s⁻1')
plt.ylim(0, 2)
plt.legend()
plt.show()