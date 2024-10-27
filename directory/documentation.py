import streamlit as st

def show_documentation():
    st.session_state.active_page = "documentation_page"

    with st.sidebar:
        st.header("Menu")
        st.button("Bouton d'exemple")

    st.title("Documentation")
    st.write("Contenu de la documentation ici.")
# def display():
#     with st.sidebar:
#         st.header("Menu")
#         st.button("Bouton d'exemple")

#     st.title("Documentation")
#     st.write("Contenu de la documentation ici.")

show_documentation()