import numpy

print(numpy.arange(1, 11))
print(numpy.arange(50, 101))

numbers = numpy.arange(50, 101)
slicer = slice(20, 23)
print(numbers[slicer])