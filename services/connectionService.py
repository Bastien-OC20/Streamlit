from dataclasses import dataclass
from services.haschService import haschService
from services.UserService import UserService
from services.haschService import haschService
from Entity.User import User
from Transiant import transiant_connection


@dataclass
class ConnectService:

    __myUserService = UserService()
    __myHaschService = haschService()

    # def __checkEmail(self, trs:transiant_connection, user:User): #TODO Data base
    #     print("__checkEmail")
        
    #     user_from_trs = self.__myUserService.FindUserByEmail(trs)
    #     print("user finded : ")
    #     print(user_from_trs)
    #     if user_from_trs is None:
    #         return False
    #     print("fin check email")
    #     return True

    def __checkPassword(self, trs:transiant_connection, user:User)->bool:
        if not self.__myHaschService.checkPassorwd(trs, user.mot_de_passe):
            return False
        return True

    def verifyConnect(self, trs:transiant_connection)->bool:
        user_from_trs = self.__myUserService.FindUserByEmail(trs)
        if user_from_trs is None:
            return False
        if not self.__checkPassword(trs, user_from_trs):
            return False
        return True