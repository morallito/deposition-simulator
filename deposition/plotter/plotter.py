import matplotlib.pyplot as plt
import numpy as np

class Plotter ():
    """
    Plotter - A class that receives a binary matrix M (n x m)
    and provides plotting optios to save it as images. 
    """

    def __init__(self,num_lines:int,num_columns:int) -> bool:
        try:
            self.__num_lines = int(num_lines)
            self.__num_columns = int(num_columns)
        except ValueError :
            raise (ValueError("num_lines and num_columns should be integers"))
        return True

    def __is_valid_item (self, num:int) -> bool:
        """
        Checks if the matrix item are valid (1 or 0)
        """
        return True if (num == 1 or num ==0 ) else False


    def set_matrix(self, A) -> bool:
        for row in A:
            for item in row:
                if self.__is_valid_item(item):
                    pass
                else:
                     raise ValueError(f'Matrix item should be 1 or 0, founded {item}')
        self.__matrix = A 
        return True

    def plot(self):
        matrix = np.identity(10)
        matrix[0][0] = 0
        inverted_matrix = matrix[::-1]
        plt.matshow(inverted_matrix,cmap='gray', vmin=1, vmax=0)
        plt.axis(False)
        plt.show()
        print(inverted_matrix)


if __name__ == "__main__":
    pltt = Plotter(3,3)
    matrix = np.identity(100, int)
    matrix[99][99] = 2
    print(pltt.set_matrix(matrix))