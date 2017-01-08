from sklearn.externals import joblib
import pandas as pd
import scipy

text_clf = joblib.load('text_clf.pkl')

with open('./example/email3.txt', 'r') as myfile:
  email = myfile.read()

print(text_clf.predict([email]))