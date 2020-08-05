def safe_name(unsafe_string, unsafe_char='/', sub_char='_'):
    safe_string_list = [x if x not in unsafe_char else sub_char for x in unsafe_string]
    safe_string_list = [x if x not in '{}' else '' for x in safe_string_list]

    return str(''.join(safe_string_list))

def requests_verb(verb):
    if verb == 'POST':
        return 'requests.post'
    elif verb == 'PUT':
        return 'requests.put'
    elif verb == 'DELETE':
        return 'requests.delete'
    elif verb == 'HEAD':
        return 'requests.head'
    else:
        return 'requests.get'