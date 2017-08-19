const DIVISORS = {
  3: 'fizz',
  5: 'buzz'
}

const capitalizeString = string => string[0].toUpperCase() + string.slice(1)

const fizzbuzz = upperLimit => {
  for (let number = 1; number <= upperLimit; number++) {
    let resultantString = ''

    for (const [divisor, string] of Object.entries(DIVISORS)) {
      if (number % divisor === 0) {
        resultantString += string
      }
    }

    if (!resultantString) {
      resultantString += number
    }

    console.log(capitalizeString(resultantString))
  }
}

fizzbuzz(100)
