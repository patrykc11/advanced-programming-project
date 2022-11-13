from PIL import Image
import PIL.ImageOps
import io

def invert(img):
    inverted_image = PIL.ImageOps.invert(Image.open(io.BytesIO(img)))
    buf = io.BytesIO()
    inverted_image.save(buf, format='JPEG')
    buf.seek(0)
    return buf
