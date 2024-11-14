import data
import sender_stand_request

from sender_stand_request import response


def get_kit_body(name):
    current_kit = data.kit_body.copy()
    current_kit["name"] = name
    return current_kit
response_name = get_kit_body("A")
print(f"Se trajo el diccionario correcto" + str(response_name))

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.new_client(kit_body)
    assert kit_response.status_code == 201, "El campo 'name' del cuerpo de la respuesta coincide con el campo 'name' del cuerpo de la solicitud"
    assert kit_response.json()["name"] != "name"
    print(kit_response.status_code)

def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.new_client(kit_body)
    assert kit_response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parametros"

def test_caract_min_1():
    positive_assert("a")

def test_caract_max_511():
    positive_assert("a"* 511)



def test_caract_menor_que_el_min():
    negative_assert("")

def test_caract_mayor_que_el_max():
    negative_assert("a" * 512)

def test_caracter_especial():
    positive_assert("\"№%@\",")

def test_espacios_permitidos():
    positive_assert("A Aaa")

def test_numeros_permitidos():
    positive_assert("123")

def test_sin_parametro():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert( kit_body)

def test_parametro_diferente_num():
    negative_assert(123)