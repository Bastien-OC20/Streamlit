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
        # print("enter __checkPassword")
        # print(trs.password)
        # print(user.mot_de_passe)
        if not self.__myHaschService.checkPassorwd(trs, user.mot_de_passe):
            # print("__checkPassword NOK")
            return False
        # print("connectionService __checkPassword OK")
        return True

    def verifyConnect(self, trs:transiant_connection)->User:
        # print(trs)
        user = self.__myUserService.FindUserByEmail(trs)
        # print(user.__dict__)

        if user is None:
            return None
        if not self.__checkPassword(trs, user):
            return None
        return user