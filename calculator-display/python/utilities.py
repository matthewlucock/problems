_INVALID_INTEGER_MESSAGE = 'You must enter a valid integer'


def get_integer_input(prompt):
    value = None

    while value is None:
        received_input = input(prompt).strip()

        try:
            value = int(received_input)
        except ValueError:
            print(_INVALID_INTEGER_MESSAGE)

    return value


def flatten_list(list_to_flatten):
    resultant_list = []

    for item in list_to_flatten:
        if isinstance(item, list):
            resultant_list += flatten_list(item)
        else:
            resultant_list.append(item)

    return resultant_list


def flatten_two_dimensional_string_list_horizontally(given_list, separator=''):
    resultant_list = given_list[0]

    for list_ in given_list[1:]:
        for index, string in enumerate(list_):
            resultant_list[index] += separator + string

    return resultant_list
