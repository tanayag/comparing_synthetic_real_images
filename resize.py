folder = './cvidea/classification_dataset/synthetic_images'

from PIL import Image
import os

c=0
for i in os.listdir(folder):
    try:
        img = Image.open(folder+"/"+i)
        img = img.resize((224, 224), Image.ANTIALIAS)
        img.save(folder+"/"+i)
    except:
        os.unlink(folder+"/"+i)
        c+=1
print '\n\nTotal Removed'
print c
