from docarray import Document

d = Document(uri='./complicated-image.jpeg')
d.load_uri_to_image_tensor()
print(d.tensor.shape)

# d.convert_image_tensor_to_sliding_windows(window_shape=(64, 64))
print(d.tensor.shape)

# d.convert_image_tensor_to_sliding_windows(window_shape=(64, 64), as_chunks=True)

print(d.chunks)