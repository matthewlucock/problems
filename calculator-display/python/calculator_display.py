import utilities
from digits import DIGITS
from generate_dashed_row import generate_dashed_row
from generate_piped_section import generate_piped_section


NUMBER_PROMPT = 'Number: '
SIZE_PROMPT = 'Size: '


def generate_digit_string_rows(digit, size):
    digit = DIGITS[digit]

    return utilities.flatten_list([
        generate_dashed_row(digit.top, size),
        generate_piped_section(digit.top_left, digit.top_right, size),
        generate_dashed_row(digit.middle, size),
        generate_piped_section(digit.bottom_left, digit.bottom_right, size),
        generate_dashed_row(digit.bottom, size)
    ])


def generate_number_string(number, size):
    digit_string_rows_list = [
        generate_digit_string_rows(int(digit), size) for digit in str(number)
    ]

    return '\n'.join(
        utilities.flatten_two_dimensional_string_list_horizontally(
            digit_string_rows_list,
            ' ' * size
        )
    )

def prompt():
    number = utilities.get_integer_input(NUMBER_PROMPT)
    size = utilities.get_integer_input(SIZE_PROMPT)

    print()
    print(generate_number_string(number, size))
    print()

if __name__ == '__main__':
    while True:
        prompt()
