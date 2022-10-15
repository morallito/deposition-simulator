
import numpy as np
import random

class  BalisticDeposition():

    def __init__ (self, max_height:int, surface_lenght:int):
        try:
            self.__height = int(max_height)
            self.__lenght = int(surface_lenght)
            self.__surface = np.zeros(self.__lenght).tolist()
            self.__matrix = np.zeros((self.__height,self.__lenght)).tolist()
            self.__is_simulated = False
        except ValueError as ve:
            raise ValueError(f'max_height and surface_lenght should be <int> and <int> not { type(max_height) } and {type(surface_lenght)}') from ve
        if (surface_lenght < 3 ):
            raise ValueError(f'Surface Length should be bigger than 3')

    def __stop_criteria(self, value) ->bool:
        return True if value == self.__height else False

    def __where_should_attatch(self, number):
        if (number == 0):
            if (self.__surface[number+1] > self.__surface[number]):
                self.__surface[number] = self.__surface[number+1]
                return self.__surface[number]
            else:
                self.__surface[number] += 1
                return self.__surface[number]
        elif (number == self.__lenght-1):
            if (self.__surface[number-1] > self.__surface[number]):
                self.__surface[number] = self.__surface[number-1]
                return self.__surface[number]
            else:
                self.__surface[number] += 1
                return self.__surface[number]
        else: 
            comparation = self.__surface[number-1] if (self.__surface[number-1] > self.__surface[number+1]) else self.__surface[number+1]
            if (comparation > self.__surface[number]):
                self.__surface[number] = comparation
                return self.__surface[number]
            else:
                self.__surface[number] += 1
                return self.__surface[number]

    def __deposit_block(self, number):
        height  =    int(self.__where_should_attatch(number))
        print(height)
        print(number)
        self.__matrix[height][number] = 1

    def simulate(self) -> bool:
        stop = False
        while stop != True:
            random_place = random.randint(0,self.__lenght -1)
            stop = self.__stop_criteria(self.__surface[random_place] +1)
            if stop != True:
                self.__deposit_block(random_place)

        self.__is_simulated = True
        return self.__is_simulated

    def get_output_matrix(self):
        return self.__matrix if self.__is_simulated== True else None



