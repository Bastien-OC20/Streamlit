import os 
import logging
import streamlit as st
import pages as pg
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
# from streamlit_navigation_bar import st_navbar 

# Configuration de la page
st.set_page_config(page_title="Fonction affine", initial_sidebar_state="expanded", page_icon="📊")

# Ajouter un logo
logo_path = "img/logo.png" 
st.image(logo_path, width=450)

# st.markdown(
#     f"""
#     <div style="display: flex; justify-content: center;">
#     </div>
#     """, unsafe_allow_html=True
# )
################################################################# login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
################################################################# page

# icone : https://mui.com/material-ui/material-icons/
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

documentation = st.Page(
    "pages/documentation.py", title="Documentation", icon=":material/dashboard:"
)
fonctionAffine = st.Page(
    "pages/fonctionAffine.py", title="Fonction affine", icon=":material/functions:"
)
hello = st.Page(
    "pages/hello.py", title="Hello", icon=":material/waving_hand:"
)
home = st.Page(
    "pages/home.py", title="Home", default=True, icon=":material/home:"
)
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Accueil": [home, hello],
            "Tools": [fonctionAffine],
            "Documentation": [documentation],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
################################################################# menu
# st.set_page_config(initial_sidebar_state="expanded")

# Définir les pages
pages = ["Home", "Documentation", "Fonction Affine"]
# # page = ["Home", "Documentation", "Hello", "Fonction Affine", "About"]

# styles = {
#     "nav": {
#         "background-color": "royalblue",
#         "justify-content": "left",
#         # "background-color": "white",
#     },
#     "img": {
#         "padding-right": "14px",
#     },
#     "span": {
#         "color": "white",
#         "padding": "14px",
#     },
#     "active": {
#         "background-color": "white",
#         "color": "white",
#         "font-weight": "normal",
#         "padding": "14px",
#     }
# }
# # Contenu principal
# if pages == "Documentation":
#     st.switch_page("pages/documentation.py")
# # elif page == "Hello":
# #     st.switch_page("pages/hello.py")
# elif pages == "Fonction Affine":
#     st.switch_page("pages/fonctionAffine.py")
# # elif page == "About":
# #     st.switch_page("pages/about.py")
# else:
#     st.switch_page("pages/home.py")

# match pages:
#     case "Documentation":
#         st.switch_page("pages/documentation.py")
#     case "Fonction Affine":
#         st.switch_page("pages/fonctionAffine.py")
#     case _:
#         st.switch_page("pages/home.py")





# options = {
#     "show_menu": True,
#     "show_sidebar": False,
# }

# page = st_navbar(
#     pages,
#     # logo_path=logo_path,
#     # urls=urls,
#     styles=styles,
#     options=options,
# )

# functions = {
#     "Home": pg.show_home,
#     "Documentation": pg.show_documentation,
#     "Fonction Affine": pg.show_fonctionAffine,
#     # "API": pg.show_api,
#     # "Examples": pg.show_examples,
#     # "Community": pg.show_community,
# }
# go_to = functions.get(page)
# if go_to:
#     go_to()


################################################################# log
# # Créer le dossier log s'il n'existe pas
# if not os.path.exists('log'):
#         os.makedirs('log')
# # Configuration de la journalisation
# logging.basicConfig(level=logging.INFO,  # Définir le niveau de journalisation
#                     format='%(asctime)s - %(message)s',  # Format du message
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='log/file_changes.log',  # Fichier journal
#                     filemode='w')  # Mode d'écriture

# # logger_blacklist = [
# #     '.streamlist',
# #     'Log',
# # ]

# # logger = logging.getLogger()  # Création d'un logger






# # Gestionnaire d'événements pour la surveillance de fichiers
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         logging.info(f'Modified: {event.src_path}')
    
#     def on_created(self, event):
#         logging.info(f'Created: {event.src_path}')
        
#     def on_deleted(self, event):
#         logging.info(f'Deleted: {event.src_path}')

# # Configurer l'observateur pour surveiller les modifications dans le répertoire courant
# event_handler = MyHandler()  # Créer une instance de LoggingEventHandler
# observer = Observer()  # Créer un observateur
# # path = '.'  # Surveiller le répertoire courant
# # for module in logger_blacklist :
# #     observer.schedule(event_handler, path, recursive=True)  # Planifier l'observateur
# observer.start()  # Démarrer l'observateur

# logger_blocklist = [
#     ".",
#     "page",
# ]

# for module in logger_blocklist:
#     observer.schedule(event_handler, module, recursive=False)