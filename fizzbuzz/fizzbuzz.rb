DIVISORS = {
  3 => "fizz",
  5 => "buzz"
}

def fizzbuzz(upper_limit)
  1.upto(upper_limit).each do |number|
    resultant_string = ""

    DIVISORS.each do |divisor, string|
      if number % divisor == 0
        resultant_string += string
      end
    end

    if resultant_string.empty?
      resultant_string = number.to_s
    end

    puts resultant_string.capitalize
  end
end

if __FILE__ == $0
  fizzbuzz(100)
end
