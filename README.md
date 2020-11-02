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
are same. We use regular expression for this purpose. After this we have to convert all the text data because the Machine learning algorithm will not understand text data. Here we
converted all the text data into vectors. There are several techniques to do that and used count vectorizer for conversion into vectors. Then we use Multinominal class of Naive Baise Classifier to understand the relationship between dependent and independent features.
![Naive baise](https://i0.wp.com/syncedreview.com/wp-content/uploads/2017/07/naive8.png?fit=531%2C327&ssl=1)
![Countvectorizer](https://kavita-ganesan.com/wp-content/uploads/image-5.png)
![NLTK](https://clay-atlas.com/wp-content/uploads/2019/08/python_nltk.png)

## Deployment of the Model
This model is deployed by using flask framework of python that is used for backend development of web. HTML and CSS has been used for the frontend UI. This app is being hosted on 
Heroku cloud which is considerd as platform as a service. This app can be viewed,used and tested directly by clicking at:[spam Classifier](https://spamclassifier02.herokuapp.com/)
![Heroku](https://a.slack-edge.com/bfaba/img/api/hosting_heroku.png)
![Flask](https://avatars1.githubusercontent.com/u/18305767)

## Installation Details
Steps for Installation:
1. First we have to download Anaconda we can visit the page directly by clicking at [Anaconda Download](https://www.anaconda.com/products/individual)
Here we have scroll to the bottom and we can see installers for various opearating systems. We have to choose according to our system requirements.
This step can be skipped if anaconda is already installed.

2. In anaconda prompt create a new environment by the following command:
```conda create --name myenv```

3. After creating a new environment it is activated by following command: ```conda activate myenv'''

4. Now we have to navigate to directory where we have downloaded this repository and we have to it via anaconda prompt using command: ```cd path of the directory``` 

5. After navigating to the directory we have to install the dependencies of this project by using a file that is called requirements.txt that I have already provided in 
my repository and the dependencies can be installed by using command ```pip install requirements.txt```
but this command must be executed after executing step 4 otherwise it will won't work.

6. To run this app in the local machine we have to use the command:```python app.py```
After execution it will give a local address just copy that and paste that in the address bar of the browser and the web app is ready to use.

## Credits
Credits of this project goes to krish Naik sir's YouToube channel. Lead data scientist at Ineuron. His videos were a great help
[Link of the channel](https://www.youtube.com/user/krishnaik06)

