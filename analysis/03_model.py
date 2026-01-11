import importlib.util
from pathlib import Path
import pandas as pd

def _load_module(name, path):
	spec = importlib.util.spec_from_file_location(name, str(path))
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module

# ----------------------------
# EINLESEN
# ----------------------------
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"

read_data_module = _load_module(
	"read_data_module", scripts_dir / "01_read_data.py"
)
read_cells = read_data_module.read_cells
read_sources = read_data_module.read_sources

spreading_module = _load_module(
	"spreading_solver_module", scripts_dir / "02_spreading_solver.py"
)
spreading_solver = spreading_module.spreading_solver

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
	index=False)
