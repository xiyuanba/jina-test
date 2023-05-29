from docarray import Document, DocumentArray
from tqdm import tqdm
from text2vec import SentenceModel, EncoderType
import numpy as np
from pprint import pprint
#import os
#text2vec在调用模型时要访问huggingface.co，如网络质量不好会导致无法调用模型，此次请想办法科学上网
#os.environ["http_proxy"] = "http://ip:port"
#os.environ["https_proxy"] = "http://ip:port"

with open('./xiyouji.txt', encoding='utf-8') as f:
    txt = f.read()
# d = Document(text=txt)
da = DocumentArray(
    storage='sqlite', config={'connection': 'example.db', 'table_name': 'xiyouji'}
)
model = SentenceModel("shibing624/text2vec-base-chinese", encoder_type=EncoderType.FIRST_LAST_AVG, device = 'cpu')
feature_vec = model.encode
for s in tqdm(txt.split('\n')):
    if s.strip():
        d = Document(text=s)
        d.embedding = feature_vec(d.text)
        da.append(d)
        print(s)
        print(d.summary())
        print(d.embedding)
# text = Document(text='悟彻菩提真妙理')  # 要匹配的文本
# text.embedding = feature_vec(text.text)
# q = text.match(da, limit=10, exclude_self=True, metric='cos', use_scipy=True)  # 找到与输入的文本最相似的句子
# pprint(q.matches[:, ('text', 'scores__cos')]) # 输出对应的文本与 cos 相似性分数