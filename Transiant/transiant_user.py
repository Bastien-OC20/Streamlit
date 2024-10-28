from Entity.Roles import Roles
from dataclasses import dataclass
from Entity.User import User

@dataclass
class transiant_user(User):
    # UserId = None
    # nom = None
    # mot_de_passe = None
    # email = None
    # code_postal = None
    # age = None
    # taille = None
    # poids = None
    # role = None
    # CreatedDate = None
    # UpdatedDate = None
    # DeletedDate = None

    def __init__(self):
        # User.__init__()
        pass
    
    @classmethod
    def ConstructUserTransiant(cls,id, nom: str, email, code_postal: int, age:int, taille:float, poids:float, role:Roles):
        user = cls()
        user.UserId = id
        user.nom = nom
        # user.mot_de_passe = mot_de_passe
        user.email = email
        user.code_postal = code_postal
        user.age = age
        user.taille = taille
        user.poids = poids
        user.role = role.value
        return user