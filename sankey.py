# sankey.py
import yaml
import plotly.graph_objects as go

def load_config(file_path='config.yaml'):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def create_sankey():
    config = load_config('config.yaml')
    
    # Extract currency, income, and expense categories
    currency = config.get('currency', 'USD')
    income = config['income']
    expenses = config['expenses']
    
    # Calculate total income and total expenses
    total_income = sum(income.values())
    total_expenses = sum(expenses.values())
    leftover_cash = total_income - total_expenses
    
    # Create nodes with "Leftover" as the last node
    nodes = list(income.keys()) + list(expenses.keys()) + ["Leftover"]
    sources, targets, values = [], [], []

    # Map income sources to expenses and track leftover per income source
    for i, (income_source, amount) in enumerate(income.items()):
        income_index = i
        for j, (expense_category, expense_amount) in enumerate(expenses.items(), start=len(income)):
            flow_value = min(amount, expense_amount)
            sources.append(income_index)
            targets.append(j)
            values.append(flow_value)
            amount -= flow_value  # Deduct from income for each expense
            if amount <= 0:
                break  # Stop if income source is exhausted

        # If there is any remaining income for this source, map it to "Leftover"
        if amount > 0:
            sources.append(income_index)
            targets.append(len(nodes) - 1)  # "Leftover" node index
            values.append(amount)

    # Remove the final leftover flow addition to avoid double-counting
    # No additional flow to leftover, as it's handled per-income-source

    # Create the Sankey diagram
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values
        )
    ))

    fig.update_layout(title_text=f"Income and Expense Flow ({currency})", font_size=10)
    fig.show()

if __name__ == "__main__":
    create_sankey()
