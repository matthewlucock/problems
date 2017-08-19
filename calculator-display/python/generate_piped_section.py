_PIPE = '|'
_SPACE = ' '


def generate_piped_section(left, right, size):
    rows = []

    for _ in range(size):
        row = ''

        if left:
            row += _PIPE
        else:
            row += _SPACE

        for _ in range(size):
            row += _SPACE

        if right:
            row += _PIPE
        else:
            row += _SPACE

        rows.append(row)

    return rows
