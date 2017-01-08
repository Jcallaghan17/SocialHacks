# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Initialize the Stanford Named Entity Recognition Tagger

import pandas as pd
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tag import pos_tag

#st = StanfordNERTagger('./stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz',
#					   './stanford-ner-2015-12-09/stanford-ner.jar',
#					   encoding='utf-8')
 
#Read Email
with open('./example/email1.txt', 'r') as myfile:
  email = myfile.read()

#POStagging

lstTags = nltk.ne_chunk(pos_tag(email.split()))
print (lstTags)

#lstTags = st.tag(email.split())
#print(lstTags)