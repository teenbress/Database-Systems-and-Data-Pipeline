
# coding: utf-8

# # Week 5: Songs Recommender

# In[1]:

import graphlab as gl


# In[14]:

song_data = gl.SFrame('song_data.gl/')


# In[15]:

gl.canvas.set_target('ipynb')


# In[16]:

users = song_data['artist'].unique()


# In[17]:

len(users)


# In[18]:

kanye = song_data[song_data['artist']== 'Kanye West']['user_id'].unique()


# In[19]:

len(kanye)


# In[20]:

fighters = song_data[song_data['artist']== 'Foo Fighters']['user_id'].unique()


# In[21]:

len(fighters)


# In[22]:

swift = song_data[song_data['artist']== 'Taylor Swift']['user_id'].unique()


# In[23]:

len(swift)


# In[24]:

gaga = song_data[song_data['artist']== 'Lady GaGa']['user_id'].unique()


# In[25]:

len(gaga)


# # Compute the sum listen_count for each artist by groupby()

# In[26]:

total_count = song_data.groupby(key_columns='artist', operations={'total_count': gl.aggregate.SUM('listen_count')})


# In[31]:

total_count = total_count.sort('total_count', ascending = False)


# In[ ]:

total_count


# In[32]:

total_count[0]


# In[33]:

total_count[-1]


# # Use groupby-aggregate to find the most recommended songs
#    Creat a song recommender system

# In[34]:

train_data,test_data = song_data.random_split(.8,seed=0)


# In[35]:

personalized_model = gl.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='song')


# ## recommend songs for the first 10,000 test_data users with the above model;

# In[36]:

subset_test_users = test_data['user_id'].unique()[0:10000]


# ## compute one recommended song for each of these test users

# In[38]:

recommend_songs = personalized_model.recommend(subset_test_users,k=1)


# In[39]:

recommend_songs.groupby(key_columns='song', operations={'count': gl.aggregate.COUNT()})


# In[ ]:



