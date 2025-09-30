import pytest
import Calculadora


def test_sumar():
    assert Calculadora.sumar(2,4) == 6

def test_division_por_cero():
    with pytest.raises(ValueError):
        Calculadora.dividir(10,0)

@pytest.mark.parametrize('a,b,esperado',[
    (2,5,7), #numero posiivos
    (-4,-2,-6), # numeros negativos
    (0,0,0) # numero ceros
])
def test_sumar_varios(a,b,esperado):
    assert Calculadora.sumar(a,b)  == esperado


def test_restar_con_fixture(numeros):
    a,b = numeros
    assert Calculadora.restar(a,b) == 0

def test_sumar_con_fixture(numeros):
    a,b= numeros
    assert Calculadora.sumar(a,b) == 10 



@pytest.mark.listo
def test_sumar_listo():
    assert Calculadora.sumar(1,3) == 4

def test_estructura_dicc():
    
    data = {'nombre':'luisa','edad': 34}

    assert 'nombre' in data
    assert 'edad' in data

    assert isinstance(data['nombre'], str)
    assert isinstance(data['edad'], int)

def test_estrutura_list():
    
    items = [{'id':1,' id':2}]

    assert all('id' in item for item in items)
