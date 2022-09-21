#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tweepy

oauth1_user_handler = tweepy.OAuth1UserHandler(
    "4GXexMbjSmrMuWPhEE5SPIxEw", "08wu6UDYT4BWLIoFvIrnPzyNFg7u7MTeke1P56SXVaAPFS3B3R",
    callback="oob"
)
print(oauth1_user_handler.get_authorization_url())
verifier = input("Input PIN: ")
access_token, access_token_secret = oauth1_user_handler.get_access_token(
    verifier
)
print(access_token)
print(access_token_secret)


# In[3]:





# In[ ]:




