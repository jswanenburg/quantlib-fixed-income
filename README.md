# GB QuantLib CodeHub

An introduction to the [QuantLib](https://www.quantlib.org/) Python library for fixed income quants, focused on pricing fixed income instruments and computing risk measures.

## Contents

The examples are structured as Jupyter notebooks in `src/Examples/`, numbered in suggested reading order:

| Notebook | Topic |
|---|---|
| [1. Get started](src/Examples/1.%20Get%20started.ipynb) | QuantLib basics: installation, dates, calendars, business day conventions, exploring market data |
| [2. ESTR](src/Examples/2.%20ESTR.ipynb) | The ESTR overnight rate, QuantLib index objects, historical fixings, ESTR swap rates |
| [3. ESTR swap term structure](src/Examples/3.%20ESTR%20swap%20term%20structure.ipynb) | Bootstrapping the ESTR zero rate curve from market swap rates |
| [4. Bond pricing](src/Examples/4.%20Bond%20pricing.ipynb) | Pricing fixed income bonds in QuantLib |
| [5. Swap pricing](src/Examples/5.%20Swap%20pricing.ipynb) | Pricing interest rate swaps |
| [6. Euribor 6M](src/Examples/6.%20Euribor%206M.ipynb) | The 6-month EURIBOR index and curve construction |
| [6. Swap dv01](src/Examples/6.%20Swap%20dv01.ipynb) | Swap DV01: zero and par DV01, impact of shifting the fixing |
| [7. Swap krdv01](src/Examples/7.%20Swap%20krdv01.ipynb) | Key rate DV01: linear mapping, impact of shifting the fixing |
| [8. Swap convexity](src/Examples/8.%20Swap%20convexity.ipynb) | Swap convexity |

## Getting Started

### Prerequisites

- Python 3.8+
- [Visual Studio Code](https://code.visualstudio.com/) with the Jupyter extension (recommended)

### Installation

From the repo root:

```bash
# Create and activate the virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

Then open any notebook in `src/Examples/` and select the `.venv` Python kernel.

## Market Data

Sample market data snapshots are stored in `data/`. Filenames include the as-of date in `YYYYMMDD` format:

- `6M EURIBOR 20260820.xlsx` — 6-month EURIBOR swap curve as of 20 Aug 2026
- `ESTR 20260820.xlsx` — ESTR OIS swap curve as of 20 Aug 2026
- `ESTR swap 20260803.xlsx` — ESTR swap rates as of 3 Aug 2026

## Key Topics

- **QuantLib fundamentals** — dates, calendars, business day conventions, day count conventions
- **Index objects** — ESTR/EONIA index, historical fixings, the IndexManager
- **Yield curve construction** — bootstrapping ESTR OIS and EURIBOR swap curves
- **Fixed income pricing** — bonds, interest rate swaps, futures
- **Risk measures** — DV01/delta and convexity calculations
