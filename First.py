from pymongo import MongoClient

# Initialize the MongoDB client
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find all Pikachu Pokemon
pikachu_pokemon = pokemonColl.find({"name": "Pikachu"})

# print result
for pokemon in pikachu_pokemon:
    print(pokemon)
