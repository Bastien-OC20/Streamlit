from ast import Import # TODO ???
import pandas as pd

import Entity.User as User

class UserRepositoryForFind:

    # __df: pd.DataFrame
    
    def __init__(self) -> None:
        self.__df = pd.read_csv("../../../DataBase/user.csv")

    
    def findAll(self)->list:
        listObject= list()
        repositoryList = [self.__df["id"]]
        for x in range(0,len(repositoryList[0])):
            listObject.append( User(repositoryList[0][x]))
        return listObject
    
    def findBy(self,search:list)->list:
        listObject= list()
        df = self.__df[self.__df[search[0]]==search[1]]
        df=df.reset_index()
        repositoryList = [df["id"]]
        for x in range(0,len(repositoryList [0])):
            listObject.append( User(repositoryList[0][x]))
        return listObject

    def findOneBy(self,search:list)->User:
        df = self.__df[self.__df[search[0]]==search[1]]
        df=df.reset_index()
        repositoryList = [df["id"]]
        return  User(repositoryList[0][0])