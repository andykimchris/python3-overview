song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro Words'])
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

song_data['Retro Words'] = tag_set

print(song_data)


song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
tag_set.discard('onion')
tag_set.discard('helloworld')
tag_set.discard('spam')

song_data_users['Retro Words'] = tag_set
print(song_data_users`)


# For set containers, we can use curly braces {}, the set() constructor, or set comprehension.
# For frozenset containers, we can only use the frozenset() constructor.
music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Checkpoint 1
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Checkpoint 2
# A union can be found using set or frozenset containers with the .union() method or | operator.
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# Checkpoint 3
# An intersection can be found using set or frozenset containers with the .intersection() method or & operator.
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# Checkpoint 4
# The difference can be found using set or frozenset containers with the .difference() method or - operator.
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# Checkpoint 5
# The symmetric difference can be found using set or frozenset containers with the .symmetric_difference() method or ^ operator.
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)


