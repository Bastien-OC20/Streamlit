import streamlit as st
from services.Verifications import VerificationsService
from services.connectionService import ConnectService
from Transiant.transiant_connection import trs_connection
from services.connectionService import ConnectService
from directory.dialogBox.DialogBox import DialogBox

def show_login():

    # myDialogBox = DialogBox()
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
                reason="Connexion impossible"
                msg = "Vos identifiants ne sont pas reconnus"
                # DialogError("Connexion impossible")
                DialogBox.DLgInfoMessage(reason,msg)
                return
            
            st.session_state.logged_in = True
            st.rerun()

        except Exception as e:
            reason = "Erreur de connexion !"
            st.write("erreur de connexion !")
            DialogBox.DLgInfo(reason)

show_login()