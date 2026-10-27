# Setup module

# Load packages
import QuantLib as ql
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from pathlib import Path

# Load and data
data_directory = Path.cwd().parents[1] / "data"
euribor_file = data_directory / "6M EURIBOR 20260820.xlsx"
ESTR_file    = data_directory / "ESTR 20260820.xlsx"
ESTR_data = pd.read_excel(ESTR_file, 
                          sheet_name="Data",
                          skiprows=0)

# Create an index object 
ESTR_curve_handle = ql.RelinkableYieldTermStructureHandle()     # empty curve handle, necessary to create the index object
ESTR_index        = ql.Eonia(ESTR_curve_handle)                 # index object, contains settings for the floating leg payments of ESTR swaps

# Create an empty list of quotes and vector of helpers
ESTR_quotes  = []
ESTR_helpers = ql.RateHelperVector()

# Current ESTR fixing:
current_ESTR_fixing = 0.0218                                            # pass the fixing as a numeric, not as percentage
current_ESTR_fixing_quote = ql.SimpleQuote(current_ESTR_fixing)         # wrap the quote in a simple quote object
current_ESTR_fixing_handle = ql.QuoteHandle(current_ESTR_fixing_quote)  # wrap the quote in a handle

ESTR_quotes.append(current_ESTR_fixing_quote)                           # add fixing to the list of quotes

# Create the deposit rate helper
deposit_helper = ql.DepositRateHelper(
    current_ESTR_fixing_handle,                                 # the quote handle pointing to our ESTR fixing
    ESTR_index                                                  # pass the index object such that all variables are passed based on the index settings
)

# Add the helper to the ESTR helper vector
ESTR_helpers.append(deposit_helper)

# Create all ESTR helpers
for idx,row in ESTR_data.iterrows():
    # Settlement days
    settlementDays = 2

    # Tenor
    # Extract the tenor from the dataset. The tenor is given as string and needs some adjustment to be converted to a quantlib period
    [tenor_numeric, period] = row['Term'].split()
    tenor_numeric = int(tenor_numeric)
    if period == "WK":
        tenor = ql.Period(tenor_numeric, ql.Weeks)
    elif period == "MO": 
        tenor = ql.Period(tenor_numeric, ql.Months)
    elif period == "YR":
        tenor = ql.Period(tenor_numeric, ql.Years)
    else:
        raise ValueError(f"{row['Term']} not specified")

    # Quote handle
    quote = float(row['Market Rate']) / 100
    quote_object = ql.SimpleQuote(quote)
    quote_handle = ql.QuoteHandle(quote_object)

    # Create a new swap helper:
    swap_helper = ql.OISRateHelper(
        settlementDays,                                             # the number of settlement days for your swap instrument
        tenor,                                                      # the tenor, i.e. the time to maturity
        quote_handle,                                               # the quote wrapped into a quote handle object
        ESTR_index                                                  # the ESTR index object containing all other parameters for ESTR swaps
    )
    
    # Add the helper to the ESTR helper vector
    ESTR_helpers.append(swap_helper)

# Bootstrap the ESTR curve

# Set the curvedate to our current evaluation date
curveDate = ql.Date(20,8,2026)

# Apply the PiecewiseLogCubicDiscount() function on our set of helpers
ESTR_curve = ql.PiecewiseLogCubicDiscount(
    curveDate,                                                      # the date of the observed market rates
    ESTR_helpers,                                                   # the vector containing our ESTR helpers and the deposit helper
    ql.Actual365Fixed()                                             # the convention for the curve
)

# Enable extrapolation to obtain zero rates outside the maturity range of our helpers
ESTR_curve.enableExtrapolation()

# Link the ESTR curve handle to the ESTR curve IMPORTANT
ESTR_curve_handle.linkTo(ESTR_curve)

print(f"ESTR curve constructed and ready to use. Setup complete")
