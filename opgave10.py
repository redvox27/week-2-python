#credit card bestaat uit 19 cijfers
#6 cijfers voor de kaartleverancier
#   een variabel aantal cijfers(max12)
#   een laatste cijfers als check


validCard = "4388576018410707" #16 digits
invalidCard = "4388576018402626" #16 digits
unevenList = []
evenList = []
def validCheck(cardNumber):
    n = 1
    cardNumber = cardNumber[::-1]
    cardNumber =[cardNumber[i:i + n] for i in range(0, len(cardNumber), n)]
    print(cardNumber)
    cardNumber = [int(i) for i in cardNumber]
    print(cardNumber)

    unevenList = cardNumber[1::2] #start, stop, step // de start is eerste index, stop = einde list, step = 2 dus de uneven indexes
    print("unevenList: ",unevenList)

    evenList = cardNumber[0::2]
    print("evenList: ", evenList)

    unevenResult = sum(unevenList) #som van values in list
    print(unevenResult)



validCheck(validCard)
