def pokemonTeam():
    pokemonList = []
    finalPokemonList = []
    finalTypeList1 = []
    finalTypeList2 = []
    typeList1 = []
    typeList2 = []

    pokemonTypeList = ["fairy", "steel", "dark", "dragon", "ghost", "rock", "bug", "psychic", "flying",
                "ground", "poison", "fight", "ice", "grass", "electric", "water", "fire", "normal"]

    weakness1 = []
    weakness2 = " "
    outputWeaknessList = []

    for pokemonEntry in range(2):
        pokemon = input("pokemon")
        type1 = input("type1")
        type2 = input("type2")

        if type2 =="":
            typeList2.append("non")

        if type1 == pokemonTypeList[0]: #the type is fairy
            weakness1 = ["poison, steel "]

        if type1 == pokemonTypeList[1]: #the type is steel
            weakness1 = "fire, fight, ground"


        pokemonList.append(pokemon)
        typeList1.append(type1)
        typeList2.append(type2)

    for pokemon in pokemonList:

        finalPokemonList.append(pokemon)

    for type1 in typeList1:
        finalTypeList1.append(type1)

    for type2 in typeList2:
        finalTypeList2.append(type2)

    for weakness in weakness1:
        outputWeaknessList.append(weakness)

    i = 0
    while i < 2:
        print("pokemon: ",finalPokemonList[i], "type1: ",finalTypeList1[i], "type2: ",finalTypeList2[i],"weakness(es): ",outputWeaknessList[0] )

        i = i+1


pokemonTeam()

