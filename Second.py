from pymongo import MongoClient

# Initialize the MongoDB client
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find all Pokemon with an attack greater than 150
high_attack_pokemon = pokemonColl.find({"attack": {"$gt": 150}})

# print result
for pokemon in high_attack_pokemon:
    print(pokemon)
