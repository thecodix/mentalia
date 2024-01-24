import pytest

from examenes.models import Carrera


@pytest.mark.django_db
def test_carrera_model():
    nombre_carrera = "Psicología"
    carrera = Carrera.objects.create(nombre=nombre_carrera)
    assert carrera.nombre == nombre_carrera
    assert str(carrera) == nombre_carrera
