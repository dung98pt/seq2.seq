from thoigian import thoigian
import os
from pyvi import ViTokenizer, ViPosTagger
import re
import numpy as np
from s2s_model import s2s
data = []

path ='./dulieu/'
target = os.listdir(os.path.expanduser(path))


for i in target:
    with open(path+i + '/data/from.txt', 'r', encoding='utf-8') as fopen:
        text_from = fopen.read().lower()
        text_from = re.sub('[“”!@#$]', '', text_from)
        text_from = text_from.split('\n')
        for j in text_from:
            data.append({"feature": j, "target": i})




class dulieu:
    def __init__(self):
        pass
    def output(str1, str2):
        output = {
            'hoi_thoi_tiet': "hôm nay trời đẹp lắm!",
            'tam_biet': 'Hẹn gặp lại sau nhé.',
            'chui_rua': 'ahuhu đồ ngốc',
            'chao_hoi': 'Xin chào, mình có thể giúp gì cho bạn',
            'hoi_gio': thoigian.ntd('gio'),
            'hoi_ngay': thoigian.ntd('ngay'),
            'tt_ca_nhan': s2s.prediction('tt_ca_nhan',str2)
        }
        return output[str1]

    def data(str):
        return data

