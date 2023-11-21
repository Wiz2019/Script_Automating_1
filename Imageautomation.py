from PIL import Image, ImageEnhance, ImageFilter
import os

path = r'C:\Users\1yash\Pictures\Image automated script _original'
pathOut = r'C:\Users\1yash\Pictures\Image automated script'

for filename in os.listdir(path):
    try:
        img = Image.open(f"{path}/{filename}")
    except (IOError, OSError, Image.UnidentifiedImageError):
        # Skip non-image files
        continue

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
