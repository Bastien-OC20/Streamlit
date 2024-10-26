import streamlit as st

from services.Verifications import VerificationsService
from services.UserService import UserService
from Entity.Roles import Roles
from Entity.User import User
from directory.dialogBox.DialogBox import DialogBox

def show_user():

    st.session_state.active_page = "user_page"
    if st.session_state.logged_in:
        profilVue, membres = st.tabs(["Profil", "Membres"])
 
    __verificationService = VerificationsService()
    __userService = UserService()

    
    if not st.session_state.logged_in:

        st.header("Enregistrement d'un nouvel utilisateur")
        col1, col2 = st.columns(2)

        with col1:
            email = st.text_input("Veuillez entre votre mail :", key="ask_email")
            password = st.text_input("Veuillez nous donner votre mot de passe : ", type="password", key="ask_password")
        with col2:
            name = st.text_input("Veuillez entrer le nom : ", key="ask_name")
            st.write()
            postalCode = st.text_input("Veuillez entrer le code postal : ", key="ask_postalCode")
            age = st.text_input("Veuillez entrer l'age : ", key="ask_age")
            size = st.text_input("Veuillez entrer la taille : ", key="ask_size")
            weight = st.text_input("Veuillez entrer le poids sans virgule : ", key="ask_weight")
        
        def checkData()->str:
            textError = ""
            checkOK = True
            if not __verificationService.IsEmail(email):
                checkOK = False
                st.write("* Veuillez saisir un courriel valide.")
                textError = f"{textError}\n* Veuillez saisir un courriel valide."           
            if not __verificationService.IsName(name):
                checkOK = False
                st.write("* Veuillez saisir un nom valide.")
                textError = f"{textError}\n* Veuillez saisir un nom valide."
            if not __verificationService.IsCodePostal(postalCode):
                checkOK = False
                st.write("* Veuillez saisir un code postal valide.")
                textError = f"{textError}\n* Veuillez saisir un code postal valide."
            if not __verificationService.IsAge(age):
                checkOK = False
                st.write("* Veuillez saisir un age valide.")
                textError = f"{textError}\n* Veuillez saisir un age valide."
            if not __verificationService.IsSize(size):
                checkOK = False
                st.write("* Veuillez saisir une taille valide de type: 1.5, 2, 1.88")
                textError = f"{textError}\n* Veuillez saisir une taille valide de type: 1.5, 2, 1.88"
            if not __verificationService.IsWeight(weight):
                checkOK = False
                st.write("* Veuillez saisir une poids valide de type: 64, 42, 135")
                textError = f"{textError}\n* Veuillez saisir une poids valide de type: 64, 42, 135"
            if checkOK:
                return None
            return textError
        
        resultCheck = checkData()
        userCreated = None
        if  st.button("enregistrer"):
            if isinstance(resultCheck, str):
                reason="Erreurs dans les données rentrées"
                DialogBox.DLgInfoMessage(reason, resultCheck)
                return
            try:
                myUser = User.ConstructUser(name,password,email,postalCode,age,size,weight,Roles.User)
                userCreated = __userService.CreateUserRoleUser(myUser)

            except ValueError as e:
                reason="Erreur d'enregistrement"
                DialogBox.DLgInfoMessage(reason, e)
            
            except Exception:
                reason="Erreur inattendue"
                DialogBox.DLgErreur(reason)

            else: # permet de réaliser la suite du code après le try qui c'est bien passé
                if userCreated is None:
                    reason="Erreur dans la création de l'utilisateur"
                    DialogBox.DLgErreur(reason)
                    return
                reason=f"Enregistrement réussi de l'utilisateur {name}"
                DialogBox.DLgInfoMessage(reason,userCreated)
                st.session_state.logged_in = True

    else:
        with profilVue:
            st.header("Profil utilisateur") 
            
        with membres:
            st.header("Liste des membres") 

show_user()