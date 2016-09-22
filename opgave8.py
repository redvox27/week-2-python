startWaarde = 2
eindWaarde = 6
deler = 1
testresultaat = 0
testLijst = []
delerLijst = []

while startWaarde <= eindWaarde :
    testresultaat = startWaarde / deler
    if testresultaat == isinstance(testresultaat,int) :
        testLijst.append(testresultaat)
    delerLijst.append(deler)


    if deler == startWaarde +1:
        startWaarde =  startWaarde +1
        deler = 2
        testLijst = []


    else:
        deler = deler +1

    print("startwaarde:",startWaarde,"deler: ", deler,"testres: ", testresultaat , testLijst, delerLijst)

