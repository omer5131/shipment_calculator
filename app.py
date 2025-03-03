import streamlit as st

st.title("Shipment Price Calculator")

# Input fields for the four inputs
total_items_cost = st.number_input("Total Items Cost", value=0.0, step=0.01, format="%.2f")
customs_rate = st.number_input("Custom's Rate", value=1.0, step=0.01, format="%.2f")
tax_rate = st.number_input("Tax Rate (from Israel)", value=1.0, step=0.01, format="%.2f")
total_cost_with_taxes = st.number_input("Total Cost Include All Taxes", value=0.0, step=0.01, format="%.2f")

# Button to trigger the calculation
if st.button("Calculate Shipment Price"):
    # Validate inputs: customs_rate and tax_rate must not be zero.
    if customs_rate == 0 or tax_rate == 0:
        st.error("Custom's Rate and Tax Rate must not be zero.")
    else:
        # Calculate shipment price using the formula:
        # Shipment Price = ((Total Cost Include All Taxes / Custom's Rate) - Total Items Cost) / Tax Rate
        shipment_price = ((total_cost_with_taxes / customs_rate) - total_items_cost) / tax_rate
        shipment_price = round(shipment_price, 2)  # round to two decimals
        
        st.success(f"Shipment Price: {shipment_price}")
