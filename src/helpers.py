import os
import requests
from time import sleep
from requests.auth import HTTPBasicAuth


def is_post_version_11(version_str):
    """
    Ping Federate v11 on uses Swagger 2.0 conventions.
    Return true if the version can be identified as v11 or greater
    """
    version_list = version_str.split(".")
    # no dot, likely latest or edge, which is greater than v11
    if len(version_list) == 1:
        return True
    elif len(version_list) > 1:
        try:
            major_ver = int(version_list[0])
        except ValueError:
            # bad formatting, raise an error with a warning.
            raise Exception("Unknown version format.")
        return major_ver >= 11
    return False


def safe_name(unsafe_string, unsafe_char="/", sub_char="_", rem_leading_char=True):
    safe_string_list = [
        x if x not in unsafe_char else sub_char for x in unsafe_string
    ]
    safe_string_list = [
        x if x not in "{}-" else "" for x in safe_string_list
    ]

    safe_string = "".join(safe_string_list)
    if len(safe_string) and rem_leading_char and safe_string.startswith(sub_char):
        return safe_string[1:]
    return safe_string


def safe_module_name(unsafe_string, sub_char="_"):
    """
    Creates a safe module name. If an upper case character is found in the module name,
    replace it with its lower case character and put the separator character "sub_char"
    before it.

    e.g. idp/ThisIsAModule -> idp_this_is_a_module

    """
    safe_string = safe_name(unsafe_string)
    safe_module_name_list = [
        x if x.islower() or x == sub_char else f"{sub_char}{x.lower()}" for x in safe_string
    ]

    if "_" in safe_module_name_list[0]:
        safe_module_name_list[0] = safe_module_name_list[0].replace("_", "")

    return "".join(safe_module_name_list)


def safe_class_name(unsafe_string, unsafe_char="/"):
    safe_class_name = ""
    for substr in unsafe_string.split(unsafe_char):
        if substr:
            safe_class_name += substr[0].capitalize() + substr[1:]
    return safe_class_name


def get_py_type(json_type):
    """
    Given a JSON type return a corresponding Python type.
    If no type can be determined, return an empty string.
    """

    if json_type in ("enum", "string", "File", "file"):
        return "str"
    elif json_type == "boolean":
        return "bool"
    elif json_type == "array":
        return "list"
    elif json_type == "integer":
        return "int"
    elif json_type == "int":
        return "int"
    elif json_type == "number":
        return "float"
    elif json_type == "void":
        return "None"
    return ""


def get_auth_session():

    if 'PING_IDENTITY_USER' in os.environ and 'PING_IDENTITY_SECRET' in os.environ:
        ping_user = os.environ.get("PING_IDENTITY_USER")
        ping_pass = os.environ.get("PING_IDENTITY_SECRET")
    else:
        ping_user = os.environ.get(
            "PING_IDENTITY_DEVOPS_ADMINISTRATOR", "administrator"
        )
        ping_pass = os.environ.get(
            "PING_IDENTITY_DEVOPS_PASSWORD", "2FederateM0re"
        )

    session = requests.Session()
    session.auth = HTTPBasicAuth(ping_user, ping_pass)
    session.headers = {
        "Accept": "application/json",
        "X-XSRF-Header": "PingFederate"
    }
    return session


def retry_with_backoff(func, retries=5, backoff=5):
    total_retries = retries
    while retries:
        try:
            func()
        except Exception as ex:
            print(
                f"{ex}, attempting retry"
                f"{total_retries - (retries + 1)}/{total_retries},"
                f"wait {backoff} seconds..."
            )
            retries -= 1
            sleep(backoff)
            backoff += backoff
            continue
        return True
    if not retries:
        return False


def strip_ref(ref_str):
    if "#/definitions/" in ref_str:
        return ref_str.split("/")[-1]
    return ref_str
