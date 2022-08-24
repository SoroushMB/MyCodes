from PIL import Image, ImageFilter

before = Image.open("846664.jpg")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("after.jpg")