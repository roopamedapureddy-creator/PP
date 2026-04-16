def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    elif datatype == 'str':
        answer = ''
    else:
        print("Unsupported datatype")
        return
    
    for x in args:
        answer = answer + x
    
    return answer

print(add('int', 5, 10))
print(add('str', 'good', 'section'))
