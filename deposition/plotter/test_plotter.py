from plotter import Plotter
import numpy as np
import pytest

def test_plotter_init_success ():
    p = Plotter(10,10)

def test_plotter_init_fail ():
    with pytest.raises(ValueError):
        p = Plotter(10, 'a')

def test_matrix_setter ():
    plt_tst = Plotter(10,10)
    matrix = np.identity(10)
    results = plt_tst.set_matrix(matrix)
    assert results == True
    
def test_matrix_setter_fail ():
    with pytest.raises(ValueError):
        plt_tst = Plotter(10,10)
        matrix = np.identity(10)
        matrix[9][9] = 3
        plt_tst.set_matrix(matrix)
