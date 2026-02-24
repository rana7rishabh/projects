import imageio.v3 as iio
import os
files=os.listdir("sample")
image=[]
for file in files:
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        image_path = os.path.join("sample", file)
        image.append(iio.imread(image_path))
iio.imwrite('newGIF.gif', image,duration=500, loop=0)
