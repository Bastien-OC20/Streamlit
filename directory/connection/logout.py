import streamlit as st

def show_logout():
    if st.button("Log out"):

        st.session_state.logged_in = False
        st.session_state.active_page = "login_page"
        st.rerun()

show_logout()