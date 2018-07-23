 
# # API


from stackapi import StackAPI
from time import sleep
from random import randint


site=StackAPI('stackoverflow')

# site parameters
site.page_size=100
site.max_pages=20

#endpoint fetch
users=site.fetch('users')
users=pd.DataFrame(dict(users.items())['items'])

#more information on users and tags
tags=[]
for i in range(20):
    tags=tags+site.fetch('/users/{ids}/top-tags',ids=users['user_id'][i*100:(i+1)*100])['items']
    sleep(randint(8,12))

    
# dataframe from top tags and answer score
tags=pd.DataFrame(tags)
indicator=pd.get_dummies(tags['tag_name'])
indicator=indicator[indicator.columns].multiply(tags["answer_score"], axis="index")
indicator['user_id']=tags['user_id']
indicator=indicator.groupby('user_id').sum().reset_index()
    

# whole data
users=users.merge(indicator,on='user_id',how='left')


#Dropping sparse columns
users=users[[column for column in users if users[column].astype(bool).sum() / len(test) >= 0.3]]
users.fillna(0,inplace=True)
