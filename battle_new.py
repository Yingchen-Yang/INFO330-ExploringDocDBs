import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    # add code to store advantages stats
    pokemon1_advantages = []
    pokemon2_advantages = []

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            #store
            pokemon1_advantages.append(stat)
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            #store
            pokemon2_advantages.append(stat)
        # add situation when its stats equal
        else:
            print("Both Pokemon have equal " + stat)

    # change code to get more correct results of winner base on stored stats
    if len(pokemon1_advantages) > len(pokemon2_advantages):
        print("Battle results: " + pokemon1['name'] + " wins!")
    elif len(pokemon2_advantages) > len(pokemon1_advantages):
        print("Battle results: " + pokemon2['name'] + " wins!")
    # add tie situation as result
    else:
        print("Battle results: Tie")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
