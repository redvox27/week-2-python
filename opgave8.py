startWaarde = 1
eindWaarde = 6
deler = 1
testresultaat = 0
testLijst = []
delerLijst = []

while startWaarde <= eindWaarde :
    testresultaat = startWaarde / deler
    print(startWaarde)
    testLijst.append(testresultaat)
    delerLijst.append(deler)


    if deler == startWaarde :
        startWaarde =  startWaarde +1
        deler = 1
        testLijst = []


    else:
        deler = deler +1
        startWaarde = startWaarde
    print("startwaarde:",startWaarde,"deler: ", deler,"testres: ", testresultaat )

