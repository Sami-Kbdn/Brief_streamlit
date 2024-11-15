import streamlit as st
import json
from pydantic import BaseModel, field_validator


class Question(BaseModel):
    question : str
    reponses : str
    indice : str
    bonne_reponse : str

    

    @field_validator("reponses")
    def validation(cls, v):
        ma_liste = v.split("\n")
        print(ma_liste)
        if len(ma_liste) < 2:
            raise ValueError("Il doit y avoir au moins deux réponses possibles.")
        else : 
            st.text("Le questionnaire a bien été enregistré !")

        return v

def read():
    try:
        with open ("question.json", "r") as fichier:
            return json.load(fichier)
             
    except:
        with open ("question.json", "w") as fichier :
            json.dump([], fichier)
            return []
        




def write(question, reponses, indice, bonne_reponse):

    liste_json = read()

    ma_question = Question(
        question = question,
        reponses = reponses,
        indice = indice,
        bonne_reponse = bonne_reponse,

    )

    # dico_json = {
    #     "question": question,
    #     "reponses": reponses,
    #     "indice": indice,
    #     "bonne_reponse": bonne_reponse}
    

    liste_json.append(ma_question)

    with open ("question.json", "w") as fichier :
        json.dump([question.__dict__ for question in liste_json], fichier, indent=4)

def control(question, reponses, indice, bonne_reponse):
    
    if st.button("Envoyer le formulaire"):
        if all(type(i) is str and len(i) > 0 for i in [question, reponses, indice, bonne_reponse]):
                    
                dico_json = {
                    "question": question,
                    "reponses": reponses,
                    "indice": indice,
                    "bonne_reponse": bonne_reponse}
                
                liste_questions.append(dico_json)
                # st.text("Le questionnaire a bien été enregistré !")
                write(question, reponses, indice, bonne_reponse)

        else :
             st.error("Remplissez bien chacune des cases.")


def display():
    if choix == "Configurer le quiz":
          st.header("Formulaire à remplir")
          question = st.text_input("Saisissez votre question :")
          reponses = st.text_area("Saisissez les 3 réponses possibles (ligne après ligne) :")
          indice = st.text_input("Saisissez un indice :")
          bonne_reponse = st.text_input("Saisissez la bonne réponse :")

          control(question, reponses, indice, bonne_reponse)
          
    elif choix == "Jouer au quiz":

        st.header("Questionnaire")

        if st.session_state['question'] == len(liste_questions):
            st.title("Quiz terminé !")
            st.write(f"Votre score final : {st.session_state.score} / {len(liste_questions)}")


        else:

            index_question = st.session_state["question"]
            question_courrante = liste_questions[index_question]

            
            st.write(question_courrante["question"])
            
            choice = question_courrante["reponses"].split("\n")
            reponse1 = st.radio("Choisissez une réponse :", choice)
            
            indice1 = st.checkbox("Voir l'indice")
            if indice1:
                st.write(question_courrante["indice"])
            

            if st.button("Valider la réponse"):
                if reponse1 == question_courrante["bonne_reponse"]:
                    st.success("Bonne réponse")
                    st.session_state['score'] += 1
                else:
                    st.error("Mauvaise réponse")

            if st.button("Passer à la question suivante"):
                st.session_state["question"] += 1 
                st.rerun()
        

liste_questions = read() 
st.sidebar.title("Quiz App")
choix = st.sidebar.radio("Choisissez une page", ["Configurer le quiz", "Jouer au quiz"])
if "question" not in st.session_state :
    st.session_state["question"] = 0

if "score" not in st.session_state :
    st.session_state['score'] = 0



display()
