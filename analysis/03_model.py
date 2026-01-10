from scripts.01_read_data import read_cells, read_sources
from scripts.02_spreading_solver import spreading_solver
import pandas as pd

# ----------------------------
# EINLESEN
# ----------------------------
cells = read_cells("data/input/raster_cells.xlsx")
sources = read_sources("data/input/waste_heat_sources.xlsx")

all_results = []

# ----------------------------
# JE QUELLE SPREADING
# ----------------------------
for _, source in sources.iterrows():

    cells, remaining = spreading_solver(cells, source)

    cells["source_id"] = source["source_id"]
    all_results.append(cells)

# ----------------------------
# EXPORT
# ----------------------------
result_cells = pd.concat(all_results)

result_cells.to_excel(
    "data/output/results_cells.xlsx",
    index=False
)
