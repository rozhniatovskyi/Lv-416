def greet(name):
    if name == 'Johnny':
        return 'Hello, my love!'
    return 'Hello, {name}'.format(name=name)

result = greet('Johnny')
print(result)
