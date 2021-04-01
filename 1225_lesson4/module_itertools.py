from itertools import count, cycle, repeat

# count(start)
for el in count(10):
    if el > 15:
        break
    else:
        print(el)

# cycle()
c = 0
for el in cycle("abc"):
    if c > 4:
        break
    print(el)
    c += 1

prog_lang = ['python', 'java', 'c++', 'rust', 'perl']
iter = cycle(prog_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


for el in repeat('a', 2):
    print(el)
