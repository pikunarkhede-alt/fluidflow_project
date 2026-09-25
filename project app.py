import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🌊 Fluid Flow Simulation")

# User inputs
U = st.number_input("Free Stream Velocity U∞", value=5.0)
R = st.number_input("Radius R", value=1.0)
Gamma = st.number_input("Circulation Γ", value=0.0)
alpha = st.number_input("Angle of Attack α (°)", value=0.0)

# Grid
x = np.linspace(-4, 4, 150)
y = np.linspace(-4, 4, 150)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Avoid singularity
Z[np.abs(Z) < R] = np.nan

# Complex velocity
V = (
    U * np.exp(-1j * np.radians(alpha))
    * (1 - R**2 / Z**2)
    + 1j * Gamma / (2 * np.pi * Z)
)

u = np.real(V)
v = -np.imag(V)

# Plot
fig, ax = plt.subplots()

ax.streamplot(X, Y, u, v, density=1.5)

t = np.linspace(0, 2*np.pi, 200)
ax.plot(R*np.cos(t), R*np.sin(t), "k", linewidth=2)

ax.set_aspect("equal")
ax.set_title("Fluid Flow Around Cylinder")
ax.set_xlabel("x")
ax.set_ylabel("y")

st.pyplot(fig)