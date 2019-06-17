#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

from SVM_model import SVMModel
from dulieu import dulieu


class TextClassificationPredict(object):
    def __init__(self):
        self.test = None

    def get_train_data(self, str):
        # Tạo train data
        train_data = []
        train_data = dulieanningu.data('ahihi')
        df_train = pd.DataFrame(train_data)

        # Tạo test data
        test_data = []
        test_data.append({"feature": str})
        df_test = pd.DataFrame(test_data)

        # init model naive bayes

        model = SVMModel()

        clf = model.clf.fit(df_train.feature, df_train.target)

        predicted = clf.predict(df_test["feature"])
        print(clf.predict_proba(df_test["feature"])[0])
        # Print predicted result
        print(predicted)
        print(dulieu.output(predicted[0],str))






if __name__ == '__main__':
    print('xin chào')
    t= True
    f = open('phattrien.txt', 'a', encoding='utf-8')
    while(t):
        str = input()
        tcp = TextClassificationPredict()
        tcp.get_train_data(str)
        if str == "ahihi":
            t = False
        f.write(str + '\n')

    f.close()
