from unicodedata import name


class Player:   #declaration de la classe
    def __init__(self,name) : #avoir un pseudo
        self.nom = name
    def score (self,nombre) : #score de la personne
        self.score = nombre
    def prendreChanson (self,Chanson0,Chanson1,Chanson2,Chanson3,Chanson4): #prendre une chanson
        self.__Chanson0=Chanson0
        self.__Chanson1=Chanson1
        self.__Chanson2=Chanson2
        self.__Chanson3=Chanson3
        self.__Chanson4=Chanson4
