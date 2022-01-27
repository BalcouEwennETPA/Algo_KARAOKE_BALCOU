class Player:
    def __init__(self,name) : 
        self.nom = name
    
    def perdPV (self,nombre) :
        self.score = nombre
    
    def prendreChanson (self,Chanson0,Chanson1,Chanson2,Chanson3,Chanson4):
        self.__Chanson0=Chanson0
        self.__Chanson1=Chanson1
        self.__Chanson2=Chanson2
        self.__Chanson3=Chanson3
        self.__Chanson4=Chanson4
    
    def BestScoreTotal(self,nombre):
        self.BestScoreTotal = nombre
    
    def BestScoreChansons(self,nombre):
        self.BestScoreChansons = nombre
    
    def BestScoreMoyenne(self,nombre):
        self.BestScoreMoyenne = nombre

class Karaoke:
    def __init__(self,name) :
        self.nomChanson = name
    def NbrPlayer (self,nombre) :
        self.NbrPlayer = nombre
    def BestScore (self,nombre1) :
        self.BestScore = nombre1
    def NbrChanson(self,nombre2) :
        self.NbrChanson = nombre2
