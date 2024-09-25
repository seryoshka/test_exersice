import requests
import pytest

# URL для получения списка пользователей
USERS_URL_MALE = "https://hr-challenge.dev.tapyou.com/api/test/users?gender=male"
USERS_URL_FEMALE = "https://hr-challenge.dev.tapyou.com/api/test/users?gender=female"
USER_URL = "https://hr-challenge.dev.tapyou.com/api/test/user/{}"
HEADERS = {"accept": "application/json"}


def validate_user_data(user_data):
    """Проверка структуры данных пользователя."""
    assert "id" in user_data, "У пользователя отсутстввет ID"
    assert isinstance(user_data["id"], int), "Поле ID должно быть целым числом"

    assert "name" in user_data, "Поле 'name' обязательное"
    assert isinstance(user_data["name"], str), "Поле 'name' должно быть строкой"

    assert "gender" in user_data, "Поле 'gender' обязательное"
    assert isinstance(user_data["gender"], str), "Поле 'gender'должно быть строкой"
    assert user_data["gender"] in ["male", "female"], "Поле 'gender' должено быть 'male' или 'female'"

    assert "age" in user_data, "Поле 'age' обязательное"
    assert isinstance(user_data["age"], int), "Поле 'age' должено быть целым числом"

    assert "city" in user_data, "Поле 'city' обязательное"
    assert isinstance(user_data["city"], str), "Поле 'city' должено быть строкой"

    assert "registrationDate" in user_data, "Поле 'registrationDate' обязательное"
    assert isinstance(user_data["registrationDate"], str), "Поле 'registrationDate' должно быть строкой"


# Тест для получения пользователей с gender=female
def test_get_female_users():
    response = requests.get(USERS_URL_FEMALE, headers=HEADERS)
    assert response.status_code == 200, f"Не удалось получить список женщин, статус: {response.status_code}"

    users_response = response.json()
    assert isinstance(users_response, dict), "Ответ должен быть объектом (dict)"
    assert "isSuccess" in users_response, "Ответ должен содержать поле 'isSuccess'"
    assert users_response["isSuccess"] is True, "Ошибка"
    assert "errorCode" in users_response, "Ответ должен содержать поле 'errorCode'"
    assert users_response["errorCode"] == 0, "Ошибка"

    users = users_response.get("user", [])
    assert isinstance(users, list), "Поле 'user' должно быть массивом (array) пользователей"

    for user_data in users:
        validate_user_data(user_data)


# Тест для получения пользователей с gender=male
def test_get_male_users():
    response = requests.get(USERS_URL_MALE, headers=HEADERS)
    assert response.status_code == 200, f"Не удалось получить список мужчин, статус: {response.status_code}"

    users_response = response.json()
    assert isinstance(users_response, dict), "Ответ должен быть объектом (dict)"
    assert "isSuccess" in users_response, "Ответ должен содержать поле 'isSuccess'"
    assert users_response["isSuccess"] is True, "Ошибка"
    assert "errorCode" in users_response, "Ответ должен содержать поле 'errorCode'"
    assert users_response["errorCode"] == 0, "Ошибка"

    users = users_response.get("user", [])
    assert isinstance(users, list), "Поле 'user' должно быть массивом (array) пользователей"

    for user_data in users:
        validate_user_data(user_data)

