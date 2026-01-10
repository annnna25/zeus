import pandas as pd

# ----------------------------
# ZENTRALE SPALTENDEFINITION
# ----------------------------
CELL_COLUMNS = {
    "id": "cell_id",
    "row": "row",
    "col": "col",
    "demand": "heat_demand"
}

SOURCE_COLUMNS = {
    "id": "source_id",
    "row": "row",
    "col": "col",
    "supply": "heat_supply"
}

def read_cells(path):
    df = pd.read_excel(path)
    return df.rename(columns={
        CELL_COLUMNS["id"]: "cell_id",
        CELL_COLUMNS["row"]: "row",
        CELL_COLUMNS["col"]: "col",
        CELL_COLUMNS["demand"]: "demand"
    })

def read_sources(path):
    df = pd.read_excel(path)
    return df.rename(columns={
        SOURCE_COLUMNS["id"]: "source_id",
        SOURCE_COLUMNS["row"]: "row",
        SOURCE_COLUMNS["col"]: "col",
        SOURCE_COLUMNS["supply"]: "supply"
    })
