def pokemonTeam():
    pokemonList = []
    finalPokemonList = []
    finalTypeList1 = []
    finalTypeList2 = []
    typeList1 = []
    typeList2 = []

    for pokemonEntry in range(2):
        pokemon = input("pokemon")
        type1 = input("type1")
        type2 = input("type2")

        if type2 =="":
            typeList2.append("non")


        pokemonList.append(pokemon)
        typeList1.append(type1)
        typeList2.append(type2)

    for pokemon in pokemonList:

        finalPokemonList.append(pokemon)

    for type1 in typeList1:
        finalTypeList1.append(type1)

    for type2 in typeList2:
        finalTypeList2.append(type2)

    i = 0
    while i < 2:
        print("pokemon: ",finalPokemonList[i], "type1: ",finalTypeList1[i], "type2: ",finalTypeList2[i] )

        i = i+1




pokemonTeam()

