# ---------- EXERCISE ZERO ---------

# --- Lists
fav_colours = ['blue', 'teal', 'maroon']

family_ages = [26, 22, 32, 28]

coin_flip = ['heads', 'tails', 'heads', 'heads', 'tails']

fave_bands = ['Kings of Leon', 'The Killers', 'Blink-182']

# --- Dictionaries
words = {
  'nummet': 'light meal or luncheon',
  'behoof': 'a benefit resulting from some course of action',
  'stactometer': 'pipette with hollow bulb for counting drops'
}

movies = {
  'Jaws': 1975,
  'Empire Records': 1995,
  'The Conjuring': 2013
}

cities = {
  'Toronto': 2.93,
  'Brooklyn': 2.64,
  'Barcelona': 1.61
}

friend_ages = {
  'Rachel': 23,
  'Christina': 25,
  'Alan': 29,
  'Brandon':27
}



# ---------- EXERCISE ONE ---------

# Print out the list of coin flips.
print(coin_flip)

# Print out the first element of the list of your favourite colours.
print(fav_colours[0])

# Output the sorted version of the list of your friends and family members' ages.
family_ages.sort()
print(family_ages)

# Add a new baby (0 years old) to the list of your family's ages.
family_ages.append(0)
# print(family_ages)

print(movies['The Conjuring'])



# ---------- EXERCISE TWO ---------

# Print out the last element of the list of your favourite colours.
print(fav_colours[-1])

# Add a new city to the dictionary of cities and population.
cities['Paris'] = 2.14
# print(cities)

# Reverse the list of coin flips and save it.
coin_flip.reverse()
# print(coin_flip)

# Print out the population of one of the cities.
print(cities['Paris'])

# Print out a sentence about each item in the list of performing artists. For example:
for band in fave_bands:
  print(f"I think {band} is great.")



# ---------- EXERCISE THREE ---------

# Print out the first two performing artists in that list.
print(fave_bands[0:2])

# For each of your favourite movies, print out a sentence about when the movie was released.
for movie, year in movies.items():
  print(f"{movie} came out in {year}")

# Sort and reverse the list of ages of your family. Save it and print it to the screen.
family_ages.sort(reverse=True)
print(family_ages)

# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.
movies['Beauty and the Beast'] = {
  'original': 1991,
  'remake': 2017
}
print(movies)





