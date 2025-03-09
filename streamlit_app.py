import streamlit as st
import pandas as pd
from utils import process_command

st.title("Generalized AI Query and Summarization App")

question = st.text_input("Ask your question:")
if st.button("Submit"):
    if question:
        try:
            raw_data, summary = process_command(question)
            
            st.subheader("Raw Data")
            if raw_data:
                raw_df = pd.DataFrame(raw_data)
                st.write(raw_df)
            else:
                st.write("No data found.")

            st.subheader("Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a question.")