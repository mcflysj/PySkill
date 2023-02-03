# 图像优化
# pip install Pillow
import PIL
# Croping
im = PIL.Image.open("Image1.jpg")
im = im.crop((34, 23, 100, 100))
# Resizing
im = PIL.Image.open("Image1.jpg")
im = im.resize((50, 50))
# Flipping
im = PIL.Image.open("Image1.jpg")
im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
# Rotating
im = PIL.Image.open("Image1.jpg")
im = im.rotate(360)
# Compressing
im = PIL.Image.open("Image1.jpg")
im.save("Image1.jpg", optimize=True, quality=90)
# Bluring
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.BLUR)
# Sharpening
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.SHARPEN)
# Set Brightness
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Brightness(im)
im = im.enhance(1.5)
# Set Contrast
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Contrast(im)
im = im.enhance(1.5)
# Adding Filters
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageOps.grayscale(im)
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.posterize(im, 4)
# Saving
im.save("Image1.jpg")