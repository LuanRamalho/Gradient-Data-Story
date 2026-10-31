import pandas as pd
import matplotlib.pyplot as plt

# Dados
df = pd.DataFrame({
    "Day": range(1, 8),
    "Growth": [12, 18, 16, 30, 42, 38, 65]
})

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 5))

# Equivalente ao geom_area (preenchimento sob a curva)
ax.fill_between(df["Day"], df["Growth"], color="#00C9FF", alpha=0.35)

# Equivalente ao geom_line (linha)
ax.plot(df["Day"], df["Growth"], color="#7B2FF7", linewidth=2)

# Equivalente ao geom_point (pontos)
ax.scatter(df["Day"], df["Growth"], color="#FF4DAB", s=50, zorder=3)

# Personalizações (equivalente ao theme_minimal e labs)
ax.set_title("Weekly Growth Journey", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Day", fontsize=11)
ax.set_ylabel("Growth", fontsize=11)

# Estilo minimalista (removendo bordas superiores e direitas)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, linestyle='--', alpha=0.5)

# Exibir o gráfico
plt.tight_layout()
plt.show()