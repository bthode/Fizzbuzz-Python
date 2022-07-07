for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ( str(i) + ' is Multiple of 3 AND 5')
    elif i % 3 == 0:
        print ( str(i) + ' is a multiple of 3')
    elif i % 5 == 0:
        print ( str(i) + ' is a multiple of 5')
    else:
        print ( str(i) )