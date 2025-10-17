class Planets:
    def __init__(self,id ,name , description , atmosphere):

        self.id = id
        self.name = name
        self.description = description
        self.atmosphere = atmosphere
planets = [
            Planets(1 , "Earth" ,"Our home planet and the only one known to support life." , "True"),
            Planets(2 , "Mercury" ,"Closest to the sun, it has extreme temperature fluctuations and a thin atmosphere." , "False"),
            Planets(3 , "Venus" , "The hottest planet due to its thick, toxic atmosphere." , "False"),
            Planets(4 , "Mars" , "Known as the Red Planet, it features giant volcanoes and dry riverbeds.", "False")
        ]
