from PIL import Image

def resize(src, trg, size):
    img = Image.open(src)
    img = img.resize(size, Image.ANTIALIAS)
    img.save(trg, 'PNG')