from PIL import Image, ImageEnchance, ImageFilter
import os

path = './imgs' #enter the path for your images to taken for editting 
pathOut = '/editedImgs' #enter the path you want you want to store your edited photos 

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnchance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
