from collections import namedtuple


_Digit = namedtuple('Digit', [
    'top',
    'top_left',
    'top_right',
    'middle',
    'bottom_left',
    'bottom_right',
    'bottom'
])
_Digit.__new__.__defaults__ = (True,) * len(_Digit._fields)

DIGITS = {
    0: _Digit(middle=False),
    1: _Digit(
        top=False,
        middle=False,
        bottom=False,
        top_left=False,
        bottom_left=False
    ),
    2: _Digit(top_left=False, bottom_right=False),
    3: _Digit(top_left=False, bottom_left=False),
    4: _Digit(top=False, bottom_left=False, bottom=False),
    5: _Digit(top_right=False, bottom_left=False),
    6: _Digit(top_right=False),
    7: _Digit(middle=False, bottom=False, bottom_left=False),
    8: _Digit(),
    9: _Digit(bottom_left=False)
}
