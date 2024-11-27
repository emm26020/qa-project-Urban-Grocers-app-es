import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH

#Función para crear un nuevo usuario
def create_user():

    from data import create_user_data

    try:
        response = requests.post(URL_SERVICE + CREATE_USER_PATH, json=create_user_data)
        if response.status_code == 201:
            return response.json().get("authToken")
        else:
            print(f"Error al crear el usuario. Código de estado: {response.status_code}. Respuesta: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

#Función para crear un kit personal
def create_personal_kit(auth_token, kit_name):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    kit_body = {"name": kit_name}  # Crear el cuerpo directamente sin copiar

    try:
        response = requests.post(URL_SERVICE + KITS_PATH, json=kit_body, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None
