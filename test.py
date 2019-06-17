import os
from pyvi import ViTokenizer, ViPosTagger
import re
import numpy as np
path ='./dulieu/'
target = os.listdir(os.path.expanduser(path))
data =[]

for i in target:
    with open(path+i + '/data/from.txt', 'r', encoding='utf-8') as fopen:
        text_from = fopen.read().lower()
        text_from = re.sub('[“”!@#$]', '', text_from)
        text_from = text_from.split('\n')
        for j in text_from:
            data.append({"feature": j, "target": i})
print (data)
