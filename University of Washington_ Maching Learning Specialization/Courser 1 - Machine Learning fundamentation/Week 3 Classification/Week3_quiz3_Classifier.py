
# coding: utf-8

# # Assignment 3

# In[1]:

import graphlab as gl


# In[2]:

products = gl.SFrame('amazon_baby.gl/')


# In[3]:

products['word_count']= gl.text_analytics.count_words(products['review'])


# In[ ]:

gl.canvas.set_target('ipynb')


# In[5]:

products = products[products['rating'] != 3]


# In[6]:

products['sentiment'] = products['rating'] >=4


# In[7]:

products.head()


# In[79]:

sentiment_model = gl.logistic_classifier.create(train_data, target = 'sentiment',features = ['word_count'], validation_set = test_data)


# ## selected words analytics

# In[9]:

selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']


# In[84]:

for word in selected_words:
    products[word] = products['word_count'].apply(lambda x : x[word] if x.has_key(word) else 0)
    print 'The number of instances of \"%s\" is %s.' % (word, products[word].sum())


# In[12]:

products.head()


# ## 2. Create a new sentiment analysis model using only the selected_words as features:

# In[48]:

train_data,test_data = products.random_split(.8, seed=0)


# In[53]:

selected_words_model = gl.logistic_classifier.create(train_data, target = 'sentiment',features = selected_words, validation_set = test_data)


# In[55]:

print selected_words_model['coefficients']


# In[56]:

selected_words_model.evaluate(test_data, metric = 'roc_curve')


# In[75]:

selected_words_model.show(view='Evaluation')


# In[58]:

gl.canvas.set_target('ipynb')    


# In[68]:

len(test_data[test_data['sentiment'] == 1])


# In[67]:

len(test_data)


# In[74]:

27976 / 33304.0


# ### Which of the following ranges contains the ‘predicted_sentiment’ for the most positive review for ‘Baby Trend Diaper Champ’?

# In[77]:

babay_trend_reviews = products[products['name'] ==  'Baby Trend Diaper Champ']


# In[80]:

babay_trend_reviews['predicted_sentiment'] = sentiment_model.predict(babay_trend_reviews, output_type='probability')


# In[81]:

babay_trend_reviews = babay_trend_reviews.sort('predicted_sentiment', ascending = False)


# In[82]:

babay_trend_reviews[0]


# In[83]:

selected_words_model.predict(babay_trend_reviews[0], output_type='probability')


# In[ ]:



