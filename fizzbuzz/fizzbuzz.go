package main

import (
  "fmt"
  "sort"
  "strings"
)

var divisorStrings = map[int]string {
  3: "fizz",
  5: "buzz",
}

var divisors = []int {}

func fizzbuzz(upperLimit int) {
  for number := 1; number <= upperLimit; number++ {
    resultantString := ""

    for _, divisor := range divisors {
      if number % divisor == 0 {
        resultantString += divisorStrings[divisor]
      }
    }

    if resultantString == "" {
      fmt.Println(number)
    } else {
      fmt.Println(strings.Title(resultantString))
    }
  }
}

func main() {
  for divisor := range divisorStrings {
    divisors = append(divisors, divisor)
  }

  sort.Ints(divisors)

  fizzbuzz(100)
}
