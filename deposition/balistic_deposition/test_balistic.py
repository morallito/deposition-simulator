from balistic_deposition import BalisticDeposition
import random
import numpy as np
import pytest



def test_create_fail():
    height = random.randint(1,100)
    with pytest.raises(ValueError):
        rds = BalisticDeposition(max_height = height, surface_lenght='a')

def test_create_fail_len ():
    height = random.randint(1,100)    
    with pytest.raises(ValueError):
        rds = BalisticDeposition(max_height = height, surface_lenght=2)

def test_create():
    height = random.randint(1,100)   
    lenght = random.randint(3,200) 
    ds = BalisticDeposition(max_height = height, surface_lenght=lenght)

def test_get_matrix_fail():
    height = random.randint(1,100)   
    lenght = random.randint(3,200) 
    ds = BalisticDeposition(max_height = height, surface_lenght=lenght)
    results = ds.get_output_matrix()
    assert results == None

def test_get_matrix():
    height = random.randint(1,100)   
    lenght = random.randint(3,200) 
    ds = BalisticDeposition(max_height = height, surface_lenght=lenght)
    ds.simulate()
    results = ds.get_output_matrix()
    lenghtresult = len(results[0])
    heightresult = len(results)
    assert lenght == lenghtresult and height == heightresult


