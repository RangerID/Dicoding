import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set style for seaborn plots
sns.set(style='dark')

# Read the dataset
customers_df = pd.read_csv("customers_dataset.csv")
payments_df = pd.read_csv("order_payments_dataset.csv")

payment_counts = payments_df.groupby(by="customer_state").customer_id.nunique().reset_index()
payment_counts.columns = ['customer_state', 'customer_count']
payment_counts = payments_df.groupby(by="payment_type").order_id.nunique().reset_index()
payment_counts.columns = ['payment_type', 'order_count']

# Create a plot
st.subheader("Negara Bagian Pelanggan")

fig, ax = plt.subplots(figsize=(10, 5))  # Set figure size

sns.barplot(
    x="customer_state",
    y="customer_count",
    data=payment_counts.sort_values(by="customer_count", ascending=False),
    ax=ax
)

# Customize the plot
ax.set_title("Negara bagian dengan pelanggan terbanyak", loc="center", fontsize=20)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Display the plot in Streamlit
st.pyplot(fig)

# Create a plot
st.subheader("Jenis Pembayaran Terbanyak")
fig, ax = plt.subplots(figsize=(10, 5))  # Set figure size

sns.barplot(
    x="payment_type",
    y="order_count",
    data=payment_counts.sort_values(by="order_count", ascending=False),
    ax=ax
)

# Customize the plot
ax.set_title("Jenis Pembayaran", loc="center", fontsize=20)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Display the plot in Streamlit
st.pyplot(fig)