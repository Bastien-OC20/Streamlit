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
        print("__checkPassword")

        if not self.__myHaschService.checkPassorwd(trs, user.mot_de_passe):
            return False
        print("fin check password")
        return True

    def verifyConnect(self, trs:transiant_connection)->bool:
        # user_from_trs = __myUserService.
        # print("-"*80)
        # print("le tranasiant - verifyConnect")
        # print(trs.__dict__)
        # print(trs.email)
        # print(trs.password)
        # print("-"*80)
        user_from_trs = self.__myUserService.FindUserByEmail(trs)
        if user_from_trs is None:
            return False
        if not self.__checkPassword(trs, user_from_trs):
        # if not self.__checkEmail(trs, user_from_trs) and not self.__checkPassword(trs, user_from_trs):
            return False
        print("fin verifyConnect")
        return True