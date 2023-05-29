from docarray import Document,DocumentArray

# d = Document(uri='https://www.w3.org/History/19921103-hypertext/hypertext/README.html')
#d = Document(text='👋	नमस्ते दुनिया!	你好世界！こんにちは世界！	Привет мир!')
# d.load_uri_to_text()
da = DocumentArray(storage="sqlite",config={'connection': 'eqsy_use.db','table_name': 'mine'})
# da.append(d)
#da.append(Document(text='hello world!'))
#da.append(d)
# d.summary()
da.summary()
for i in da:
    print(i.text)

q = (
    Document(text="世界",tags="test").embed_feature_hashing().match(da,limit=1,exclude_self=True,use_scipy=True)
)

print(q.matchs[:,('text','score__jaccard')])