from docarray import Document

d = Document(uri='apple.png')
d.load_uri_to_image_tensor()

print(d.tensor, d.tensor.shape)