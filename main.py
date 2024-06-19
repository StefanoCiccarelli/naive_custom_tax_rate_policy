# THIS IS AN ACCADEMIC TEMPLATE - IT CONTAINS PUBLICLY AVAILABLE INFORMATION / DATA
# THE CONTENT IS THE SOLE PROPERTY AND OUTPUT OF STEFANO CICCARELLI
# EVERYONE IS AUTHORIZED TO COPY / PASTE AND EDIT FOR ACCADEMICAL PURPOSES

from tax_policy_optimization import custom_tax_rate_policy
import streamlit as st

expected_productivity_factors = [0.8, 1.2, 0.6, 0.9, 1.1, 0.7, 1.0, 1.3, 0.5, 0.8]  

# Streamlit app
st.title("Custom Tax Rate Policy Optimization")

st.write("This app allows you to explore the trade-offs between economic growth and income equality by optimizing tax rates for individuals based on their expected productivity factors. You can adjust the 'Equality Policy' slider to prioritize economic growth or income equality, and the app will provide the optimal tax rates, expected global income, Gini coefficient, and the expected changes in GDP growth and inequality compared to a flat tax rate scenario.")

equality_policy = st.slider("Equality Policy", 0.05, 3.0, 1.0, 0.05, help="A value of 1 represents perfect equality, where no individual can control more than 1/num_individuals % of the total economy. Values higher than 1 allow for more inequality, potentially increasing GDP growth but at the cost of increased inequality. Values lower than 1 prioritize equality over GDP growth, leading to a more equal distribution of income but potentially lower total GDP growth.")

if st.button("Run Optimization"):
    expected_income, optimal_tax_rates, gini_coeff, gdp_growth, inequality_increase = custom_tax_rate_policy(equality_policy)

    st.subheader("Optimization Results")
    st.write(f"**Expected Global Income**: {expected_income:.2f}")
    st.write("This is the expected total income of all individuals based on the optimized tax rates and their respective productivity factors.")

    for i, rate in enumerate(optimal_tax_rates):
        st.write(f"**Individual {i}** (Productivity Factor {expected_productivity_factors[i]:.2f}): Tax rate = {rate:.2f}")
    st.write("The optimized tax rates for each individual, considering their expected productivity factors.")

    st.write(f"**Gini Coefficient (Optimized Solution)**: {gini_coeff:.4f}")
    st.write("The Gini coefficient is a measure of income inequality, ranging from 0 (perfect equality) to 1 (perfect inequality). A higher value indicates greater income inequality.")

    st.write(f"**Expected Increase of GDP Growth**: {gdp_growth:.2f}%")
    st.write("The expected increase in GDP growth compared to a flat tax rate scenario of 35%.")

    st.write(f"**Expected Increase of Inequality**: {inequality_increase:.2f}%")
    st.write("The expected increase in income inequality compared to a flat tax rate scenario of 35%.")

    st.write("You can adjust the 'Equality Policy' slider to explore different scenarios and observe the trade-offs between economic growth and income equality.")
