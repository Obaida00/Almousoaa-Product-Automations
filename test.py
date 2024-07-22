global x
def append_one(li):
    global x
    x.replace('g', 's')
x = 'ghgd'
append_one(x)
print(x)