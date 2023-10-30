from PIL import Image
from PIL import GifImagePlugin

gif = Image.open("D:\Projects\Glowy eyes\python stuff\eye.gif")
gifData = gif.load()

gif.seek(1)
print(gif.info['duration'])