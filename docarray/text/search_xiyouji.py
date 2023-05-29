from docarray import Document, DocumentArray
from tqdm import tqdm
from text2vec import SentenceModel, EncoderType
import numpy as np
from pprint import pprint
#import os



da = DocumentArray(
    storage='sqlite', config={'connection': 'example.db', 'table_name': 'xiyouji'}
)
model = SentenceModel("shibing624/text2vec-base-chinese", encoder_type=EncoderType.FIRST_LAST_AVG, device = 'cpu')
feature_vec = model.encode

text = Document(text='三打白骨精')  # 要匹配的文本
text.embedding = feature_vec(text.text)
q = text.match(da, limit=10, exclude_self=True, metric='cos', use_scipy=True)  # 找到与输入的文本最相似的句子
pprint(q.matches[:, ('text', 'scores__cos')]) # 输出对应的文本与 cos 相似性分数


