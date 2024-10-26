import streamlit as st
from services.Verifications import VerificationsService
from services.connectionService import ConnectService
from Transiant.transiant_connection import trs_connection
from services.connectionService import ConnectService

@st.dialog("Error")
def DialogError(error_message):
    st.write(f"App error")
    st.write(f"reason: {error_message}")
    if st.button("Ok"):
        st.rerun()


def show_login():

    st.session_state.active_page = "login_page"
    __myConectionService = ConnectService()

    myEmail = ""
    myPassword = ""

    myEmail = st.text_input("courriel", placeholder="Votre courriel", key="connect_email")
    myPassword = st.text_input("mot-de-passe", placeholder="Votre mot-de-passe", key="connect_password", type="password")

    if st.button("Log in"):

        myTrs_connection = trs_connection(myEmail, myPassword)

        try:
            repone = __myConectionService.verifyConnect(myTrs_connection)
            if not repone:
                DialogError("Connexion impossible")
                return
            
            st.session_state.logged_in = True
            st.rerun()

        except Exception as e:
            st.write("erreur de connexion !")
            print("erreur de connexion :[ ")
            DialogError(e)

show_login()