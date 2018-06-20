import math

class KNeighbors :
    instances = []
    class_num = 0
    class_value = []
    var_names = list()
    k = 0

    #Init class with .csv file
    #Archivo -> Path of .csv file
    #Class_num -> Num of class column in .csv file

    def __init__(self, archivo, class_num):
        self.class_num = class_num
        #Reading .csv
        with open(archivo, "r") as  datos:
            instance = datos.read().splitlines()
            #Saving var names
            self.var_names = instance[0].split(",")
            instance.pop(0)

            #Saving instances
            for i in instance :
                line = i.split(",")
                self.class_value.append(line[self.class_num])
                del line[class_num]

                for index in range(len(line)):
                    line[index] = float(line[index])
                self.instances.append(line)

    #Set K value, if we know best K Value for model
    def setK (self, num) :
        self.k = num

    def classify (self, tuple1) :

        if self.k == 0:
            print("Value of K = 0, please set k value before try to short out a new instance")
            return 0

        if len(tuple1) != len(self.var_names) - 1 :
            print("Please, give an instance with same number of variables than instances in the model")
            return 0

        kneighbour_index = list(range(0, self.k))

        for i in range(len(kneighbour_index)):
            kneighbour_index[i] = [9999.9, 0]

        for i in range(len(self.instances)):
            dist = self._distance_(self.instances[i], tuple1)
            mayor_dist = kneighbour_index[self.k - 1]
            mayor_dist = mayor_dist[0]

            if dist < mayor_dist:
                kneighbour_index[self.k - 1] = [dist, i]
                kneighbour_index.sort()

        count = {}
        for i in range(len(kneighbour_index)):
            cla = kneighbour_index [i]
            cla = cla[1]
            cla = self.class_value[cla]
            count.setdefault(cla, 0)
            count[cla] += 1
        print "\n\nClasses of the closest K Values ", count

        final_class = ""
        cont = 0
        for cl in count :
            if count[cl] > cont:
                cont = count[cl]
                final_class = cl

        print "Instance has been classified as ", cl

    #Function that calculates the distance (Manhattan) between two instances
    def _distance_(self,tuple1,tuple2):
        distance = 0
        cont = 0
        while cont < len(self.var_names):
            if cont != self.class_num :
                distance = distance + pow((tuple1[cont] - tuple2[cont]),2)
            cont = cont + 1
        distance = math.sqrt(distance)
        return distance


