"""#Image Type Converter 


Types of images formats:

https://en.wikipedia.org/wiki/Image_file_formats


PIL - image type converter lib used for python2

pillow lib. - used for python3.
https://pypi.org/project/Pillow/

golb lib. - Unix style path manipulation. https://docs.python.org/3/library/glob.html
"""

pip install Pillow

from PIL import Image  # Python Image Library - Image Processing 

import glob
print(glob.glob("*.png"))

"""Note: jpg to png im.convert('RGBA') 

A stands here for alpha. 
"""

# based on SO Answer: https://stackoverflow.com/a/43258974/5086335
for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95)



# '''
# import os
# for file in glob.glob("*.jpg"):
#     os.remove(file)
# '''