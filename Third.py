from pymongo import MongoClient

# Initialize the MongoDB client
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find all Pokemon with the "Overgrow" ability
overgrow_pokemon = pokemonColl.find({"abilities": "Overgrow"})

# print result
for pokemon in overgrow_pokemon:
    print(pokemon)
