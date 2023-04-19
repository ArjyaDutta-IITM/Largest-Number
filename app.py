import streamlit as st

def app():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below and click on the 'Find Largest' button to get the largest number among them.")
    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")
    if st.button("Find Largest"):
        st.write("The largest number is:", max(a,max(b,c)))

if _name_ == "_main_":
    app()
