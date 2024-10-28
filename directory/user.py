import streamlit as st

from services.VerificationsService import VerificationsService
from services.UserService import UserService
from Entity.Roles import Roles
from Entity.User import User
from directory.dialogBox.DialogBox import DialogBox
from Transiant.transiant_connection import transiant_connection
from Transiant.UserConnected import UserConnected
from Entity.Roles import Roles

def show_user():
    if st.session_state.active_page != "user_page":
        st.session_state.modif_user = False
    st.session_state.active_page = "user_page"


    __verificationService = VerificationsService()
    __userService = UserService()

    st.write(f"nom : {st.session_state.user_name}")
    st.write(f"email : {st.session_state.user_email}")
    st.write(f"id : {st.session_state.user_id}")
    st.write(f"role : {st.session_state.user_role}")
    
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
        
        
        resultCheck = __verificationService.checkAllData(email,name, postalCode, age, size, weight)
        st.write(resultCheck)
        userCreated = None
        if  st.button("enregistrer"):
            if resultCheck != "":
                reason="Erreurs dans les données rentrées"

                DialogBox.DLgInfoMessage(reason, resultCheck)
                return
            try:
                myUser = User.ConstructUser(name,password,email,postalCode,age,size,weight,Roles.User)
                userCreated = __userService.CreateUserRoleUser(myUser)

            except ValueError as e:
                reason="Erreur d'enregistrement"
                DialogBox.DLgInfoMessage(reason, e)
                return
            
            except Exception:
                reason="Erreur inattendue"
                DialogBox.DLgErreur(reason)
                return

            else: # permet de réaliser la suite du code après le try qui c'est bien passé
                if userCreated is None:
                    reason="Erreur dans la création de l'utilisateur"
                    DialogBox.DLgErreur(reason)
                    return
                reason=f"Enregistrement réussi de l'utilisateur {name}"
                DialogBox.DLgInfoMessage(reason,userCreated.afficher_infos_str())

    else:
        with profilVue:

            state = st.session_state.modif_user

            st.header("Profil utilisateur") 
            transia_conected = transiant_connection(st.session_state.user_email, "_")
            user_conected = __userService.FindUserByEmail(transia_conected)
            c1, c2 = st.columns(2)
            with c1:
                st.text(f"nom : {user_conected.nom}")

                st.text(f"courriel : {user_conected.email}")

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
                    st.text(f"poids : {int(user_conected.poids)}")
                else:
                    new_weight = st.text_input("poids :",int(user_conected.poids), key="modif_poids")

            with c2:
                
                if st.button("Modifier" if not state else "Annuler"):
                    st.session_state.modif_user = not state
                    st.rerun()
                st.write()
                if st.session_state.modif_user:
                    if st.button("Valider"):
                        resultCheck = __verificationService.checkSimpleData(new_postalcode, new_age, new_size, new_weight)
                        st.write(resultCheck)
                        userModifed = None
                        if resultCheck != "":
                            reason="Erreurs dans les données de création de l'utilisateur"
                            DialogBox.DLgInfoMessage(reason, resultCheck)
                            return

                        try:
                            userModifed = User.ConstructUserSimple(
                                st.session_state.user_id,
                                st.session_state.user_name,
                                None,
                                st.session_state.user_email,
                                int(new_postalcode),
                                int(new_age),
                                float(new_size),
                                int(new_weight),
                                Roles(st.session_state.user_role))
                            
                            userConnected = UserConnected(
                                st.session_state.user_id, 
                                st.session_state.user_name, 
                                st.session_state.user_email)
                            
                            result = User()
                            result = __userService.UpdateUserRoleUser(userModifed, userConnected)
                            if result is None:
                                reason=f"Aucune action"
                                msg="Aucune Modification de l'utilisateur courrant constaté"
                                # st.rerun()
                                DialogBox.DLgInfoMessage(reason,msg)
                                st.session_state.modif_user = False
                                return

                            st.session_state.logged_in = True
                            st.session_state.user_name = result.nom
                            st.session_state.user_email = result.email
                            

                        except ValueError as e: 
                            reason="Erreur lors de la mise-à-jour"
                            DialogBox.DLgInfoMessage(reason, e)
                            return
                        
                        except Exception:
                            print("exeption user modif")
                            reason="Erreur inattendue"
                            DialogBox.DLgErreur(reason)
                            return

                        else: # permet de réaliser la suite du code après le try qui c'est bien passé
                            if result is None:
                                reason="Erreur dans la mise-à-jour de l'utilisateur"
                                DialogBox.DLgErreur(reason)
                                st.session_state.modif_user = False

                                return
                            reason=f"Modification de l'utilisateur \"{result.nom}\" réussie"
                            DialogBox.DLgInfoMessage(reason,result.afficher_infos_str())
                            st.session_state.modif_user = False
                            return

        with membres:
            if "modif_user" not in st.session_state:
                del st.session_state.modif_user
            st.header("Liste des membres") 


            df_all_users = __userService.FindAll()
            st.dataframe(df_all_users, column_order=("nom","email", "code_postal", "age", "taille", "poids", "role" ))


show_user()