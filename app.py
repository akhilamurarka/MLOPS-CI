import streamlit as st

#UI
st.write("Power Calculator")
st.write("Provide a number to calculate its square, cube or fifth power")

n=st.number_input("Enter an integer",value=1,step=1)

square=n**2
cube=n**3
fifth=n**5

st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth}")