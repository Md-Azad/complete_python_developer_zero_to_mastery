from PIL import Image, ImageFilter

img = Image.open('./imeges/img1.JPG')

filtered_img =img.filter(ImageFilter.BLUR) # we can use also (SHARPEN, SMOOTH)

convert_img = img.convert('L')

#convert_img.show()

rotate = img.rotate(90)

rotate.save('rotate_img.png', 'png')

convert_img.save('grey.png', 'png')

#img2 = img.convert("1")
#img2.show()
# to make a image blur
filtered_img.save("blur.png", 'png')

# for resize a image

resize = img.resize((300, 300))

resize.show()
resize.save('resize_img.png', 'png')

# for crop an image

box = (100, 100, 400, 400)

crop = img.crop(box)

crop.save('crop_img.png', 'png')
# crop.show()

print(img)
# use size to know the image size.
print(img.size)
# for color combination.
print(img.mode)

#print(dir(img))