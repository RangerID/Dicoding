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
        data=payments_df.sort_values(by="order_id", ascending=False),
        ax=ax        
    )
ax.set_title("Jenis Pembayaran", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
plt.figure(figsize=(10, 5))