import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 10))

# Draw system boundary
system_box = patches.Rectangle((2, 1), 10, 8, linewidth=2, edgecolor='black', facecolor='lightgrey')
ax.add_patch(system_box)
ax.text(7, 8.8, "Sistema Vida+", fontsize=14, ha="center", va="top", weight='bold')

# Actors
ax.text(0.5, 7, "Secretária", fontsize=12, ha="center")
ax.plot([1.5, 2], [7, 6.5], color='black')  # Line to "Cadastrar Paciente"
ax.plot([1.5, 2], [7, 5.5], color='black')  # Line to "Agendar Consulta"
ax.plot([1.5, 2], [7, 4.5], color='black')  # Line to "Confirmar Consulta"
ax.plot([1.5, 2], [7, 3.5], color='black')  # Line to "Cancelar Consulta"

ax.text(13, 5, "Médico", fontsize=12, ha="center")
ax.plot([12, 10.5], [5, 3.5], color='black')  # Line to "Cancelar Consulta"
ax.plot([12, 10.5], [5, 2.5], color='black')  # Line to "Gerar Receita"

# Use Cases
def draw_use_case(x, y, label):
    circle = patches.Ellipse((x, y), 3.2, 1, edgecolor='black', facecolor='white')
    ax.add_patch(circle)
    ax.text(x, y, label, ha="center", va="center", fontsize=11)

draw_use_case(4, 6.5, "Cadastrar Paciente")
draw_use_case(4, 5.5, "Agendar Consulta")
draw_use_case(4, 4.5, "Confirmar Consulta")
draw_use_case(4, 3.5, "Cancelar Consulta")

draw_use_case(10, 3.5, "Cancelar Consulta")
draw_use_case(10, 2.5, "Gerar Receita")
draw_use_case(7, 1.5, "Imprimir Receita")

# Relationships
# Gerar Receita -> include -> Imprimir Receita
ax.annotate("<<include>>", xy=(8.5, 2.5), xytext=(7.2, 1.9),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)

# Hide axes
ax.axis('off')
plt.xlim(0, 14)
plt.ylim(0, 10)
plt.tight_layout()
plt.show()
