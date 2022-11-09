import random
import numpy as np


class RandomDeposition ():
    def __init__ (self, max_height:int, surface_lenght:int):
        try:
            self.__height = int(max_height)
            self.__lenght = int(surface_lenght)
            self.__surface = np.zeros(self.__lenght).tolist()
            self.__is_simulated = False
            self.__rugosity_vector = []
        except ValueError as ve:
            raise ValueError(f'max_height and surface_lenght should be <int> and <int> not { type(max_height) } and {type(surface_lenght)}') from ve

    def __stop_criteria(self, value) ->bool:
        return True if value == self.__height else False

    def __should_calculate_rugosity(self, i):
        return True  if (i%self.__lenght) == 0 else False

    def __calculate_rugosity(self):
        self.__rugosity_vector.append(np.var(self.__surface))


    def simulate(self) -> bool:
        stop = False
        count = 0
        while stop != True:
            rtandom_place = random.randint(0,self.__lenght -1)
            self.__surface[rtandom_place] +=1
            stop = self.__stop_criteria(self.__surface[rtandom_place])
            count+=1
            if (self.__should_calculate_rugosity(count)):
                self.__calculate_rugosity()

        self.__is_simulated = True
        return self.__is_simulated


    def get_output_matrix(self) -> bool:
        matrix =[]
        for lenght_filled in self.__surface:
            column = []
            for i in range(self.__height):
                column.append(1 if i < lenght_filled-1  else 0)
            matrix.append(column)
        output_matrix = np.matrix.transpose(np.array(matrix))
        return(output_matrix.tolist())

    def get_rugosity(self):
        return self.__rugosity_vector if self.__is_simulated else None

    def get_output_surface (self): 
        return self.__surface if self.__is_simulated == True else None 