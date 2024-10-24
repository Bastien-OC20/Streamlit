import streamlit as st
import dataclasses as dataclass

from services.Verifications import VerificationsService
from Entity.Roles import Roles

import re



def show_register():

    if st.session_state.logged_in:
        profilVue, membres = st.tabs(["Profil", "Membres"])
    # else:
        # createVue, profilVue = st.tabs(["Création", "Profil"])
    if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
    __verificationService = VerificationsService()
    print(st.session_state)
    if not st.session_state.logged_in:

        # with createVue:
        st.header("Enregistrement d'un ouvel utilisateur")
        col1, col2 = st.columns(2)

        with col1:
            email = st.text_input("Veuillez entre votre mail :", key="ask_email")
            password = st.text_input("Veuillez nous donner votre mot de passe : ", key="ask_password")
        with col2:
            name = st.text_input("Veuillez entrer le nom : ", key="ask_name")
            st.write()
            postalCode = st.text_input("Veuillez entrer le code postal : ", key="ask_postalCode")
            age = st.text_input("Veuillez entrer l'age : ", key="ask_age")
            size = st.text_input("Veuillez entrer la taille : ", key="ask_size")
            weight = st.text_input("Veuillez entrer le poids sans virgule : ", key="ask_weight")

        # bt_registre =

        def checkData():
            if not __verificationService.IsEmail(email):
                st.write("Veuillez saisir un courriel valide.")            
            if not __verificationService.IsName(name):
                st.write("Veuillez saisir un nom valide.")
            if not __verificationService.IsCodePostal(postalCode):
                st.write("Veuillez saisir un code postal valide.")
            if not __verificationService.IsAge(age):
                st.write("Veuillez saisir un age valide.")
            if not __verificationService.IsSize(size):
                st.write("Veuillez saisir une taille valide de type: 1.5, 2, 1.88")
            if not __verificationService.IsWeight(weight):
                st.write("Veuillez saisir une taille valide de type: 64, 42, 135")
        
        if  st.button("enregistrer"):
            checkData()
    else:
        with profilVue:
            st.header("Profil utilisateur") 
            
        with membres:
            st.header("Liste des membres") 

show_register()