from dataclasses import dataclass
from services.haschService import haschService
from Entity.User import User

@dataclass
class ConnectService:

    __myHaschService = haschService()
    def __int__():
        pass

    def __checkEmail(self, email:str): #TODO Data base
        return True

    def __checkPassword(self, password:str, hash:str)->bool:
        if self.__myHaschService.checkPassorwd(password, hash):
            return True
        return False

    def verifyConnect(self, mail:str,password:str, hash:str)->bool:
        if self.__checkEmail(mail) & self.__checkPassword(password, hash):
            return True
        return False