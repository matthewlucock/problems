const once = fn => {
  let functionHasBeenCalled = false

  return (...args) => {
    if (!functionHasBeenCalled) {
      functionHasBeenCalled = true
      return fn(...args)
    }
  }
}
