from docarray import DocumentArray, Document

da = DocumentArray(
    [
        Document(text='hello world'),
        Document(text='goodbye world'),
        Document(text='hello goodbye'),
    ]
)

vocab = da.get_vocabulary()
print(vocab)

for d in da:
    d.convert_text_to_tensor(vocab)
    print(d.tensor)
