# import streamlit as st
# from dataclasses import dataclass

# @dataclass
# class sessionService():

#     # def __init__(self) -> None:
#     #     pass

#     # sessionState = st.session_state

#     def __init__(self, logged_in:bool=False):
#         st.session_state.logged_in = logged_in
    

#     def testSessionLoggedIn(self)->bool:
#         if "logged_in" not in st.session_state:
#             # self.__logged_in = False
#             st.session_state.logged_in = False
#             return False
#         return True
    
#     @property
#     def logged_in(self):
#         # self.sessionState.logged_in = True
#         return st.session_state.logged_in
#         # return self.__logged_in
    
#     @logged_in.setter
#     def logged_in(self, value: bool):
#         if not isinstance(value, bool):
#             raise TypeError(f"logged n'est pas du bon type")
#         st.session_state.logged_in = value
    
#     @property
#     def sessionState(self):
#         return return st.session_state
        
