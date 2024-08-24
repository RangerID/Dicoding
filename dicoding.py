'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

payments_df = pd.read_csv("order_payments_dataset.csv")
payments_df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False)

sns.barplot(
        y="order_id", 
        x="payment_type",
        data=payments_df.sort_values(by="order_id", ascending=False)
    )
ax.set_title("Jenis Pembayaran", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
plt.figure(figsize=(10, 5))
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set style for seaborn plots
sns.set(style='dark')

# Read the dataset
payments_df = pd.read_csv("order_payments_dataset.csv")

# Calculate the number of unique orders per payment type
payment_counts = payments_df.groupby(by="payment_type").order_id.nunique().reset_index()
payment_counts.columns = ['payment_type', 'order_count']

# Create a plot
fig, ax = plt.subplots(figsize=(10, 5))  # Set figure size

sns.barplot(
    x="payment_type",
    y="order_count",
    data=payment_counts.sort_values(by="order_count", ascending=False),
    ax=ax
)

# Customize the plot
ax.set_title("Jenis Pembayaran", loc="center", fontsize=20)
ax.set_ylabel("Jumlah Order")
ax.set_xlabel("Tipe Pembayaran")
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Display the plot in Streamlit
st.pyplot(fig)