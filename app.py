import streamlit as st
from src.income import Income, add_income, get_income_data
from src.expense import Expense, add_expense, get_expense_data
import locale
import matplotlib.pyplot as plt

# Set the locale to your system's default (e.g., 'en_US.UTF-8')
locale.setlocale(locale.LC_ALL, '')

st.title("Personal Finance Manager")

st.sidebar.header("Income")
income_amount = st.sidebar.number_input("Amount (Income)", min_value=0.01, key="income_amount")
income_source = st.sidebar.text_input("Source (Income)", key="income_source")

if st.sidebar.button("Add Income"):
    income = Income(amount=income_amount, source=income_source)
    add_income(income)

st.sidebar.header("Expenses")
expense_amount = st.sidebar.number_input("Amount (Expense)", min_value=0.01, key="expense_amount")
expense_category = st.sidebar.text_input("Category (Expense)", key="expense_category")

if st.sidebar.button("Add Expense"):
    expense = Expense(amount=expense_amount, category=expense_category)
    add_expense(expense)

st.header("Income Data")
income_data = get_income_data()
income_table_data = [{"Amount": locale.currency(income.amount, grouping=True), "Source": income.source} for income in income_data]
st.table(income_table_data)

st.header("Expense Data")
expense_data = get_expense_data()
expense_table_data = [{"Amount": locale.currency(expense.amount, grouping=True), "Category": expense.category} for expense in expense_data]
st.table(expense_table_data)

# Visualize Income and Expense as a Line Graph
fig, ax = plt.subplots(figsize=(10, 6))
income_dates = [income.date for income in income_data]
income_amounts = [income.amount for income in income_data]
expense_dates = [expense.date for expense in expense_data]
expense_amounts = [expense.amount for expense in expense_data]

# Plot income and expense as lines on the same graph
ax.plot(income_dates, income_amounts, label="Income", marker='o')
ax.plot(expense_dates, expense_amounts, label="Expense", marker='x')

# Customize the plot
ax.set_xlabel("Date")
ax.set_ylabel("Amount")
ax.set_title("Income vs. Expense Over Time")
ax.legend()
ax.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(fig)
