class Calculator:
    def __init__(self) -> None:
        self.__value = 0

    def value(self):
        return self.__value
    
    def add(self, number):
        self.__value += number