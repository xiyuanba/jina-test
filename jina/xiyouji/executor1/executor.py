from jina import Executor, requests, DocumentArray,Document
import torch
import numpy as np


class MyExecutor(Executor):
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        docs[0].text = 'hello, world!'
        docs[1].text = 'goodbye, world!'

    @requests(on='/index_books')
    def index(self, docs: DocumentArray, **kwargs):
        print('输入到Executor的文本为："{}"'.format(docs[0].text))
        # docs[0].text = 'hello jina'
        # for doc in docs:
        #     doc.tensor = torch.tensor(np.random.random([10, 2]))

# Exec = MyExecutor()
# data = DocumentArray(Document(text='向世界问好！'))
# print('准备向Executor输入文本："{}"'.format(data[0].text))
# Exec.index(data)
# print('经过Executor的洗礼后，文本变成了："{}"'.format(data[0].text))