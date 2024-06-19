# Custom Tax Rate Policy Optimization

This repository contains a Python implementation of a custom tax rate policy optimization model using linear programming. The objective is to find the optimal tax rates for individuals based on their expected productivity factors, while balancing economic growth and income equality.

## Overview

The tax policy optimization model aims to maximize the expected global income by adjusting individual tax rates. The model takes into account various parameters such as individual incomes, expected productivity factors, public expenses, and an equality policy factor.

By incorporating an equality policy factor, the model allows for exploring the trade-offs between economic growth and income equality. A higher equality policy value promotes greater income equality but may result in lower overall economic growth, while a lower value prioritizes economic growth at the cost of increased inequality.

## Usage

The optimization model is implemented in the `tax_policy_optimization.py` file. To run the optimization, you can use the provided Streamlit app:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Start the Streamlit app by running `streamlit run main.py`.
3. Adjust the "Equality Policy" slider to explore different scenarios.
4. Click the "Run Optimization" button to obtain the optimized tax rates, expected global income, Gini coefficient, and the expected changes in GDP growth and inequality.

## Files

- `main.py`: The Streamlit app for running the tax policy optimization.
- `tax_policy_optimization.py`: The Python module containing the implementation of the custom tax rate policy optimization model.
- `requirements.txt`: The list of required Python dependencies.
- `Knowledge and Reasoning Formula.pdf`: A PDF document explaining the knowledge and reasoning pseudo-formula for a Large scale potential version of this Example.
- `ObjectiveFunction Formula.pdf`: A PDF document detailing the objective function pseudo-formula for a Large scale potential version of this Example.
- `Business Intelligence Luiss Presentation.pptx`: A PowerPoint presentation providing an overview of a Business Intelligence Application for MacroEconomics Policy.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was developed as part of an academic exercise by Stefano Ciccarelli for Luiss Guido Carli University, Rome, Italy.
