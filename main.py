# THIS IS AN ACCADEMIC TEMPLATE - IT CONTAINS PUBLICLY AVAILABLE INFORMATION / DATA
# THE CONTENT IS THE SOLE PROPERTY AND OUTPUT OF STEFANO CICCARELLI
# EVERYONE IS AUTHORIZED TO COPY / PASTE AND EDIT FOR ACCADEMICAL PURPOSES

from tax_policy_optimization import custom_tax_rate_policy
import streamlit as st

expected_productivity_factors = [0.8, 1.2, 0.6, 0.9, 1.1, 0.7, 1.0, 1.3, 0.5, 0.8]  
# Streamlit app
st.title("Custom Tax Rate Policy")

equality_policy = st.slider("Equality Policy", 0.05, 3.0, 1.0, 0.05)

if st.button("Run Optimization"):
    expected_income, optimal_tax_rates, gini_coeff, gdp_growth, inequality_increase = custom_tax_rate_policy(equality_policy)

    st.write(f"Expected Global Income: {expected_income:.2f}")
    for i, rate in enumerate(optimal_tax_rates):
        st.write(f"Individual {i} (Productivity Factor {expected_productivity_factors[i]:.2f}): Tax rate = {rate:.2f}")

    st.write(f"Gini Coefficient (Optimized Solution): {gini_coeff:.4f}")
    st.write(f"Expected Increase of GDP Growth: {gdp_growth:.2f}%")
    st.write(f"Expected Increase of Inequality: {inequality_increase:.2f}%")
