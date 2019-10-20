
# coding: utf-8

# # Document retrieval from wikipedia data

# In[2]:

import graphlab as gl


# In[3]:

people = gl.SFrame('people_wiki.gl/')


# In[4]:

people.head()


# In[5]:

len(people)


# # Explore the dataset and checkout the text it contains.
# ## Exploring the entry for president Obama

# In[6]:

obama = people[people['name'] == 'Barack Obama']


# In[7]:

obama


# In[8]:

obama['text']


# In[9]:

clooney = people[people['name'] == 'George Clooney']
clooney['text']


# In[10]:

obama['word_count'] = gl.text_analytics.count_words(obama['text'])


# In[11]:

print obama['word_count']


# ## Sort the word count dict for the Obama articale

# In[12]:

obama_word_count_table = obama[['word_count']].stack('word_count',new_column_name = ['word', 'count'])


# In[13]:

obama_word_count_table.sort('count',ascending=False)


# # Compute TF-IDF for the corpus 
# 
# To give more weight to informative words, we weigh them by their TF-IDF scores.

# In[5]:

people['word_count'] = gl.text_analytics.count_words(people['text'])


# In[6]:

people.head()


# In[7]:

tfidf = gl.text_analytics.tf_idf(people['word_count'])


# In[8]:

tfidf


# In[9]:

people['tfidf'] = tfidf


# ## Examine the TF-IDF for the Obama article

# In[20]:

obama = people[people['name'] == 'Barack Obama']


# In[21]:

obama


# In[22]:

obama[['tfidf']].stack('tfidf', new_column_name=['word','tfidf']).sort('tfidf', ascending=False)


# # Manually compute distances between a few people¶

# In[23]:

clinton = people[people['name'] == 'Bill Clinton']


# In[19]:

beckham = people[people['name'] == 'David Beckham']


# In[25]:

gl.distances.cosine(obama['tfidf'][0], clinton['tfidf'][0])


# In[26]:

gl.distances.cosine(obama['tfidf'][0], beckham['tfidf'][0])


# # Build a nearest neighbor model for document retrieval

# In[10]:

knn_model = gl.nearest_neighbors.create(people,features=['tfidf'],label='name')


# In[28]:

## Start apply the model: who's colest to the obama?
knn_model.query(obama)


# # some other examples:

# In[29]:

swift = people[people['name'] == 'Taylor Swift']


# In[30]:

knn_model.query(swift)


# In[11]:

elton = people[people['name'] == 'Elton John']


# In[12]:

elton


# In[14]:

elton_text_table = elton[['word_count']].stack('word_count', new_column_name = ['word','count']).sort('count', ascending = False)


# In[15]:

elton_text_table


# In[16]:

elton[['tfidf']].stack('tfidf', new_column_name=['word','tfidf']).sort('tfidf', ascending=False)


# In[30]:

beckham = people[people['name'] == 'Victoria Beckham']


# In[31]:

gl.distances.cosine(elton['tfidf'][0],beckham['tfidf'][0] )


# In[21]:

maCartney = people[people['name'] == 'Paul McCartney']


# In[32]:

gl.distances.cosine(elton['tfidf'][0],maCartney['tfidf'][0])


# In[23]:

word_cmodel = gl.nearest_neighbors.create(people,features=['word_count'],label='name',distance='cosine')


# In[24]:

knn_cmodel = gl.nearest_neighbors.create(people,features=['tfidf'],label='name',distance='cosine')


# In[25]:

word_cmodel.query(elton)


# In[26]:

knn_cmodel.query(elton)


# In[33]:

word_cmodel.query(beckham)


# In[34]:

knn_cmodel.query(beckham)


# In[ ]:



