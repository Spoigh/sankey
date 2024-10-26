# Income and Expense Sankey Diagram

This project visualizes income and expenses as a **Sankey diagram** using **Python** and **Plotly**. It takes a configurable YAML file as input, allowing you to specify income sources, expenses, and the currency used. The diagram displays the flow of funds from income sources to expenses, with any remaining cash displayed as "Leftover."

## Features
- Visualizes income and expenses in a Sankey diagram.
- Configurable YAML file for easy customization.
- Shows leftover cash from income after expenses.

## Prerequisites

- **Python** 3.8 or higher
- **Poetry** for dependency management (recommended)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/income-expense-sankey.git
   cd income-expense-sankey
   ```

2. **Install dependencies using Poetry**

    If you don’t have Poetry installed, you can install it by following Poetry's installation guide.

    ```bash
    poetry install
    ```

## Configuration

    The project uses a YAML configuration file (config.yaml) to specify income, expenses, and currency. Here’s an example config.yaml file format:

    ```yaml
    currency: "CZE"  # Specify the currency symbol or code here

    income:
    Salary: 3000
    Freelance: 500

    expenses:
    Rent: 1200
    Groceries: 400
    Utilities: 200
    Savings: 800
    Entertainment: 300
    ```

## Usage

    ```bash
    poetry run sankey
    ```



