import math
class KNeighbors :
    instances = []
    class_num = 0
    k = 0

    #Init class with .csv file
    #Archivo -> Path of .csv file
    #Class_num -> Num of class column in .csv file
    def __init__(self, archivo, class_num):
        self.class_num = class_num

        with open(archivo, "r") as  datos:
            instance = datos.read().splitlines()
            instance.pop(0)
            for i in instance :
                self.instances.append(i.split(","))

    #Set K value, if we know best K Value for model
    def setK (self, num) :
        self.k = num


    def _distance_(self,tuple1,tuple2):
        distance = 0
        cont = 0
        while cont < len(self.var_names):
            if cont != self.class_num :
                distance = distance + pow((tuple1(cont) - tuple2(cont)),2)
            cont = cont + 1
        distance = math.sqrt(distance)
        return distance


