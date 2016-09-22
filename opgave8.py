startWaarde = 1
eindWaarde = 6
deler = 1
testresultaat = 0
testLijst = []
delerLijst = []

while startWaarde <= eindWaarde :
    testresultaat = startWaarde / deler
    print("startwaarde: ",startWaarde)
    print("deler: ",deler)
    print("testresultaat: ", testresultaat)
    testLijst.append(testresultaat)

    if deler == startWaarde:
        startWaarde = startWaarde +1
        deler = 1



    else:
        deler = deler + 1



