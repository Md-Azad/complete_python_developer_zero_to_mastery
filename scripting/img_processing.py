from PIL import Image

image = Image.open('./imeges/img2.JPG')

new_image = image.resize((400, 400))
new_img = new_image.rotate(90)
new_img.save('thumbnail.jpg')

print(new_image.size)

