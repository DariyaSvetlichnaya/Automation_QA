# Let's create 3 sets of people that are in different blacklists
australia_blacklist = {'Sam', 'Petya', 'Jon', 'Colin', 'Eugene'}
poker_blacklist = {'Sam', 'Katya', 'Jon', 'Max', 'Peter'}
alcohol_blacklist = {'Jack', 'Jon', 'Steven', 'Colin', 'Eugene'}

# Intersection between 3 sets
jackpot_list = australia_blacklist & poker_blacklist & alcohol_blacklist

# Print result of intersection
print(jackpot_list)
