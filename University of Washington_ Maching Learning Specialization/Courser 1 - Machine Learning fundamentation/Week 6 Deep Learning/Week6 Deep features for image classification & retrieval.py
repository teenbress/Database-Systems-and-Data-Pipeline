
# coding: utf-8

# # Week 6: Deep features for image classification & retrieval 

# In[1]:

import graphlab as gl


# In[6]:

image_train = gl.SFrame('image_train_data/')


# In[28]:

image_test = gl.SFrame('image_test_data/')


# In[33]:

gl.canvas.set_target('ipynb')


# In[34]:

image_test[0:1]['image'].show()


# ## Creating category-specific image retrieval models

# In[19]:

image_train_bird = image_train[image_train['label'] == 'bird']


# In[20]:

image_train_dog = image_train[image_train['label'] == 'dog']


# In[21]:

image_train_cat = image_train[image_train['label'] == 'cat']


# In[22]:

image_train_automobile = image_train[image_train['label'] == 'automobile']


# In[23]:

knn_model_dog = gl.nearest_neighbors.create(image_train_dog,features=['deep_features'],
                                             label='id')


# In[24]:

knn_model_cat = gl.nearest_neighbors.create(image_train_cat,features=['deep_features'],
                                             label='id')


# In[25]:

knn_model_automobile = gl.nearest_neighbors.create(image_train_automobile,features=['deep_features'],
                                             label='id')


# In[26]:

knn_model_bird = gl.nearest_neighbors.create(image_train_bird,features=['deep_features'],
                                             label='id')


# ## Use image retrieval model with deep features to find similar images

# In[36]:

cat = image_test[0:1]


# In[37]:

cat['image'].show()


# In[39]:

nearest_cats = knn_model_cat.query(cat)


# In[40]:

def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')


# In[42]:

get_images_from_ids(nearest_cats)['image'].show()


# In[43]:

nearest_dogs = knn_model_dog.query(cat)


# In[44]:

get_images_from_ids(nearest_dogs)['image'].show()


# In[48]:

nearest_dogs['distance'].mean()


# In[49]:

nearest_cats['distance'].mean()


# ## Computing nearest neighbors accuracy using SFrame operations

# In[50]:

# trainning models
image_test_dog = image_test[image_test['label'] == 'dog']


# In[53]:

dog_dog_neighbors = knn_model_dog.query(image_test_dog, k=1)
dog_cat_neighbors = knn_model_cat.query(image_test_dog, k=1)
dog_automobile_neighbors = knn_model_automobile.query(image_test_dog, k=1)
dog_bird_neighbors = knn_model_bird.query(image_test_dog, k=1)


# In[55]:

dog_distances = gl.SFrame({'dog-dog': dog_dog_neighbors['distance'],
                                 'dog-cat': dog_cat_neighbors['distance'], 
                                 'dog-automobile': dog_automobile_neighbors['distance'], 
                                 'dog-bird': dog_bird_neighbors['distance']})


# In[56]:

print dog_distances


# In[57]:

row = dog_distances[0]


# In[58]:

row['dog-cat']


# In[59]:

def is_dog_correct(row):
    if row['dog-dog'] < row['dog-cat'] and row['dog-dog'] < row['dog-automobile'] and row['dog-dog'] < row['dog-bird']:
        return 1
    else:
        return 0


# In[60]:

correct_predictions = dog_distances.apply(is_dog_correct)


# In[61]:

total_correct_predictions = correct_predictions.sum()


# In[62]:

accuracy = float(total_correct_predictions) / len(dog_distances)


# In[63]:

accuracy


# In[ ]:



