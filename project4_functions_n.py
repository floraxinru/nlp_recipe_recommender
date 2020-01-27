import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def regex_nodigits_new(s):
    '''use regex to clean string: 
    get rid of punctuations, capitalized letters and numbers'''
    s = re.sub(r'[\d]','',str(s))#replace digits with empty str
    return s #only returning ingredients of first recipe?

def regex_noads(s):
    #s = re.sub(r'[^\w\s]','',str(df[col])) #replaces anything not alphanumeric or whitespace with empty str
    s = re.sub(r'["ADVERTISEMENT"]','',str(s))#replace the word "ADVERTISEMENT"--also replaced capital letters
    return s
    ##*for re.sub, always change input to strings with str() (wouldn't hurt if it's already a string)

##better coding practice to put it in this ftn instead of jupyter, but not priority rn
def get_rec(title, data, n=3):    
    '''takes in a recipe r, and outputs recommendedations of 
    the n recipes with the highest cosine similarity to r'''
    
    reclist = []

    data.loc[data.title == 'title'].index

    #find doc_id of recipe r in lsa output:
    # doc_id = where title = data.title.iloc[doc_id] 
    r.title
    #Alt. use lsa for rec that makes sense, nmf for surprises?
    cos_sim = cosine_similarity(lem_topic[doc_id].reshape(1, -1),lem_topic).round(3) #LSA

    most_to_least=(-cos_sim).argsort() #array of most- to least- similar recipes based on cos_sim with doc_id
    for i in most_to_least: #
        reclit.append(data.title.iloc[i]) #do we want ingredients/instructions also? clickable? auto search?
    #get name
    return reclist


    #from topic modelling/LSA/NMF lecture
def display_topics(model, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


    #from Kmeans Clustering lecture
# helper function that allows us to display data in 2 dimensions an highlights the clusters
def display_cluster(X,km=[],num_clusters=0):
    import matplotlib.pyplot as plt

    color = 'brgcmyk'
    alpha = 0.3
    s = 20
    if num_clusters == 0:
        plt.scatter(X[:,0],X[:,1],c = color[0],alpha = alpha,s = s)
    else:
        for i in range(num_clusters):
            plt.scatter(X[km.labels_==i,0],X[km.labels_==i,1],c = color[i],alpha = alpha,s=s)
            plt.scatter(km.cluster_centers_[i][0],km.cluster_centers_[i][1],c = color[i], marker = 'x', s = 100)
            #get error: string index out of range? -- took this out of lecture, modify code! also change colours