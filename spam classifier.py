import pandas as pd
import re
import nltk

message = pd.read_csv('SMSSpamCollection',sep='\t',names=["label","Message"])

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []

for i in range(len(message)):
    review = re.sub('[^a-zA-Z]',' ',message['Message'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
x = cv.fit_transform(corpus)

y = pd.get_dummies(message['label'],drop_first=True)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import MultinomialNB
spam_classifier = MultinomialNB().fit(x_train,y_train)

y_pred = spam_classifier.predict(x_test)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)





    
    
    


