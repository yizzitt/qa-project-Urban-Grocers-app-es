import requests

from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH


def post_new_user(body):
    return requests.post(
        URL_SERVICE + CREATE_USER_PATH,
        json=body,
        timeout=10
    )


def post_new_client_kit(auth_token, kit_body):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    return requests.post(
        URL_SERVICE + KITS_PATH,
        json=kit_body,
        headers=headers,
        timeout=10
    )