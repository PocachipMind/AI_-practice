import glob
import os

def image_szie(path) :

    all_label = os.listdir(path)
    
    print(all_label) 
    # ['african-wildcat', 'blackfoot-cat', 'chinese-mountain-cat', 'domestic-cat', 'european-wildcat', 'jungle-cat', 'sand-cat']

    # folder image size

    for i in all_label:
        locals()[i] = glob.glob(os.path.join(path, i,"*.jpg"))


    # show print
    for i in all_label:
        print(f"{i} >> {len(locals()[i])}")
    pass

path = './data'
image_szie(path)
