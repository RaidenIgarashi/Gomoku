
class player():
    def __init__(self):
        self.all_line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
        self.all_columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.position_lst=[]
        self.lock_places = []
#translateLocation recebe uma posição composta por uma letra e um número, e traduz para uma coordenada apenas com números
    def translateLocation(self, location=str):
        converter = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19}
        locationtranslate = []
        line = converter[location[0]]
        locationtranslate.append(line)
        if len(location) > 2:
            column = location[1] + location[2]
            column = int(column)
            locationtranslate.append(column)
        else:
            column = location[1]
            column = int(column)
            locationtranslate.append(column)
        return locationtranslate
    
  

    
