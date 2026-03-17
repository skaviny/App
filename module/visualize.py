import matplotlib.pyplot as plt
from module import analysis
import streamlit as st

def plot_sum_marks_line(df):
    sum_marks = analysis.sum_of_marks(df)
    plt.plot(sum_marks.index, sum_marks.sum(axis=1), marker='o', color='teal')
    plt.title("Sum of Marks per Student")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def plot_top_performers_total(df, n=5):
    top_df = analysis.top_performers(df, n)
    plt.bar(top_df['Name'], top_df["Total"], color="skyblue")
    plt.title(f"Top {n} Students - Total Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def plot_hours_vs_sum(df):
    sum_marks = analysis.sum_of_marks(df)
    plt.scatter(df["Hours_Studied"], sum_marks.sum(axis=1), color="purple", s=100, alpha=0.7)
    plt.title("Hours Studied vs Sum of Marks")
    plt.tight_layout()
    st.pyplot(plt)

