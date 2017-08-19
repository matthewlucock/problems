def once(method)
  method_has_been_called = false

  def wrapper(*args)
    unless method_has_been_called
      method_has_been_called = true
      method(*args)
    end
  end
end
