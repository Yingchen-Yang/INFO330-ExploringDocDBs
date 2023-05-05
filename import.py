import sqlite3
import pymongo
from pymongo import MongoClient

# Initialize the MongoDB client
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Connect to SQLite db
sqlite_conn = sqlite3.connect("pokemon.sqlite")
sqlite_cursor = sqlite_conn.cursor()

# Define the query
query = """
    SELECT p.name, p.pokedex_number, t.type1, t.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, a.name
    FROM pokemon AS p
    LEFT JOIN pokemon_types_view AS t ON p.name = t.name
    LEFT JOIN pokemon_abilities AS pa ON p.id = pa.pokemon_id
    LEFT JOIN ability AS a ON pa.ability_id = a.id
"""

# fetch all the data
sqlite_cursor.execute(query)
rows = sqlite_cursor.fetchall()

# Close the SQL connection
sqlite_conn.close()

# Transform the format
pokemon_data = {}
for row in rows:
    pokedex_number = row[1]
    if pokedex_number not in pokemon_data:
        pokemon_data[pokedex_number] = {
            "name": row[0],
            "pokedex_number": row[1],
            "types": [t for t in [row[2], row[3]] if t],
            "hp": row[4],
            "attack": row[5],
            "defense": row[6],
            "speed": row[7],
            "sp_attack": row[8],
            "sp_defense": row[9],
            "abilities": [row[10]]
        }
    else:
        pokemon_data[pokedex_number]["abilities"].append(row[10])

# Insert the data into the MongoDB database
pokemon_list = [pokemon_data[key] for key in pokemon_data]
pokemonColl.insert_many(pokemon_list)

# Close the MongoDB client connection
mongoClient.close()

