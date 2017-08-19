_DASH = '—'
_SPACE = ' '


def generate_dashed_row(row_is_filled, size):
    string = _SPACE

    for _ in range(size):
        if row_is_filled:
            string += _DASH
        else:
            string += _SPACE

    string += _SPACE

    return string
