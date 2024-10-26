import streamlit as st



@st.dialog("Error")
def DialogError(error_message):
    print("dialog")
    st.write(f"App error")
    st.write(f"reason: {error_message}")
    # reason = st.text_input("Because...")
    if st.button("Ok"):
        # st.session_state.vote = {"item": item, "reason": error_message}
        st.rerun()
        # pass