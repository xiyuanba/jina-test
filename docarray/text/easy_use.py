from docarray import Document

# d = Document(uri='https://www.w3.org/History/19921103-hypertext/hypertext/README.html')
d = Document(text='👋	नमस्ते दुनिया!	你好世界！こんにちは世界！	Привет мир!')
# d.load_uri_to_text()

d.summary()