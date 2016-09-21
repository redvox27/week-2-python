

def perfectInt() :
    startGetal = 6
    deler = 1
    testResult = 0

    while testResult <= startGetal :
        testResult = startGetal / deler
        print(testResult)
        deler +1
        if testResult == startGetal :
            break


    print(testResult)

perfectInt()