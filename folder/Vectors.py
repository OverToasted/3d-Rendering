import math as m
import pynput as pt

class vector:
    def __init__(self,*args):
        """Accepts any type for arguemnents but tuples are split up so that
           its elements become elements of the vector
           Last arguement should be row or column"""
        #alows arbitary num of arguements
        list1 = []
        i = 0
        length = len(args)
        for value in args:
            if type(value) == tuple:
                length += len(list(value)) - 1
                for index, j in enumerate(list(value)):
                    if index != len(value) and index + i != length - 1:
                        setattr(self,'e' + str(index + i),j)
                        #print('e' + str(index + i) + 'tuple' + str(args))
                    if index == len(value) - 1 and args[-1] == value:
                        setattr(self,'pose',j)
                        #print('pose' +str(j) +str(args))
                        #determines if row or column vector
                        #gives key as pose to last element of tuple if tuple is last arg
                i += len(list(value))
            else:
                if i != length - 1:
                    setattr(self,'e' + str(i),value)
                    #print('e' + str(i) + 'nontuple' + str(args))
                if i == length - 1:
                    setattr(self,'pose',value)
                    #print('pose' +str(value) +str(args))
                i += 1
                #determines if column or row vector


        if self.pose != 'row' and self.pose != 'column':
            self.pose = 'row'
            #sets default pose to row if row or column not inputed

            
        for j in range(len(self.__dict__.items())):
            if self.__dict__.get('e' + str(j)) != None:
                list1.append(self.__dict__['e' + str(j)])
        list1.append(self.__dict__['pose'])
        self.comp = list1
        #defines .comp to give vector as a list

        
    def trans(self):
        list1 = self.__dict__
        list2 = []
        if self.pose == 'row':
            for j in range(len(self.__dict__.items())):
               if self.__dict__.get('e' + str(j)) != None:
                   list2.append(list1['e' + str(j)])
            list2.append(list1['pose'])
            list2[-1] = 'column'
            return vector(tuple(list2))
#defines the vector class + methods



class matrix:
    def __init__(self, *args: vector | tuple):
        #alows arbitary num of arguements
        list1 = []
        i = 0
        vectarg = []
        length = len(args)
        for value in args:
            if type(value) == tuple:
                vectarg = value
                length += len(list(value))
                for index, j in enumerate(list(value)):
                    if index != len(value) and index + i != length - 1:
                        setattr(self,'e' + str(index + i),j)
                        #print('e' + str(index + i) + 'tuple' + str(args))
                    
                i += len(list(value))
            else:
                if i != length - 1:
                    setattr(self,'e' + str(i),value)
                    #print('e' + str(i) + 'nontuple' + str(args))
                i += 1
                #determines if column or row matrix
                
        for j in range(len(self.__dict__.items())):
            if self.__dict__.get('e' + str(j)) != None:
                list1.append(self.__dict__['e' + str(j)])
        list1.append(self.__dict__['pose'])
        self.comp = list1
        #defines .comp to give vector as a list

  #  def trans(self):
       # list1 = self.__dict__
       # list2 = []
       # list3 = []
       # for j in range(len(self.__dict__.items())):
              # if self.__dict__.get('e' + str(j)) != None:
                   #list2.append(list1['e' + str(j)])
        


        



def mag(v):
    sumand = 0
    for index, i in enumerate(v.comp):
        if index != len(v.comp)-1:
            sumand += i**2
    return m.sqrt(sumand)
#gives the magnitude of the vector

       
def dot(v,u):
    sumand = 0
    if v.pose == u.pose and v.pose == 'row:
        for i in range(len(v.comp)):
            if v.__dict__.get('e' + str(i)) != None:
                sumand += v.__dict__['e' + str(i)]*u.__dict__['e' + str(i)]
            return sumand
    else:
        return 'DNE, poses do not match'
#gives the dot product


def angle(v,u):
    return m.acos(dot(v,u)/(mag(v)*mag(u)))
#gives the angle between two vectors

x1v = vector(1,0,0)
y1v = vector(0,1,0)
z1v = vector(0,0,1)
mat = matrix(x1v,y1v,z1v,'row')
print(mat.e1.e1)
print(mat.comp)
#gives 1 vectors
