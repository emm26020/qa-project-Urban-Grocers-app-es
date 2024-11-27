import sender_stand_request
import data


def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body


def get_new_user_token():
    response = sender_stand_request.create_user()
    assert response is not None, "Error: No se pudo obtener el token de usuario."
    return response


def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.create_personal_kit(auth_token, kit_body["name"])
    assert response.status_code == 201, f"Error: Código de estado inesperado {response.status_code}. Respuesta: {response.text}"
    assert response.json()["name"] == kit_body["name"], f"Error: El nombre del kit en la respuesta '{response.json()['name']}' no coincide con '{kit_body['name']}'."


def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.create_personal_kit(auth_token, kit_body.get("name"))
    assert response.status_code == 400, f"Error: Código de estado inesperado {response.status_code}. Respuesta: {response.text}"
    assert response.json()["code"] == 400, "Error: El código de error en la respuesta no es 400."


# PRUEBAS POSITIVAS

def test_kit_min_length():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


def test_kit_max_length():
    max_length_name = data.max_length_name
    kit_body = get_kit_body(max_length_name)
    positive_assert(kit_body)


def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


def test_kit_name_with_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# PRUEBAS NEGATIVAS

def test_kit_empty_name():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


def test_kit_name_too_long():
    too_long_name = data.too_long_name
    kit_body = get_kit_body(too_long_name)
    negative_assert_code_400(kit_body)


def test_kit_name_special_characters():
    special_name = data.special_name
    kit_body = get_kit_body(special_name)
    negative_assert_code_400(kit_body)


def test_kit_name_not_provided():
    kit_body = {}
    negative_assert_code_400(kit_body)


def test_kit_name_is_number():
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body)
