def flatten_multidimensional_array(array)
  resultant_array = []

  array.each do |item|
    if item.is_a?(Array)
      resultant_array.concat(flatten_multidimensional_array(item))
    else
      resultant_array.push(item)
    end
  end

  resultant_array
end
