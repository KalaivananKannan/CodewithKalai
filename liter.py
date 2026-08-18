def list_generator(lst):
    yield from lst




numbers=[10,20,30]
it=list_generator(numbers)
print(next(it))
print(next(it))
print(next(it))