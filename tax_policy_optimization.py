# THIS IS AN ACCADEMIC TEMPLATE - IT CONTAINS PUBLICLY AVAILABLE INFORMATION / DATA
# THE CONTENT IS THE SOLE PROPERTY AND OUTPUT OF STEFANO CICCARELLI
# EVERYONE IS AUTHORIZED TO COPY / PASTE AND EDIT FOR ACCADEMICAL PURPOSES

import pulp

# This imports the PuLP library, which is a linear programming modeler written in Python.
# PuLP allows us to define and solve linear optimization problems.
def custom_tax_rate_policy(equality_policy):

    # Create a new problem instance
    prob = pulp.LpProblem("Tax_Rate_Policy", pulp.LpMaximize)

    # This line creates a new linear programming problem instance called "Tax_Rate_Policy".
    # The "pulp.LpMaximize" argument specifies that we want to maximize the objective function.

    # Define parameters (Fixed Information from your Business / Real Environment)
    num_individuals = 10
    individual_incomes = [10, 12, 8, 15, 9, 11, 14, 7, 13, 10]  # Million Euros
    public_expenses = 35  # Million Euros
    current_tax_rate = 0.35  # 35% - We assume al Pubblic Expenses are immeditaly financed by Private Income
    expected_productivity_factors = [0.8, 1.2, 0.6, 0.9, 1.1, 0.7, 1.0, 1.3, 0.5, 0.8]  
    # Factors representing expected long term productivity of 1 EUR given to an Individual i
    # Those can be estimated by more sophisticated Profilation Model / Methodologies based on Academical Background and Motivations

    # This section defines the parameters or fixed information that we have about our business or real environment.
    # Parameters are values that are known and cannot be changed by the optimization process.
    # In this case, we have information about the number of individuals, their incomes, public expenses, the current tax rate, and expected productivity factors.

    # Define decision variables (Levers you Can Change / Influence via a Policy)
    tax_rates = [pulp.LpVariable(f"t{i}", lowBound=0.1, upBound=0.5) for i in range(num_individuals)]

    # This line defines the decision variables in our optimization problem.
    # Decision variables are the values that the optimization process can change or optimize to achieve the desired objective.
    # In this case, we have a list of decision variables called "tax_rates", representing the tax rate for each individual.
    # The tax rates are bounded between 0.1 and 0.5 (10% and 50%). They can't be lower or higher than those boundaries.

    # Define the objective function (Your Goal: It can be Maximized or Minimized)
    prob += sum(individual_incomes[i] * (1 - tax_rates[i]) * expected_productivity_factors[i] for i in range(num_individuals))

    # This line defines the objective function that we want to maximize in our optimization problem.
    # The objective function represents our goal or the quantity that we want to optimize.
    # In this case, we want to maximize the sum of the expected incomes for all individuals, considering their tax rates and productivity factors.
    # The expected income for each individual is calculated as their income multiplied by (1 - tax rate) and their productivity factor.

    # Define constraints (Limits or Physical Boundaries of our Problem)
    # Ensure public services are covered
    prob += sum(individual_incomes[i] * tax_rates[i] for i in range(num_individuals)) >= public_expenses

    # This line defines a constraint in our optimization problem.
    # Constraints represent the limits or physical boundaries that our solution must satisfy.
    # In this case, we ensure that the sum of the tax revenues from all individuals is greater than or equal to the public expenses.
    # This constraint ensures that the government can cover the cost of public services.

    # Cap the expected income based on the average productivity factor
    avg_productivity_factor = sum(expected_productivity_factors) / len(expected_productivity_factors)
    total_income = sum(individual_incomes)

    # In this model we Assume that no Individual can control more than a given % of the Total Economy
    expected_income_cap = total_income * avg_productivity_factor * (equality_policy / num_individuals)

    for i in range(num_individuals):
        prob += (individual_incomes[i] * (1 - tax_rates[i]) * expected_productivity_factors[i]) <= expected_income_cap

    # This section defines another constraint in our optimization problem.
    # First, we calculate the average productivity factor by taking the sum of all productivity factors and dividing by the number of individuals.
    # We also calculate the total income by summing the incomes of all individuals.
    # Then, we define the expected income cap based on the equality policy and the assumption that no individual can control more than 1/num_individuals % of the total economy.
    # The expected income cap is calculated as the total income multiplied by the average productivity factor and the equality policy factor.
    # Finally, we add a constraint for each individual, ensuring that their expected income does not exceed the expected income cap.

    # Solve the problem
    prob.solve()

    # This line solves the optimization problem using the PuLP solver.
    # The solver finds the optimal values for the decision variables (tax rates) that maximize the objective function while satisfying all the constraints.

    # Print the solution
    print(f"Objective value (Expected Global Income): {pulp.value(prob.objective):.2f}")
    for i in range(num_individuals):
        print(f"Individual {i} (Productivity Factor {expected_productivity_factors[i]:.2f}): Tax rate = {tax_rates[i].varValue:.2f}, Expected Income = {individual_incomes[i] * (1 - tax_rates[i].varValue) * expected_productivity_factors[i]:.2f}")

    print(f"Total Expected Income with Custom Tax Rate: {pulp.value(prob.objective):.2f}")
    # This section prints the solution of the optimization problem.
    # First, it prints the objective value, which is the expected global income calculated based on the optimal tax rates.
    # Then, it prints the optimal tax rate and expected income for each individual, considering their productivity factors.

    # Calculate Gini coefficient for the optimized solution
    optimized_expected_incomes = [individual_incomes[i] * (1 - tax_rates[i].varValue) * expected_productivity_factors[i] for i in range(num_individuals)]
    gini_coefficient_optimized = sum(abs(optimized_expected_incomes[i] - optimized_expected_incomes[j]) for i in range(num_individuals) for j in range(num_individuals)) / (2 * num_individuals * sum(optimized_expected_incomes))
    print(f"Gini Coefficient (Optimized Solution): {gini_coefficient_optimized:.4f}")

    expected_incomes = [individual_incomes[i] * (1 - current_tax_rate) * expected_productivity_factors[i] for i in range(num_individuals)]
    total_expected_income_flat_tax = sum(expected_incomes)
    print(f"Total Expected Income with 35% Flat Tax Rate: {total_expected_income_flat_tax:.2f}")

    # This section calculates the total expected income if a flat tax rate of 35% is applied to all individuals.
    # It first creates a list of expected incomes for each individual with a 35% tax rate and their respective productivity factors.
    # Then, it calculates the total expected income by summing up the individual expected incomes.
    # Finally, it prints the total expected income with the 35% flat tax rate.

    # Calculate Gini coefficient for the 35% flat tax rate scenario
    flat_tax_expected_incomes = [individual_incomes[i] * (1 - current_tax_rate) * expected_productivity_factors[i] for i in range(num_individuals)]
    gini_coefficient_flat_tax = sum(abs(flat_tax_expected_incomes[i] - flat_tax_expected_incomes[j]) for i in range(num_individuals) for j in range(num_individuals)) / (2 * num_individuals * sum(flat_tax_expected_incomes))
    print(f"Gini Coefficient (35% Flat Tax Rate): {gini_coefficient_flat_tax:.4f}")


    increase_expected_income = (pulp.value(prob.objective) / total_expected_income_flat_tax - 1) * 100
    print(f"Expected Increase of GDP with this Policy: {increase_expected_income:.2f}%")

    # This section calculates the expected increase in GDP growth compared to the flat tax rate scenario.
    # It takes the ratio of the objective value (expected global income from the optimization solution) and the total expected income with the flat tax rate.
    # It then subtracts 1 and multiplies by 100 to get the percentage increase.
    # Finally, it prints the expected increase in GDP growth with the optimized tax policy compared to the flat tax rate scenario.

    # The Gini coefficient is a measure of income inequality that ranges from 0 (perfect equality) to 1 (perfect inequality)
    increase_gini = (gini_coefficient_optimized / gini_coefficient_flat_tax - 1) * 100
    print(f"Expected Increase of Inequality with this Policy: {increase_gini:.2f}%")

    # Return all the necessary parameters
    return (
        pulp.value(prob.objective),
        [tax_rates[i].varValue for i in range(num_individuals)],
        gini_coefficient_optimized,
        increase_expected_income,
        increase_gini
    )


EQUALITY_POLICY = 1  
# Higher Than 1 Will Increase Private Total GDP Growth by Increase Inequality
# Lower than 1 will Increase Equality but Lower Private Total GDP

# This variable represents the equality policy that we want to enforce in our optimization problem.
# A value of 1 means that we aim for perfect equality, where no individual can control more than 1/num_individuals % of the total economy.
# Values higher than 1 will allow for more inequality, increasing private total GDP growth but at the cost of increased inequality.
# Values lower than 1 will prioritize equality over GDP growth, leading to a more equal distribution of income but potentially lower total GDP growth.
# Value lower than 1 will also imply more Government Control over the Economy that if excessive can push the Total GDP to 0
expected_income, optimal_tax_rates, gini_coeff, gdp_growth, inequality_increase = custom_tax_rate_policy(EQUALITY_POLICY)