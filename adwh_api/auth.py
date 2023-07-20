import getpass

import keyring


def get_dwh_password(username: str) -> str:
    password = keyring.get_password(service_name="adwh_dwh_pass", username=username)
    if password is None:
        keyring.set_password(
            service_name="adwh_dwh_pass",
            username=username,
            password=getpass.getpass("Enter your ADWH data warehouse password: "),
        )
        password = keyring.get_password(service_name="adwh_dwh_pass", username=username)
    return password
