# class Building:
#     def __init__(self,f = 1,w = 1):
#         self.floor = f
#         self.windows = w
# b1 = Building()
# b2 = Building(2,16)
# print(b1)
# print(b2.windows)


# class Human:
#     def __init__(self,name,surname,age,nickname):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.nickname = nickname
#     def speak(self,mstr = "hello everyone"):
#         print(mstr)
#     def __str__(self):
#         return (f"Name is {self.name} surname is {self.surname} age {self.age}, acakan {self.nickname}")
#     def get_older(self):

#         self.age += 10

# h1 = Human("Travis","Scott",33,"Staright_up")
# h2 = Human("Gugush","Tadevosayn",64,"jxer Gugush")

# # h1.speak()
# # h1.speak("good bye")
# print(h1)
# # h1.get_older()
# # print(h1.age)

# h2.speak()
# print(h2)


# class Cars:
#     def __init__(self,make,model,color,year:int,engine):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.engine = engine
#     def show(self,cars = " we are best cars"):
#         print(cars)
#     def __str__(self) -> str:
#         return f" The make of this car {self.make} the model of this car {self.model},The color of this car {self.color},The year of this car {self.year},the engine of this car {self.engine}"
#     def beeb(self):
#         print(f"{self.model} is beeeeeeeeb")
    
#     def drift(self):
#         print(f"this {self.make} is awesome drifting car")
#     def change_color(self,new_color):
#         self.color = new_color
#     def do_youngest(self,how_many_year):
#         self.year = self.year + how_many_year


# infiniti = Cars("INFINITI","FX35","WET BLACK",2006,"V6 ATMOSPHERE")
# audi = Cars("Audi","RS6 Avant","Electrick Blue",2016,"4.2 V8 Quattro")
# print(audi)
# audi.beeb()
# audi.drift()
# audi.change_color("green")
# infiniti.do_youngest(10)
# print(infiniti)



# class Animal:
#     def __init__(self,name,breed,age:int,gender,voice):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.gender = gender
#         self.voice = voice

#     def sounds(self):
#         print(f"my sounds is {self.voice}")

#     def __str__(self):
#         return f"my name is {self.name} my breed is {self.breed} my age {self.age} year, my gender {self.gender} my growl sounds like this {self.voice}"
    

# cat = Animal("Barsik","british cat",4,"boy","myauuu")
# print(cat)
# print("-----------------")
# dog = Animal("zek","pitbull","3","boy","hahf")
# print(dog)



# class Car:
#     def __init__(self,marka:str=None,model:str=None,hp:int=None,color:str=None,year:int=None,isNew:bool=None):
#         self.marka = marka
#         self.model = model
#         self.hp = hp
#         self.color = color
#         self.year = year

#     def setMarka(self,marka):
#         self.marka = marka
    
#     def getMarka(self):
#         return self.marka

#     def resetMarka(self):
#         self.marka = None

#     def delMarka(self):
#         del self.marka
    
#     def setNew(self,isNew):
#         self.isNew = isNew
    
#     def getNew(self):
#         return self.isNew
    

#     def set_hp(self,hp):
#         self.hp = hp

#     def get_hp(self):
#         return self.hp

# bmw = Car()
# bmw.set_hp(333)
# bmw.setMarka("bmw")
# bmw.setMarka("audi")
# bmw.resetMarka()

# print(bmw.get_hp())

# year = int(input())
# car = Car(year=year)

# car.setNew(year > 2010)

# print(car.getNew())



# class BanckAccount:
#     def __init__(self,name,balance,passport):
#         self.__name = name 
#         self.__balance = balance
#         self.__passport = passport

#     def print_public_data(self):
#             self.__print_private_data()

#     def __print_protected_data(self):
#         print(self.__name,self.__balance,self.__passport)

#     def __print_private_data(self):
#         print(self.__name,self.__balance,self.__passport)




# account1 = BanckAccount("Travis",100000,34125678)
# account1.print_public_data()
# print(account1._BanckAccount__balance)


        
# class Car:
#     def __init__(self,marka,model,year):
#         self.__marka = marka
#         self.__model = model
#         self.__year = year

#     def __setMarka__(self,marka):
#         self.__marka = marka
        
#     def __GetMarka__(self):
#         return self.__marka
    
#     def __setModel__(self,model):
#         self.__model = model

#     def __GetModel__(self):
#         return self.__model
    
#     def __serYear__(self,year):
#         self.__year = year
    
#     def __getYear__(self):
#         return self.__year
    
# auto = Car("Audi","rs6",2011)
# auto.__setMarka__("BMW")
# auto.__setModel__("X5")
# auto.__serYear__(2010)
# print(auto.__GetModel__(),auto.__GetMarka__(),auto.__getYear__())


# class CarBavaria:
#     def __init__(self,marka,model,year):
#         self.__marka = marka
#         self.__model = model
#         self.__year = year

#     @property
#     def marka(self):
#         return self.__marka

#     @marka.setter
#     def marka(self,marka):
#         self.__marka = marka

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self,model):
#         self.__model = model

#     @property
#     def year(self):
#         return self.__year
    
#     @year.setter
#     def year(self,year):
#         self.__year = year

   
    
# auto = CarBavaria("audi","rs6",2016)
# print(auto.marka)
# print(auto.model)
# print(auto.year)
# auto.model = "vilis"
# print(auto.model)











# class Bavarian_Motors:
#     def __init__(self,Marka,Model,Year,Hp,Color,Engine):
#         self.__Marka = Marka
#         self.__Model = Model
#         self.__Year = Year
#         self.__Hp = Hp
#         self.__Color = Color
#         self.__Engine = Engine
#     @property
#     def Marka(self):
#         return self.__Marka
        
#     @Marka.setter
#     def Marka(self,Marka):
#         self.__Marka = Marka

#     @property
#     def Model(self):
#         return self.__Model
    
#     @Model.setter
#     def Model(self,Model):
#         self.__Model = Model

#     @property
#     def Year(self):
#         return self.__Year
    
#     @Year.setter
#     def Year(self,Year):
#         self.__Year = Year

#     @property
#     def Hp(self):
#         return self.__Hp
    
#     @Hp.setter
#     def Hp(self,Hp):
#         self.__Hp = Hp

#     @property
#     def Color(self):
#         return self.__Color
    
#     @Color.setter
#     def Color(self,Color):
#         self.__Color = Color

#     @property
#     def Engine(self):
#         return self.__Engine
    
#     @Engine.setter
#     def Engine(self,Engine):
#         self.__Engine = Engine

# Cars = Bavarian_Motors('Audi','RS6',2015, "410 Hp", "Blue","V6 Quattro")
# print(Cars.Marka,Cars.Model,Cars.Color,Cars.Year,Cars.Hp,Cars.Engine)
# Cars.Hp = "560 Hp"
# print(Cars.Hp)
# Cars.Color = "Red"
# print(Cars.Color)

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance 
    

#     def set_balance(self,value ):
#         if not isinstance(value,(int,float)):
#             raise ValueError ("balancy bdi tiv exni dalbun")
#         self.__balance = value
    
#     def delete_balance(self):
#         del self.__balance





#     my_balance = property()

#     my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)

# a = BankAccount("Vasya",13333)
# a.my_balance = 1000
# print(a.get_balance())



# class Rectangle:
#     def __init__(self,l = 1, w =  1) -> None:
#         self.lenght = l
#         self.width = w 

#     def __add__(self,other):
#         r3 = Rectangle(self.lenght + other.lenght,other.width)
#         return r3
    

#     def arrea(self):
#         return (self.lenght * self.width)
    
#     def perimetr(self):
#         return(self.lenght + self.width) * 2

#     def __str__(self):
#         return f"lenght is {self.lenght} widht is {self.width}"
        
# r1 = Rectangle(3,5)
# r2 = Rectangle(3,4)
# print(r1.perimetr())


         
# class Number:
#     def __init__(self, n):
#         self._num = n


#     def __add__(self, other):
#         n3 = Number(self._num + other._num)
#         return n3
    
    
#     def __sub__(self,other): 
#         r2 = Number (self._num - other._num)
#         return r2
    
#     def __mul__(self,other):
#         r4 = Number(self._num * other._num)
#         return r4
    
#     def __truediv__(self,other):
#         r5 = Number(self._num / other._num)
#         return r5

#     def __str__(self):


#         return f" _num {self._num}"
    















# class MY_List:
#     def __init__(self, *values):
#         if values is None:
#             self.values = []
#         else:
#             self.values = list(values)

#     def __len__(self):
#         return len(self.values)
    
#     def __reversed__(self):
#         return self.values[::-1]
    
#     def __pop__(self):
#         value = self.values[-1]
#         del self.values[-1]
#         return value
    
#     def __append__(self,value):
#         return self.values + [value]
    
#     def __extend__(self,value):
#         return self.values + value.values
    

#     def __remove__(self):
#         del self.values[0]
#         return self.values
    

#     def __clear__(self):
#         self.values = []
#         return []
    
#     def __count__(self):
#         count = 0
#         for i in self.values:
#             count += i
#         return count
        
        
#     def __bubble_sort__(self):
        

#         for i in range(len(self.values)):
            
#             for j in range(0,len(self.values)-i - 1):
#                 if self.values[j] > self.values[j+1]:
#                     temp = self.values[j]

#                     self.values[j] = self.values[j+1] 
#                     self.values[j+1] = temp

#         return self.values
    

#     def __str__(self):
#         return f"{self.values}"

# l2 = MY_List(9,8,7,6,5,4)
# l3 = MY_List(1,2,4,5)

# print(l2)
    


# class Roman_to_int:
#     def roman_to_int(self,s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
#                 int_val += rom_val[s[i]]-2 * rom_val[s[i-1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val
    
# print(Roman_to_int().roman_to_int(''))





# class Person:
    
#     def __init__(self,fio,old,ps,weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)

#         self.__fio = fio.split()
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
  

#     @classmethod
#     def verify_fio(cls,fio):
#         if type(fio) != str:
#             raise TypeError ("FIO Must Be A String")


#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError ("Wrong Format FIO")
        

#     @classmethod
#     def verify_old(cls,old):
#         if type(old) != int or old < 14 or old > 98:
#             raise TypeError ("OLD Must Be a Integer from [14; 98]")
        


#     @classmethod
#     def verify_weight(cls,weight):
#         if type(weight) != int or weight < 38:
#             raise TypeError ("Weight Must Be a Float Integer from 38 and higher")
        

#     @classmethod
#     def verify_ps(cls,ps):
#         if type(ps) != int:
#             raise TypeError ("The  Characters Must Be a Digits")
        
       

#     @property
#     def fio(self):
#         return self.__fio
    
#     @fio.setter
#     def fio(self,fio):
#         self.verify_fio(fio)
#         self.__fio = fio

#     @property
#     def old(self):
#         return self.__old
    
#     @old.setter
#     def old(self,old):
#         self.verify_old(old)
#         self.__old = old

#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.verify_weight(weight)
#         self.__weight = weight
    
#     @property
#     def ps(self):
#         return self.__ps
    
#     @ps.setter
#     def ps(self,ps):
#         self.verify_ps(ps)
#         self.__ps = ps


# person = Person("Asoyan Lyudvig Ruslani",25,3778097890,63)
# print(person.__dict__)



    
        

# class Stack:
#     def __init__(self):
#      self._items = []
     


#     def isempty(self):
#         return self._items == []
    
#     def isfull(self):
#        return len(self._items)
     
#     def push(self,item):
#        self._items.append(item)
        
#     def pop(self):
#        return self._items.pop()
    
    
#     def get_top(self):
#        return self._items[-1]


# s = Stack()







# class Number:
#     def __init__(self, n):
#         self._num = n


#     def __add__(self, other):
#         result = Number(self._num + other._num)
#         return result
    
    
#     def __sub__(self,other): 
#         result = Number (self._num - other._num)
#         return result
    
#     def __mul__(self,other):
#         result = Number(self._num * other._num)
#         return result
    
#     def __truediv__(self,other):
#         result = Number(self._num / other._num)
#         return result

#     def __str__(self):


#         return f" _num {self._num}"
    




# class Unamber(Number):
#     def __init__(self,n):
#         super().__init__(n)

#     def only_pos(self):
#         if self._num > 0:
#             return True
#         else:
#             return False
    
#     def __mul__(self, other):
#         if self.only_pos() and other.only_pos():
#             result = Unamber(self._num * other._num)
#             return result
#         else:
#             return "Cannot multiply non-positive numbers"
    
#     def __add__(self, other):
#         if self.only_pos() and other.only_pos():
#             result = Unamber(self._num + other._num)
#             return result
#         else:
#             return "Cannot add non-positive numers"

#     def __sub__(self, other):
#         if self.only_pos() and other.only_pos():
#             result = Unamber(self._num - other._num)
#             return result
#         else:
#             return "Cannot sub non-positive numers"
        
#     def __truediv__(self, other):
#         if self.only_pos() and other.only_pos():
#             result = Unamber(self._num / other._num)
#             return result
#         else:
#             return "Cannot div non-positive numers"

# num1 = Unamber(-6)
# num2 = Unamber(8)
# print(num1 / num2)



# unittest kardal nayel 