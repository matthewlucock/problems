_DIVISORS = {
    3: 'fizz',
    5: 'buzz'
}

def fizzbuzz(upper_limit):
    for number in range(1, upper_limit + 1):
        resultant_string = ''

        for divisor, string in _DIVISORS.items():
            if number % divisor == 0:
                resultant_string += string

        if not resultant_string:
            resultant_string = str(number)

        print(resultant_string.capitalize())

if __name__ == '__main__':
    fizzbuzz(100)
