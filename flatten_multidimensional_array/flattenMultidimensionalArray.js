'use strict'

const flattenMultidimensionalArray = array => {
  const resultantArray = []

  for (const item of array) {
    if (Array.isArray(item)) {
      resultantArray.push(...flattenMultidimensionalArray(item))
    } else {
      resultantArray.push(item)
    }
  }

  return resultantArray
}

module.exports = flattenMultidimensionalArray
