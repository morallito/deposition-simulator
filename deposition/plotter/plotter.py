import matplotlib.pyplot as plt
import numpy as np


class Plotter ():
    def __init__(self,num_lines:int,num_columns:int) -> None:
        try:
            self.__num_rows = int(num_lines)
            self.__num_columns = int(num_columns)
        except ValueError as ve:
            raise (ValueError("num_lines and num_columns should be integers")) from ve
    

    def __is_valid_item (self, num:int) -> bool:
        """
        Checks if the matrix item are valid (1 or 0)
        """
        return True if (num == 1 or num ==0 ) else False



    def __invert_colors(self):
        for row in range(self.__num_rows):
            for column in range(self.__num_columns):
                self.__matrix[row][column] = 1 if self.__matrix[row][column]==0 else 0 


    def set_matrix(self, A) -> bool:
        """
        Define the matrix that will be printed.
        Checks for dimentional consistency and 
        """
        rows = len(A)
        columns = len(A[0])

        if (rows != self.__num_rows or columns != self.__num_columns):
            raise IndexError(f'A must be a matrix {self.__num_rows} by {self.__num_columns}')

        for row in A:
            for item in row:
                if self.__is_valid_item(item):
                    pass
                else:
                     raise ValueError(f'Matrix item should be 1 or 0, founded {type(item)}')
        
        self.__matrix = A 
        return True

    def plot(self, fig_name:str) -> bool:
        """
        Prints the matrix using matshow
        """
        try:
            self.__invert_colors()
            inverted_matrix = self.__matrix[::-1]
            plt.matshow(inverted_matrix,cmap='gist_yarg_r', vmin=0, vmax=1)
            plt.axis(False)
            plt.savefig(fig_name + '.png', format='png')
            plt.close()
            return True
        except Exception as e:
            raise (e)


    def plot_rugosity(self, rugosity_vector, fig_name):


        plt.title(fig_name)
        plt.xlabel("Time axis")
        plt.ylabel("Rugosity axis")
        plt.plot(range(len(rugosity_vector)), rugosity_vector, color ="blue")
        plt.savefig(fig_name + '.png', format='png')