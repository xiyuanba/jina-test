from docarray import Document

#doc = Document(uri='Kaws.glb').load_uri_to_vertices_and_faces()
doc = Document(uri='Kaws.glb').load_uri_to_point_cloud_tensor(samples=30000)
doc.load_uris_to_rgbd_tensor()
#doc.summary()
print(doc.tensor.shape)
for chunk in doc.chunks:
    print(f'chunk.tags = {chunk.tags}')
doc.display()