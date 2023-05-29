from jina import Client, DocumentArray,Document

if __name__ == '__main__':
    c = Client(host='grpc://0.0.0.0:54321')
    # da = c.post('/', DocumentArray.empty(2))
    # txt = "你好"
    with open('./xiyouji.txt', encoding='utf-8') as f:
        txt = f.read()

    da = c.post('/index_books', DocumentArray(Document(text=txt)))
    # print(da.texts)
    print("==============")
