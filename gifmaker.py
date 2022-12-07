from PIL import Image

images = []
images.append(Image.open('IMG_8007.jpg'))
images.append(Image.open('IMG_8008.jpg'))
images.append(Image.open('IMG_8009.jpg'))
images.append(Image.open('IMG_8010.jpg'))
images.append(Image.open('IMG_8009.jpg'))
images.append(Image.open('IMG_8008.jpg'))




images[0].save('mygif.gif', save_all=True, append_images=images[1:], optimize=False, duration=10, loop=0)
