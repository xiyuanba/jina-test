from docarray import Document, DocumentArray

da = DocumentArray(
    [
        Document(text='a short phrase'),
        Document(text='word'),
        Document(text='this is a much longer sentence'),
    ]
)
vocab = da.get_vocabulary()
print(vocab)

# encoding
for d in da:
    d.convert_text_to_tensor(vocab, max_length=10)
    print(d.tensor)

# decoding
for d in da:
    d.convert_tensor_to_text(vocab)
    print(d.text)