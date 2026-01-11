import pulp as pl

# ----------------------------
# DATEN
# ----------------------------
cells = {
    "C1": {"demand": 50, "distance": 0},
    "C2": {"demand": 40, "distance": 1},
    "C3": {"demand": 30, "distance": 1},
    "C4": {"demand": 20, "distance": 2},
    "C5": {"demand": 10, "distance": 3},
}

supply = 100

# ----------------------------
# MODELL
# ----------------------------
model = pl.LpProblem("Abwaerme_Spreading", pl.LpMinimize)

x = {
    c: pl.LpVariable(f"x_{c}", lowBound=0)
    for c in cells
}

# Zielfunktion: Distanzgewichtete Lieferung
model += pl.lpSum(cells[c]["distance"] * x[c] for c in cells)

# Nachfrage
for c in cells:
    model += x[c] <= cells[c]["demand"]

# Angebot
model += pl.lpSum(x[c] for c in cells) <= supply

# ----------------------------
# LÖSEN
# ----------------------------
model.solve()

# ----------------------------
# AUSGABE
# ----------------------------
for c in cells:
    print(c, x[c].value())
