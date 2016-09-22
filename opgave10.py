#credit card bestaat uit 19 cijfers
#6 cijfers voor de kaartleverancier
#   een variabel aantal cijfers(max12)
#   een laatste cijfers als check


validCard = "4388576018410707" #16 digits
invalidCard = "4388576018402626" #16 digits

def validCheck(cardNumber):
    n = 1
    cardNumber = cardNumber[::-1]
    cardNumber =[cardNumber[i:i + n] for i in range(0, len(cardNumber), n)]
    print(cardNumber)

validCheck(validCard)
