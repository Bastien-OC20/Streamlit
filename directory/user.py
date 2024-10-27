import streamlit as st

from services.Verifications import VerificationsService
from services.UserService import UserService
from Entity.Roles import Roles
from Entity.User import User
from directory.dialogBox.DialogBox import DialogBox
from Transiant.transiant_connection import transiant_connection
from Transiant.UserConnected import UserConnected
# from Transiant.transiant_user import transiant_user
from Entity.Roles import Roles

def show_user():
    # print(Roles.User.value)
    if st.session_state.active_page != "user_page":
        st.session_state.modif_user = False
    st.session_state.active_page = "user_page"


    __verificationService = VerificationsService()
    __userService = UserService()

    def checkData(email,name, postalCode, age, size, weight)->str:
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
            st.write("* Veuillez saisir une taille valide en mètre du type: 1.5, 2, 1.88")
            textError = f"{textError}\n* Veuillez saisir une taille valide de type: 1.5, 2, 1.88"
        if not __verificationService.IsWeight(weight):
            checkOK = False
            st.write("* Veuillez saisir une poids valide de type: 64, 42, 135")
            textError = f"{textError}\n* Veuillez saisir une poids valide de type: 64, 42, 135"
        if checkOK:
            return None
        return textError

    # print("st.session_state.modif_user")
    # print(st.session_state.modif_user)
    if "modif_user" not in st.session_state:
        st.session_state.modif_user = False
        
    if st.session_state.logged_in:
        profilVue, membres = st.tabs(["Profil", "Membres"])
    
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
        
        
        resultCheck = checkData(email,name, postalCode, age, size, weight)
        userCreated = None
        if  st.button("enregistrer"):
            if isinstance(resultCheck, str):
                reason="Erreurs dans les données rentrées"
                DialogBox.DLgInfoMessage(reason, resultCheck)
                return
            try:
                myUser = User.ConstructUser(name,password,email,postalCode,age,size,weight,Roles.User.value)
                
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
                DialogBox.DLgInfoMessage(reason,userCreated.afficher_infos_str())
                st.session_state.logged_in = True

    else:
        with profilVue:
            state = st.session_state.modif_user

            st.header("Profil utilisateur") 
            transia_conected = transiant_connection(st.session_state.user_email, "_")
            user_conected = __userService.FindUserByEmail(transia_conected)
            # print(user_conected.afficher_infos())
            c1, c2 = st.columns(2)
            with c1:
                if not state:
                    st.text(f"nom : {user_conected.nom}")
                else:
                    new_nom = st.text_input("nom :",user_conected.nom, key="modif_nom")

                if not state:
                    st.text(f"courriel : {user_conected.email}")
                else:
                    new_email = st.text_input("courriel :",user_conected.email, key="modif_email")

                if not state:
                    st.text(f"code postal : {user_conected.code_postal}")
                else:
                    new_postalcode = st.text_input("code postal :",user_conected.code_postal, key="modif_code_postal")
                
                if not state:
                    st.text(f"age : {user_conected.age}")
                else:
                    new_age = st.text_input("age :",user_conected.age, key="modif_age")
                
                if not state:
                    st.text(f"taille : {user_conected.taille}")
                else:
                    new_size = st.text_input("taille :",user_conected.taille, key="modif_taille")
                
                if not state:
                    st.text(f"poids : {user_conected.poids}")
                else:
                    new_weight = st.text_input("poids :",user_conected.poids, key="modif_poids")

            with c2:
                
                if st.button("Modifier" if not state else "Annuler"):
                    st.session_state.modif_user = not state
                    st.rerun()
                st.write()
                if st.session_state.modif_user:
                    if st.button("Valider"):
                        resultCheck = checkData(new_email,new_nom, new_postalcode, new_age, new_size, new_weight)
                        userModifed = None
                        if isinstance(resultCheck, str):
                            reason="Erreurs dans les données de création de l'utilisateur"
                            DialogBox.DLgInfoMessage(reason, resultCheck)
                            return
                        
                        try:
                            userModified = User.ConstructUserSimple(st.session_state.user_id,
                                                             new_nom,
                                                             "",
                                                             new_email,
                                                             int(new_postalcode),
                                                             int(new_age),
                                                             float(new_size),
                                                             int(new_weight),
                                                             Roles(st.session_state.user_role))
                            userConnected = UserConnected(st.session_state.user_id, st.session_state.user_name, st.session_state.user_email)
                            userModifed = __userService.UpdateUserRoleUser(userModified, userConnected)
                            

                        except ValueError as e: 
                            reason="Erreur lors de la mise-à-jour"
                            DialogBox.DLgInfoMessage(reason, e)
                        
                        except Exception:
                            reason="Erreur inattendue"
                            DialogBox.DLgErreur(reason)

                        else: # permet de réaliser la suite du code après le try qui c'est bien passé
                            if userModifed is None:
                                reason="Erreur dans la mise-à-jour de l'utilisateur"
                                DialogBox.DLgErreur(reason)
                                return
                            reason=f"Modification de l'utilisateur \"{userModifed.nom}\" réussie"
                            DialogBox.DLgInfoMessage(reason,userModifed.afficher_infos_str())
                            st.session_state.logged_in = True


















                        # # myTransiantUser = transiant_user()
                        # if __verificationService.IsName(name):
                        #     # myTransiantUser.nom = name
                        #     pass #TODO modif bdd

        with membres:
            if "modif_user" not in st.session_state:
                del st.session_state.modif_user
            st.header("Liste des membres") 


            df_all_users = __userService.FindAll()
            st.dataframe(df_all_users, column_order=("nom","email", "code_postal", "age", "taille", "poids", "role" ))


show_user()