from docarray import DocumentArray
from urllib3.exceptions import HTTPError


da = DocumentArray.from_files('/home/yingtie/Pictures/images/*.jpg')
da.plot_image_sprites('sprite-img.png')