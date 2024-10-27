import streamlit as st
from services.Verifications import VerificationsService
# from services.connectionService import ConnectService
from Transiant.transiant_connection import transiant_connection
from services.connectionService import ConnectService
from directory.dialogBox.DialogBox import DialogBox
from Transiant.UserConnected import UserConnected as UserConnected

def show_login():
    st.session_state.active_page = "login_page"

    # myDialogBox = DialogBox()
    st.session_state.active_page = "login_page"
    __myConectionService = ConnectService()

    myEmail = ""
    myPassword = ""

    myEmail = st.text_input("courriel", placeholder="Votre courriel", key="connect_email")
    myPassword = st.text_input("mot-de-passe", placeholder="Votre mot-de-passe", key="connect_password", type="password")

    if st.button("Log in"):

        myTrs_connection = transiant_connection(myEmail, myPassword)

        try:
            user = __myConectionService.verifyConnect(myTrs_connection)
            if user is None:
                reason="Connexion impossible"
                msg = "Vos identifiants ne sont pas reconnus"
                # DialogError("Connexion impossible")
                # DialogBox.DLgInfoMessage(reason,msg)
                dg = DialogBox()
                dg.DLgInfoMessage(reason,msg)
                del dg
                return
            # myUserConnected = UserConnected(user.email,user.UserId, user.nom)
            # print(myUserConnected.__dir__)
            user.password = ""
            st.session_state.logged_in = True
            st.session_state.user_email = user.email
            st.session_state.user_id = user.UserId
            st.session_state.user_role = user.role
            st.session_state.user_name = user.nom

            # print("st.session_state.user_role")
            # print(st.session_state.user_role)

            st.rerun()

        except Exception as e:
            reason = "Erreur de connexion !"
            st.write("erreur de connexion !")
            # DialogBox.DLgInfo(reason)
            dg = DialogBox()
            dg.DLgInfo(reason)
            del dg

show_login()