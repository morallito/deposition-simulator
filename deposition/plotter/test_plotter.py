from plotter import Plotter
import numpy as np
import pytest
import os
import time

def test_plotter_init_success ():
    p = Plotter(10,10)
    assert type(p) is Plotter

def test_plotter_init_fail ():
    with pytest.raises(ValueError):
        p = Plotter(10, 'a')

def test_matrix_setter ():
    plt_tst = Plotter(10,10)
    matrix = np.identity(10)
    results = plt_tst.set_matrix(matrix)
    assert results == True

def test_matrix_setter_fail_len ():
    plt_tst = Plotter(10,9)
    matrix = np.identity(10)
    with pytest.raises(IndexError):
        results = plt_tst.set_matrix(matrix)

def test_plotting():
    pltt = Plotter(10,10)
    matrix = np.identity(10, int)
    pltt.set_matrix(matrix)
    path = os.getcwd()
    fig_name = str(time.time())
    path = os.path.join(path,fig_name)
    pltt.plot(path)
    fig_exists = os.path.isfile(path + '.png')
    os.remove(path + '.png')
    assert fig_exists == True
    
def test_matrix_setter_fail ():
    with pytest.raises(ValueError):
        plt_tst = Plotter(10,10)
        matrix = np.identity(10)
        matrix[9][9] = 3
        plt_tst.set_matrix(matrix)
