import streamlit as st
from services.haschService import haschService
from datetime import datetime
from Entity.Roles import Roles
import pandas as pd
from Transiant.Personne import Personne

class User(Personne):
    UserId = None
    nom = None
    mot_de_passe = None
    email = None
    code_postal = None
    age = None
    taille = None
    poids = None
    role = None
    CreatedDate = None
    UpdatedDate = None
    DeletedDate = None

    def __init__(self):
        pass
    
    @classmethod
    def ConstructUser(cls, nom: str, mot_de_passe:str, email, code_postal: int, age:int, taille:float, poids:int, role:Roles):
        print(mot_de_passe)
        user = cls()
        user.UserId = -1
        user.nom = nom
        user.mot_de_passe = haschService().HashPassord(mot_de_passe)
        user.email = email
        user.code_postal = code_postal
        user.age = age
        user.taille = taille
        user.poids = poids
        user.role = role.value
        return user

    @classmethod
    def ConstructUserAllAttributsFrormDf(cls, userId: str,nom: str, mot_de_passe:str, email, code_postal: int, age:int, taille:float, poids:int, role:Roles, CreatedDate:datetime.timestamp, UpdatedDate:datetime.timestamp, DeletedDate:datetime.timestamp):
        """_summary_
            construct User with all attributes from dataframe
            No password encryption, it's already encrypted in dataframe
            Juste values frome dataframe
        """
        user = cls()
        user.UserId = userId
        user.nom = nom
        user.mot_de_passe = mot_de_passe # No encryption
        user.email = email
        user.code_postal = code_postal
        user.age = age
        user.taille = taille
        user.poids = poids
        user.role = role #
        user.CreatedDate = CreatedDate
        user.UpdatedDate = UpdatedDate
        user.DeletedDate = DeletedDate
        return user
    
    @classmethod
    def ConstructUserSimple(cls, userId: str,nom: str, mot_de_passe:str, email:str, code_postal: int, age:int, taille:float, poids:int, role:Roles):
        """_summary_
            construct User with all attributes from dataframe
            No password encryption, it's already encrypted in dataframe
            Juste values frome dataframe
        """
        print("init construct user  simple")
        user = cls()
        user.UserId = userId
        user.nom = nom
        user.mot_de_passe = mot_de_passe
        user.email = email
        user.code_postal = code_postal
        user.age = age
        user.taille = taille
        user.poids = poids
        user.role = role 
        print("fin istanciation user simple")
        return user
    
    def set_CreatedDate(self):
        self.CreatedDate = datetime.timestamp(datetime.now())
        
    def set_UpdatedDate(self):
        self.UpdatedDate = datetime.timestamp(datetime.now())

    def set_DeletedDate(self):
        self.DeletedDate = datetime.timestamp(datetime.now())
  
    def afficher_infos(self):
        print(f"Nom: {self.nom}")
        print(f"Email: {self.email}")
        print(f"Code postal: {self.code_postal}")
        print(f"Âge: {self.age} ans")
        print(f"Taille: {self.taille} m")
        print(f"Poids: {self.poids} kg")
    
    def afficher_infos_str(self) -> str:
        return (f"""
                    * Nom: {self.nom}
                    * Email: {self.email}
                    * Code postal: {self.code_postal}
                    * Âge: {self.age} ans
                    * Taille: {self.taille} m
                    * Poids: {self.poids} kg
                    """)
        print(f"Nom: {self.nom}")
        print(f"Email: {self.email}")
        print(f"Code postal: {self.code_postal}")
        print(f"Âge: {self.age} ans")
        print(f"Taille: {self.taille} m")
        print(f"Poids: {self.poids} kg")
    
    def calculer_imc(self):
        # IMC = poids / (taille^2)
        imc = self.__poids / (self.__taille ** 2)
        return round(imc, 2)
    

    # Vérifie si le role de l'utilisateur est celui d'un admin ou superAdmin
    # Renvoie le résultat
    def IsAdmin(self):
        if self.role == Roles.Roles.SuperAdmin or self.role == Roles.Roles.Admin:
            return True
        return False
    
    def __str__(self) -> str:
        return f"User({self.UserId},\n {self.nom},\n{self.mot_de_passe},\n {self.email},\n {self.code_postal},\n {self.age},\n {self.taille},\n {self.poids},\n {self.role})"

    def __eq__(self, user: object) -> bool:
        if not isinstance(user, User):
            return False
        if (self.nom == user.nom) and (self.email == user.email) and (self.code_postal == user.code_postal) and (self.age == user.age) and (self.taille == user.taille) and (self.poids==user.poids):
            return True
        return False
    

        
    
    @classmethod
    def IsInstanceOfUser(cls, user: object) -> bool:
        # print("Check instance")
        if not isinstance(user, User):
            print("user is not User object")
            return False
        return True
    
    @classmethod
    def UserFromRowDf(cls, row : pd.DataFrame):
        instance = cls()
        for key, value in row.items():
            setattr(instance, key, value)
        return instance
    
