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

