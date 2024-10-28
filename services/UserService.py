

from dataclasses import dataclass
import pandas as pd
from Entity.User import User
from Entity.Roles import Roles
from DAL.Repository.UserRepositoryCSV import UserRepositoryCSV
from services.VerificationsService import VerificationsService
# from services.connectionService import ConnectService
from Transiant import transiant_connection
from Transiant.UserConnected import UserConnected

import re
import keyboard

@dataclass
class UserService:
    
    __repoUserCSV = UserRepositoryCSV()
    __verificationService = VerificationsService()
    # __connectService = ConnectService()
    
    # def __init__(self, UserRepositoryForCRUD: UserRepositoryForCRUD = UserRepositoryForCRUD(), VerificationsService: VerificationsService = VerificationsService()):
    #     self.__repoUserCSV = UserRepositoryForCRUD
    #     self.__verificationService = VerificationsService()
    
#####################################################################################  méthodes utilisée
    def CreateUserRoleUser(self, user:User) -> User:
        """Creates a new user, fetches all users from the database and prints them
        """
        # user = User.ConstructUser("pat","1234","lol@lol.fr",13008,47,1.8,72,Roles.User)
        if user is None:
            print("Aucun utilisateur créé")
            return None

        if self.__isEmailExiste(user.email):
            raise ValueError(f"Un utilisateur avec ce courriel : \"{user.email}\" existe déjà présent.")
        if self.__isNameExiste(user.nom):
            raise ValueError(f"Un utilisateur avec ce nom : \"{user.nom}\" existe déjà présent.")

            # repoUserCSV = UserRepositoryForCRUD()
        # print("passe CreateUserRoleUser")
        user = self.__repoUserCSV.Create(user)
        return user

    def UpdateUserRoleUser(self, userModified:User, userConnected:UserConnected ) -> User:

        if userModified is None or userConnected is None:
            print("Aucun utilisateur mis-à-jour")
            return None

        nbEmail = self.__CountEmail(userModified.email)
        if nbEmail > 0:
            if userModified.email != userConnected.email:
                raise ValueError(f"Un utilisateur avec ce courriel : \"{userModified.email}\" existe déjà présent.")

        # print("*"*80)
        # print(nbEmail)
        # print(userModified.nom != userConnected.name)
        # print("userModified.nom = " + userModified.nom)
        # print("userConnected.name = " + userConnected.name)
        # print("*"*80)
        nbEname = self.__CountName(userModified.nom)

        if nbEname > 0:
            if userModified.nom != userConnected.name:
                raise ValueError(f"Un utilisateur avec ce nom : \"{user.nom}\" existe déjà présent.")

        user = self.__repoUserCSV.FindUserById(userConnected.UserId)
        userModified.mot_de_passe = user.mot_de_passe     
        user = self.__repoUserCSV.Update(userModified)

        return user
    
    @classmethod
    def FindUserByEmail(cls, trs: transiant_connection) -> User:
        mail = trs
        if cls.__verificationService.IsEmail(trs.email):
            myUser = cls.__repoUserCSV.FindUserByEmail(trs.email)
            return myUser
        return None

    @classmethod
    def __isEmailExiste(cls, email:str):
        df = cls.__repoUserCSV.FindAll()
        if not df['email'].isin([email]).any():
            return False
        print("This email exists")
        return True
    
    @classmethod
    def __CountEmail(cls, email:str):
        df = cls.__repoUserCSV.FindAll()
        result = len(df[df["email"]==email])
        return result
    
    @classmethod
    def __isNameExiste(cls, name:str):
        df = cls.__repoUserCSV.FindAll()
        if not df['nom'].isin([name]).any():
            return False
        print("This name exists")
        return True
    
    @classmethod
    def __CountName(cls, name:str):
        df = cls.__repoUserCSV.FindAll()
        return len(df[df["nom"]==name])
#####################################################################################

    # def CreateUserRoleUser(self) -> User:
    #     """Creates a new user, fetches all users from the database and prints them
    #     """
    #     user = self.__askForCreateUserRoleUser()
    #     # user = User.ConstructUser("pat","1234","lol@lol.fr",13008,47,1.8,72,Roles.User)
    #     if user is None:
    #         print("Aucun utilisateur créé")
    #         return None
        
    #     user = self.__repoUserCSV.Create(user)
    #     return user

    
    # def CreateUserRoleAdmin(self) -> User:
    #     """Creates a new admin, fetches all users from the database and prints them
    #     """
    #     user = self.__askForCreateUserRoleAdmin()
    #     # user = User.ConstructUser("adminPat","1234","lol@admin.fr",13008,47,1.8,72,Roles.Admin)
    #     if user is None:
    #         print("Aucun administrateur créé")
    #         return None
    #     user = self.__repoUserCSV.Create(user)
    #     return user
    
    def FindAll(self) ->pd.DataFrame:
        # repoUserCSV = UserRepositoryForCRUD()
        user = self.__repoUserCSV.FindAll()
        return user
    
    # def Setmodif() -> User:
    #     # verifi si user ou admin
    #     # si user alors SetModificationOfUseIfSessionAndRoleUser
    #     # si admin alors SetModificationOfUseIfSessionAndRoleAdmin
    #     pass
    
    
    # def SetModificationOfUserIfSessionAndRoleUser(self, user:User) -> User:
    #     """_Set modification if the user is his role is user
        
    #     Args:
    #         user (User): User instance

    #     Returns:
    #         pd.DataFrame: pandas dataframe
    #     """
    #     # TODO check session and if role is user
    #     print("")
    #     print(f'{"Modification du profil" :=^80}')
    #     choice = self.__PrintActionsForRoleUser(user)
    #     user = self.__GetActionAndDoForRoleUser(user, choice)
    #     print("="*80)
    #     print("")
    #     return user


    # def __PrintActionsForRoleUser(self, user):
    #     regInputChoise = re.compile(r"([1-2]{1})")

    #     choice = 0
    #     while True:
    #         print("Vos informations de profil:")
    #         print(str(user))
    #         print("")
    #         print("Actions pour vous en avec votre role user:")
    #         print("1. Modifier mon mot de passe")
    #         print("2. (espace ou entrer) Fermer l'application")
    #         print("")
    #         choice = input("Choisissez une action : ")
            
    #         self.__pressSpaceOrEnter()

    #         if not re.fullmatch(regInputChoise, choice):
    #             print("Choix invalide. Veuillez réessayer.")
    #         else:
    #             break
    #     return choice

    # def __pressSpaceOrEnter(self):
    #     if keyboard.is_pressed("space") or keyboard.is_pressed("enter"):
    #         self.__exitAppli()
    
    # def __GetActionAndDoForRoleUser(self, user:User, __choice):
    #     match __choice:
    #         case "1":
    #             user.mot_de_passe = input("Veuillez nous donner votre mot de passe : ")
    #             user = self.__repoUserCSV.Update(user)
    #             print(f"Utilisateur modifié avec succès : {str(user)}")
    #         case "2":
    #             self.__exitAppli()
    #         case _:
    #             print("Choix invalide.")
    #     return user
    
    
    # def SetModificationOfUserIfSessionAndRoleAdmin(self, user:User) -> User:
    #     """_Set modification if the user is his role is user
        
    #     Args:
    #         user (User): User instance

    #     Returns:
    #         pd.DataFrame: pandas dataframe
    #     """
    #     print("")
    #     print(f'{"Modification du profil" :=^80}')
    #     userName = self.__askWhichUserToBeModified()
    #     choice = self.__PrintActionsForRoleAdmin(userName)
    #     user = self.__GetActionAndDoForRoleAdmin(user, choice)
    #     print("="*80)
    #     print("")
    #     return user

    # def __askWhichUserToBeModified(self) -> str:
    #     df = self.FindAll()
    #     print(df)
    #     print("")
    #     return input("Qui voulez-vous modifier ? (sélectionné par nom) : ")
    
    # def __PrintActionsForRoleAdmin(self, userName):
    #     regInputChoise = re.compile(r"([1-9]{1})")
    #     regEmptyString = re.compile(r"(^$)") # ^\s*$
    #     regEmptyString2 = re.compile(r"(\s*$)") # ^\s*$
    #     regWiteString = re.compile(r"(\s*)") # ^\s*$
    #     choice = 0
    #     while True:
    #         print("Les informations du profil sélectionné:")
    #         dfUser = self.__repoUserCSV.FindUserByName(userName)
    #         if dfUser is None:
    #             print("Utilisateur non trouvé.")
    #             continue
    #         print(dfUser)
    #         print("")
    #         print("Actions pour vous en avec votre role user:")
    #         print("1. Modifier le nom")
    #         print("2. Modifier mon mot de passe")
    #         print("3. Modifier l'email")
    #         print("4. Modifier le code postal")
    #         print("5. Modifier l'age")
    #         print("6. Modifier la taille")
    #         print("7. Modifier le poids")
    #         print("8. Modifier le role")
    #         print("9. Fermer l'application")
    #         print("")
    #         choice = input("Choisissez une action : ")
            
    #         self.__pressSpaceOrEnter()
            
    #         if not re.fullmatch(regInputChoise, choice) or not re.fullmatch(regEmptyString) or not re.fullmatch(regWiteString) or not re.fullmatch(regEmptyString2):
    #             print("Choix invalide. Veuillez réessayer.")
    #         else:
    #             break
    #     return choice
    
    # def __GetActionAndDoForRoleAdmin(self, user:User, __choice):
    #     modif = False
    #     match __choice:
    #         case "1":
    #             user.nom = input(f"Nodification du nom, ancien : {user.nom} :")
    #             user.nom = self.__setNanme()
    #             modif = True
    #         case "2":
    #             user.mot_de_passe = input("Veuillez entrer le nouveau mot-de-passe : ")
    #             modif = True
    #         case "3":
    #             user.nom = input(f"Nodification de l'email, ancien : {user.email} :")
    #             user.nom = self.__setEmail()
    #             modif = True
    #         case "4":
    #             user.nom = input(f"Nodification du code postal, ancien : {user.code_postal} :")
    #             user.nom = self.__setPostalCode()
    #             modif = True
    #         case "5":
    #             user.nom = input(f"Nodification d'age, ancien : {user.age} :")
    #             user.nom = self.__setAge()
    #             modif = True
    #         case "6":
    #             user.nom = input(f"Nodification la taille, ancien : {user.taille} :")
    #             user.nom = self.__setSize()
    #             modif = True
    #         case "7":
    #             user.nom = input(f"Nodification le poids, ancien : {user.poids} :")
    #             user.nom = self.__setWeight()
    #             modif = True
    #         case "8":
    #             user.nom = input(f"Nodification le role, ancien : {Roles(user.role).name} : {Roles(user.role).value}")
    #             user.nom = self.__setRole()
    #             modif = True
    #         case "9":
    #             self.__exitAppli()
    #         case _:
    #             print("Choix invalide.")
    #     if modif:
    #         user = self.__repoUserCSV.Update(user)
    #         print(f"Utilisateur modifié avec succès : {str(user)}")
    #     return user

    # def __exitAppli(self):
    #     print("Merci d'avoir utilisé notre application!")
    #     exit()
    
    
    def DeleateUser(self,user):
        
        """deletes a user from the database
        """
        # TODO check if user is admin
        
        # repoUserCSV = UserRepositoryForCRUD()
        self.__repoUserCSV.Delete(user)
        print(f"Utilisateur supprimé avec succès : {str(user)}")
        
    
    # def __askForCreateUserRoleUser(self) -> User:
    #     """requests the elements needed to create a user in the database

    #     Returns:
    #         User: User object
    #     """
    #     try:
    #         __name, __password, __email, __postalCode, __age, __size, __weight = self.__askUserProperties()
    #         return User.ConstructUser(__name,__password,__email,__postalCode,__age,__size,__weight,Roles.User)
    #     except Exception as e:
    #         print(f"create user => An error occurred: {e}")
    #         return None

    # def __askForCreateUserRoleAdmin(self) -> User:
    #     """requests the elements needed to create an admin in the database

    #     Returns:
    #         User: User object
    #     """
    #     try:
    #         __name, __password, __email, __postalCode, __age, __size, __weight = self.__askUserProperties()
    #         return User.ConstructUser(__name,__password,__email,__postalCode,__age,__size,__weight,Roles.Admin)
    #     except Exception as e:
    #         print(f"create admin => An error occurred: {e}")
    #         return None
    
    # def setUserAdmin(self,name,password,email,postalCode,age,size,weight) -> User:
    #     try:
    #         return User.ConstructUser(name,password,email,postalCode,age,size,weight,Roles.Admin)
    #     except Exception as e:
    #         print(f"create admin => An error occurred: {e}")
    #         return None
    # def setJustUser(self,name,password,email,postalCode,age,size,weight) -> User:
    #     try:
    #         return User.ConstructUser(name,password,email,postalCode,age,size,weight,Roles.User)
    #     except Exception as e:
    #         print(f"create user => An error occurred: {e}")
    #         return None

    # def __askUserProperties(self):
    #     __name = self.__setNanme()
    #     __password = input("Veuillez nous donner votre mot de passe : ")
    #     __email = self.__setEmail()
    #     __postalCode = self.__setPostalCode()
    #     __age, loop = self.__setAge()
    #     __size = self.__setSize()
    #     __weight = self.__setWeight()
    #     return __name,__password,__email,__postalCode,__age,__size,__weight
    
    

    
    # def __setWeight(self):
    #     while True:
    #         weight = input("Veuillez entrer le poids sans virgule : ")
    #         if not self.__verificationService.IsWeight(weight):
    #         # if not re.fullmatch(reAgeAndWeight, weight):
    #             print("Veuillez saisir une taille valide de type: 64, 42, 135")
    #         else:
    #             break
    #     return weight

    
    # def __setSize(self):
    #     while True:
    #         size = input("Veuillez entrer la taille : ")
    #         if not self.__verificationService.IsSize(size):
    #             print("Veuillez saisir une taille valide de type: 1.5, 2, 1.88")
    #         else:
    #             break
    #     return size

    
    # def __setAge(self):
    #     while True:
    #         age = input("Veuillez entrer l'age : ")
    #         if not self.__verificationService.IsAge(age):
    #             print("Veuillez saisir un age valide.")
    #         else:
    #             break
    #     return age

    
    # def __setPostalCode(self):
    #     while True:
    #         postalCode = input("Veuillez entrer le code postal : ")
    #         if not self.__verificationService.IsCodePostal(postalCode):
    #             print("Veuillez saisir un code postal valide.")
    #         else:
    #             break
    #     return postalCode

    
    # def __setEmail(self):
    #     while True:
    #         email = input("Veuillez entrer le courriel : ")
    #         if not self.__verificationService.IsEmail(email):
    #             print("Veuillez saisir un courriel valide.")
    #         else:
    #             break
    #     return email

    
    # def __setNanme(self):
    #     while True:
    #         name = input("Veuillez entrer le nom : ")
    #         if not self.__verificationService.IsName(name):
    #             print("Veuillez saisir un nom valide.")
    #         else:
    #             break
    #     return name
    
    # def __setRole(self):
    #     print("Liste des roles :")
    #     for role in Roles:
    #         print(f"{role.name} : {role.value}") 
    #     while True:
    #         role = input("Veuillez entrer numéro de rôle : ")
    #         if not self.__verificationService.IsInt(role):
    #             print("Veuillez saisir un numéro de rôle valide.")
    #             continue
    #         if not self.__verificationService.IsRole(role):
    #             print("Veuillez saisir un role valide.")
    #         else:
    #             break
    #     return role
    

    
    
            