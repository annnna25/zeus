import numpy as np

def spreading_solver(cells, source):
    """
    cells: DataFrame mit [cell_id, row, col, demand]
    source: Series mit [source_id, row, col, supply]
    """

    # Kopien
    cells = cells.copy()
    remaining_supply = source["supply"]

    # Ergebnis-Spalten
    cells["allocated_heat"] = 0.0
    cells["remaining_demand"] = cells["demand"]

    # Distanz berechnen
    cells["distance"] = (
        abs(cells["row"] - source["row"]) +
        abs(cells["col"] - source["col"])
    )

    # Nach Distanz sortieren (Netzlogik!)
    cells = cells.sort_values("distance")

    # Spreading
    for idx, cell in cells.iterrows():

        if remaining_supply <= 0:
            break

        if cell["remaining_demand"] <= 0:
            continue

        allocation = min(
            remaining_supply,
            cell["remaining_demand"]
        )

        cells.at[idx, "allocated_heat"] += allocation
        cells.at[idx, "remaining_demand"] -= allocation
        remaining_supply -= allocation

    return cells, remaining_supply
