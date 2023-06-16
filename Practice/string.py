singleQuote = 'Hi'
print(singleQuote)
print(id(singleQuote))

doubleQuote = "Hello! In double quote"
print(doubleQuote)
print(id(doubleQuote))
tripleQuote = """I'm in triple quotes"""
print(tripleQuote)
print(id(tripleQuote))
# id is used to memory address of the object
x, u = 5, 5
print(id(x))
print(id(u))

# negative indexing
print(tripleQuote[-4])

# slicing
print(tripleQuote[7:])

# stride
print(tripleQuote[:: 2])
print(r'foo \\bar \n baz')
