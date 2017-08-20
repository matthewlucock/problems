import utilities
from digits import DIGITS


_NUMBER_PROMPT = 'Number: '
_SIZE_PROMPT = 'Size: '
_SPACE = ' '
_DASH = '—'
_PIPE = '|'


def _generate_dashed_row(row_is_filled, size):
    string = _SPACE

    for _ in range(size):
        string += _DASH if row_is_filled else _SPACE

    string += _SPACE
    return string


def _generate_piped_section(left, right, size):
    rows = []

    for _ in range(size):
        row = _PIPE if left else _SPACE

        for _ in range(size):
            row += _SPACE

        row += _PIPE if right else _SPACE
        rows.append(row)

    return rows


def _generate_digit_string_rows(digit, size):
    digit = DIGITS[digit]

    return utilities.flatten_list([
        _generate_dashed_row(digit.top, size),
        _generate_piped_section(digit.top_left, digit.top_right, size),
        _generate_dashed_row(digit.middle, size),
        _generate_piped_section(digit.bottom_left, digit.bottom_right, size),
        _generate_dashed_row(digit.bottom, size)
    ])


def generate_number_string(number, size):
    digit_string_rows_list = (
        [_generate_digit_string_rows(int(digit), size) for digit in str(number)]
    )

    return '\n'.join(
        utilities.flatten_two_dimensional_string_list_horizontally(
            digit_string_rows_list,
            ' ' * size
        )
    )


def prompt():
    number = utilities.get_integer_input(_NUMBER_PROMPT)
    size = utilities.get_integer_input(_SIZE_PROMPT)

    print('\n{}\n'.format(generate_number_string(number, size)))


if __name__ == '__main__':
    while True:
        prompt()
