import pytest
import random
from relaxed_deposition import RelaxedDeposition


def test_create_fail_nonint():
    height = random.randint(1,100)
    with pytest.raises(ValueError):
        rds = RelaxedDeposition(max_height = height, surface_lenght='a')

def test_create_fail_short_lenght():
    height = random.randint(1,100)
    with pytest.raises(ValueError):
        rds = RelaxedDeposition(max_height = height, surface_lenght=2)    

def test_simulate_job(): 
    height = random.randint(1,100)
    lenght = random.randint(3,20)
    rds = RelaxedDeposition(max_height = height, surface_lenght = lenght)
    result = rds.simulate()
    assert result == True

def test_get_out_matrix():
    height = random.randint(1,100)
    lenght = random.randint(3,20)
    rds = RelaxedDeposition(max_height = height, surface_lenght = lenght)
    rds.simulate()
    results = rds.get_output_matrix()
    output_heigth = len(results)
    output_len = len(results[0])
    assert (output_heigth == height and output_len == lenght) == True

def test_get_surface_success():
    height = random.randint(1,100)
    lenght = random.randint(3,20)
    rds = RelaxedDeposition(max_height = height, surface_lenght = lenght)
    rds.simulate()
    result = len(rds.get_output_surface())
    assert (lenght == result) == True

def test_get_surface_not_simulated():
    height = random.randint(1,100)
    lenght = random.randint(3,20)
    rds = RelaxedDeposition(max_height = height, surface_lenght = lenght)
    result = rds.get_output_surface()
    assert result == None