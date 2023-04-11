

"""
Write a Python class,
MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.
Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type
If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
"""

class MedPlus:
    def __init__(self,Name:str,Batch_Number:int,Price:float):
        self.Name = Name
        self.Batch_Number= Batch_Number
        self.Price= Price
    def set_Name(self, Name:str):
        self.Name = Name
    def set_Batch_Number(self, Batch_Number:int):
        self.Batch_Number= Batch_Number
    def set_Price(self, Price:float):
        self.Price= Price
    
    def get_Name(self) -> str:
        return self.Name
    
    def get_Batch_Number(self) -> int:
        return self.Batch_Number
    
    def get_Price(self) -> float:
        return self.Price
Medicine= MedPlus("Pandrop",25,14.22)
print(Medicine.get_Name())
Medicine.set_Price(50.90)
print(Medicine.get_Price())