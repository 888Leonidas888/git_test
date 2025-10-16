class Person:
    def __init__(self, name:str, age:int, country: str) -> None:
        self.name = name
        self.age = age
        self.country = country

    def display(self):
        return $'hi, mi name is {self.name}, has {self.age} year old and Iam {self.country}'
