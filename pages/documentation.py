import streamlit as st

def show_documentation():
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