x = range(10)
def f(x):
    return x * 2

y = []
for dummy_x in x:
    y.append(f(dummy_x))
print [x, y]

