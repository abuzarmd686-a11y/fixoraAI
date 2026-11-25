import streamlit as st
import ast

# Page settings
st.set_page_config(
    page_title="Fixora AI",
    page_icon="🤖",
    layout="centered"
)

# Application heading
st.title("🤖 Fixora AI")
st.subheader("Your Intelligent Python Debugging Assistant")

st.write(
    "Find Python syntax errors and understand "
    "what went wrong with your code."
)

st.divider()

# Code input
code = st.text_area(
    "Paste your Python code",
    height=220,
    placeholder='print("Hello World"'
)

# Diagnose button
if st.button("🔍 Diagnose Code", use_container_width=True):

    if not code.strip():
        st.warning("Please paste your Python code first.")

    else:
        try:
            ast.parse(code)

            st.success("No syntax errors detected!")

            st.info(
                "Your code passed the syntax check. "
                "Runtime errors may still exist."
            )

        except SyntaxError as error:

            st.error("Python syntax error detected!")

            st.write("**Problem:**", error.msg)
            st.write("**Line:**", error.lineno)

            st.write(
                "**Suggestion:** Check for missing "
                "brackets, quotation marks or colons."
            )

st.divider()

st.caption("Fixora AI © 2026 | Built with Python")
