import streamlit as st
from directory.dialogBox.DialogBox import DialogBox



def show_logout():

    if st.button("Log out"):
        reason = "Vous allé être déconnecté"
        DialogBox.DLgInfo(reason)
        st.session_state.logged_in = False
        st.session_state.active_page = "login_page"

show_logout()