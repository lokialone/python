import os
from PIL import Image,ImageFilter

def resize_image():
    #get all file
    img_path = "/Users/lokalone/code/tech/python/img"
    pic_dir = '/Users/lokalone/code/tech/python/deal_img'
    files = os.listdir(img_path)
    path = os.getcwd()
    width = 600
    #change dir path
    os.chdir(img_path)

    for file in files:
        print(file)
        img = Image.open(file)
        out = img.resize((width,width),Image.ANTIALIAS)
        print(img)
        new_name = os.path.join(pic_dir, file)
        out.save(new_name,'jpeg')
resize_image()
