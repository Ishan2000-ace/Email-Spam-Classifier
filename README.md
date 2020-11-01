# Email-Spam-Classifier
## Overview of the Project
We recieve many spam emails and SMS daily and some of them are sent by fraud people and if we are trapped then in most of the cases we loose our hard earned money or our personal data can be 
compromised. I tried to stop this by creating this web app based on NLP. In this app we just have to enter the message that we got and it will tell us whether the message is spam 
or a ham.

## Data Collection
I got the dataset from kaggle. It can be downloaded from this link [SMS Spam Collection](https://www.kaggle.com/uciml/sms-spam-collection-dataset).

## Data Preprocessing and Machine Learning Techiques Used
In Natural Language Processing first we have to preprocess the text data that we have by removing all the  stopwords for,if,but etc that has no use in analysis. After that we have
to convert upper case character into lower case by using regular expression because machine considers upper case characters and lower case characters differently but actually they 
are same. We use regular expression for this purpose. After this we have to convert all the text data because the Machine learning algorithm will not understand text data


