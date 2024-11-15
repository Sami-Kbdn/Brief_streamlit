import streamlit as st
import json

with open("question.json") as f: 
    question = json.load(f)

st.header("Formulaire à remplir")

st.write ('Question 1?')

reponse1 = st.checkbox("rep1")
reponse2 = st.checkbox("rep2")
reponse3 = st.checkbox("rep3")


# if reponse1 :
#     st.write("bien")
# elif reponse2 or reponse3 :
#     st.write("non")

#def 