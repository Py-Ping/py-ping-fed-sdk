def safe_name(unsafe_string, unsafe_char="/", sub_char="_"):
    safe_string_list = [x if x not in unsafe_char else sub_char for x in unsafe_string]
    safe_string_list = [x if x not in "{}" else "" for x in safe_string_list]

    return str("".join(safe_string_list))


def safe_variable(unsafe_variable):
    """
    Some APIs define variables that are unsafe to Python code
    e.g. id and type are both reserved words in Python.
    This helper adds 'var_' to the beginning to avoid shadowing
    these builtins.
    """
    if unsafe_variable == "id":
        return "var_id"
    elif unsafe_variable == "type":
        return "var_type"
    return unsafe_variable


def requests_verb(verb):
    if verb == "POST":
        return "requests.post"
    elif verb == "PUT":
        return "requests.put"
    elif verb == "DELETE":
        return "requests.delete"
    elif verb == "HEAD":
        return "requests.head"
    return "requests.get"


def json_type_convert(json_type):
    if json_type == "enum":
        return "str"
    elif json_type == "string":
        return "str"
    elif json_type == "boolean":
        return "bool"
    elif json_type == "array":
        return "list"
    elif json_type == "integer":
        return "int"
    return ""
