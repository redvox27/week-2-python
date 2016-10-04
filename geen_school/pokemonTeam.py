def pokemonTeam():
    for pokemonEntry in range(3):
        pokemon = input("pokemon")
       # type1 = input("type1")
        #type2 = input("type2")

        pokemonList = []
        finalPokemonList = []
        typeList1 = []
        typeList2 = []

        pokemonList.append(pokemon)
        #typeList1.append(type1)
        #typeList2.append(type2)

        for pokemon in pokemonList:

            finalPokemonList.append(pokemon)

        print(finalPokemonList)



pokemonTeam()