# clickbait-detector 

A simple flask server with classifier is deployed on - http://clickbait.pythonanywhere.com/ 

Blog post about it - https://shubhamkalra27.github.io/clickbait-detector/ 

Repository is pretty self explainatory - a quick introduction for forgetful future me

`model.ipynb` walks you through training and testing the model - scoring and accuracy added too 
`model_1.pkl` stores the serialised sklearn object which is used for predictions 
`runner.py` & `main.py` helps host the flask app and do a runtime scoring

## Science
* The clickbait corpus consists of article headlines from ‘BuzzFeed’, ‘Upworthy’, ‘ViralNova’, ‘Thatscoop’, ‘Scoopwhoop’ and ‘ViralStories’. 
* The non-clickbait article headlines are collected from ‘WikiNews’, ’New York Times’, ‘The Guardian’, and ‘The Hindu’.
* Added data in a Pandas dataframe with shuffling
* Tried couple of pipelines - the production pipeline contains `Pipeline([('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),('mnb', MultinomialNB())])`



## Future - 
* If the tool reaches a significant audience. I would be happy to wrap it in a AWS lambda function and call it from a chrome extension- which looks for articles on google news, facebook etc. - for a more significant usage. 
* If you think so too - let me know at [@shubhamkalra27](https://twitter.com/shubhamkalra27) 

## References
* Training data has been used from this [study](http://cse.iitkgp.ac.in/~abhijnan/papers/chakraborty_clickbait_asonam16.pdf) - data posted [here](https://github.com/bhargaviparanjape/clickbait/tree/master/dataset)
