class Player:
    def __init__(self,name) : #avoir un nom
        self.nom = name
    
    def perdPV (self,nombre) : #score de la personne 
        self.score = nombre
    
    def prendreChanson (self,Chanson0,Chanson1,Chanson2,Chanson3,Chanson4): #prendre une musique 
        self.__Chanson0 = Chanson0
        self.__Chanson1 = Chanson1
        self.__Chanson2 = Chanson2
        self.__Chanson3 = Chanson3
        self.__Chanson4 = Chanson4
    
    def BestScoreTotal(self,nombre): #avoir son meilleur score des musiques au total
        self.BestScoreTotal = nombre
    
    def BestScoreChansons(self,nombre): #avoir son meilleur score par musique
        self.BestScoreChansons = nombre
    
    def BestScoreMoyenne(self,nombre): #avoir son score moyen des musiques au total
        self.BestScoreMoyenne = nombre

class Karaoke:
    def __init__(self,name) : #avoir le nom de la musique
        self.nomChanson = name

    def NbrPlayer (self,nombre) : #avoir le nombre de joueurs
        self.NbrPlayer = nombre
    
    def BestScore (self,nombre1) : #avoir le meilleur score
        self.BestScore = nombre1
    
    def NbrChanson(self,nombre2) : #avoir le numéro de la musique utilisé
        self.NbrChanson = nombre2
