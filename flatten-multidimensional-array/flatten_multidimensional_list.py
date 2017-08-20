def flatten_multidimensional_list(list_):
    resultant_list = []

    for item in list_to_flatten:
        if isinstance(item, list):
            resultant_list += flatten_list(item)
        else:
            resultant_list.append(item)

    return resultant_list
