import streamlit as st
import analysis
import visualize

st.title("Student Performance Dashboard")

df = analysis.load_data()

st.subheader("Sum of Marks per Student")
visualize.plot_sum_marks_line(df)

st.subheader("Top 5 Students - Total Marks")
visualize.plot_top_performers_total(df)

st.subheader("Hours Studied vs Sum of Marks")
visualize.plot_hours_vs_sum(df)

