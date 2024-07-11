from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "./ImageProcessor/editedImgs"

for filename in os.listdir(path): #Access the files/images in this folder and apply the code
	img = Image.open(f"{path}/{filename}") #holds image object to variable

	edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-180)

	factor = 1.5
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(factor)

	clean_name = os.path.splitext(filename)[0]

	edit.save(f".{pathOut}/{clean_name}_edited.jpg")

