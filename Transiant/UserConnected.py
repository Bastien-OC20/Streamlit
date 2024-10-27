from dataclasses import dataclass
from Transiant.Personne import Personne

@dataclass
class UserConnected(Personne):
    __instance = None
    UserId:str=""
    name:str=""
    # email:str=""

    def __init__(self,UserId:str, name:str, email:str):
        self.UserId = UserId
        self.name = name
        super().__init__(cls, email)
            
    def __new__(cls, UserId, name, email):
        if not cls.__instance:
            print("creating instance")
            
            # cls.email = email
            cls.__instance = super(UserConnected, cls).__new__(cls)
            super().__init__(cls, email)
            cls.UserId = UserId
            cls.name = name
        return cls.__instance
    
    def getUserConnectedSingleton(cls):
        return cls.__instance