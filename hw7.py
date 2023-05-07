from pymongo import MongoClient

# I use below in the terminal to import data
# mongoimport --type csv --headerline --db pokemon --collection pokemon_data --file pokemon.csv

# Connect to the MongoDB instance
client = MongoClient("mongodb://localhost/pokemon")

# Access the "pokemon" database
db = client.pokemon

# Access the "pokemon_data" collection
collection = db.pokemon_data

# Question 1: Return all the Pokemon named "Pikachu"
print('Answer to question1:')
pikachu = collection.find_one({'name': 'Pikachu'})
print("Name:", pikachu['name'])
print("Pokedex number:", pikachu['pokedex_number'])
print("Types:", pikachu['type1'], pikachu['type2'])
print("HP:", pikachu['hp'])
print("Attack:", pikachu['attack'])
print("Defense:", pikachu['defense'])
print("Speed:", pikachu['speed'])
print("Special attack:", pikachu['sp_attack'])
print("Special defense:", pikachu['sp_defense'])
print("Abilities:", pikachu['abilities'])
print('')
print('')


# Question 2: Return all the Pokemon with an attack greater than 150
print('Anser to question2:')
strong_pokemon = collection.find({'attack': {'$gt': 150}})
for pokemon in strong_pokemon:
    print("Name:", pokemon['name'])
    print("Pokedex number:", pokemon['pokedex_number'])
    print("Types:", pokemon['type1'], pokemon['type2'])
    print("HP:", pokemon['hp'])
    print("Attack:", pokemon['attack'])
    print("Defense:", pokemon['defense'])
    print("Speed:", pokemon['speed'])
    print("Special attack:", pokemon['sp_attack'])
    print("Special defense:", pokemon['sp_defense'])
    print("Abilities:", pokemon['abilities'])
    print('')
print('')
print('')


# Question 3: Rerurn all the Pokemon with an ability "Overgrow"
print('Answer to question 3:')
overgrow_pokemon = collection.find({'abilities': {'$regex': 'Overgrow', '$options': 'i'}})

for pokemon in overgrow_pokemon:
    print("Name:", pokemon['name'])
    print("Pokedex number:", pokemon['pokedex_number'])
    print("Types:", pokemon['type1'], pokemon['type2'])
    print("HP:", pokemon['hp'])
    print("Attack:", pokemon['attack'])
    print("Defense:", pokemon['defense'])
    print("Speed:", pokemon['speed'])
    print("Special attack:", pokemon['sp_attack'])
    print("Special defense:", pokemon['sp_defense'])
    print("Abilities:", pokemon['abilities'])
    print('')
