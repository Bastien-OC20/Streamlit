import streamlit as st
from Entity.User import User


class DialogBox():

    @st.dialog("Information")
    def DLgInfoMessage(reason:str = "error", message:str="message error"):
        reason = st.write(f"{reason}")
        st.write(f"{message}")
        if st.button("Ok"):
            st.rerun()

    @st.dialog("Information")
    def DLgInfo(reason:str = "error"):
        reason = st.write(f"{reason}")
        if st.button("Ok"):
            st.rerun()


    @st.dialog("Erreur !")
    def DLgErreurMessage(reason:str = "error", message:str="message error"):
        reason = st.write(f"{reason}")
        st.write(f"{message}")
        if st.button("Ok"):
            st.rerun()

    @st.dialog("Erreur !")
    def DLgErreur(reason:str = "error"):
        reason = st.write(f"{reason}")
        if st.button("Ok"):
            st.rerun()