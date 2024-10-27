import streamlit as st
from directory.dialogBox.DialogBox import DialogBox



def show_logout():
   st.session_state.active_page = "logout_page"

   if st.button("Log out"):
      reason = "Vous allé être déconnecté"
      DialogBox.DLgInfo(reason)
      st.session_state.logged_in = False
      
      if "user_UserId" in st.session_state:
         del st.session_state.user_UserId

      if "user_email" in st.session_state:
         del st.session_state.user_email
         
      if "user_role" in st.session_state:
         del st.session_state.user_role

      if "user_name" in st.session_state:
         del st.session_state.user_name


      st.session_state.active_page = "login_page"

show_logout()