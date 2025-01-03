# app.py
import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import google.generativeai as genai
from sql import create_student_table, insert_data, read_sql_query

# Load environment variables
load_dotenv()

# Set up Google Gemini API key for AI
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Function to load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])  # Generate response based on input question
    return response.text

# Function to validate and safely execute SQL queriesdef safe_read_sql_query(sql, db="student.db"):
def safe_read_sql_query(sql, db="student.db"):
    if "SELECT" in sql.upper():
        rows = read_sql_query(sql, db)
        # Check if the query is an aggregate function (like AVG, COUNT, etc.)
        if len(rows) == 1 and len(rows[0]) == 1:
            return rows[0][0]  # Return the single value (e.g., average)
        return rows  # Return the full result set if it's not a single value
    else:
        return "Invalid SQL query. Only SELECT queries are allowed."



# Streamlit UI setup
st.set_page_config(page_title="Text-to-SQL Query Generator")
st.header("Gemini App to Retrieve SQL Data")

# Input field for natural language question
question = st.text_input("Ask a question:", key="input")
submit = st.button("Ask The Question")

# Display results when the question is submitted
if submit:
    if question:
        prompt = [
            """
            You are an expert in converting English questions to SQL query!
            The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
            SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
            the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
            \nExample 2 - Tell me all the students studying in Data Science class?, 
            the SQL command will be something like this SELECT * FROM STUDENT 
            where CLASS="Data Science"; 
            also the sql code should not have ``` in beginning or end and sql word in output
            """
        ]

        # Get response from the model (Gemini)
        response = get_gemini_response(question, prompt)
        st.write(f"Generated SQL Query: {response}")

        # Execute SQL query and display results
        try:
            data = safe_read_sql_query(response, "student.db")
            if isinstance(data, list) and data:
                # For a standard result set, show as a DataFrame
                import pandas as pd
                df = pd.DataFrame(data, columns=["ID", "NAME", "CLASS", "SECTION", "MARKS"])
                st.subheader("Query Results:")
                st.dataframe(df)
            elif isinstance(data, (int, float)):  # If the result is a single value (e.g., AVG)
                st.subheader("Query Result:")
                st.write(data)
            else:
                st.warning(data)  # Show warning if no data is returned
        except Exception as e:
            st.error(f"Error executing query: {str(e)}")

# create_student_table()
# insert_data()