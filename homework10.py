from PIL import Image
import numpy as np

# make red flower
def makered():
    i = Image.open('flower.jpg')
    dim = np.zeros((i.size[1], i.size[0]), 'int8')

    img_zero = Image.fromarray(dim, 'L')
    img = Image.merge('RGB', (i, img_zero, img_zero)) # in this variant will be easy to encode
    img.save('redflower.bmp') # (!) important to use bmp; jpg does some image conversion while saving
    # other options to save are, e.g.:      scipy.misc.toimage(numpytable, cmin=0, cmax=255).save(stringfilename)
makered()

def decode(img_path):
  I = Image.open(img_path)
  crypto_array = np.array(I)
  row7_blue = crypto_array[7, :, 2] # The message is violet so we need to look in the blue layer (third dimension)
  ascii_r7 = row7_blue[row7_blue != 0]
  hidden_message = ''.join([chr(val) for val in ascii_r7])
  print(hidden_message)
decode('crypto.bmp')

def encode(img_path,message_str):
  I = Image.open(img_path)
  crypto_array = np.array(I)
  dim = np.zeros((I.size[1], I.size[0]), 'int8')
  img_zero = Image.fromarray(dim, 'L')
  dim[7,:len(message_str)] = np.array([ord(val) for val in message_str])
  img2 = Image.fromarray(dim, 'L')
  img = Image.merge('RGB', (Image.fromarray(crypto_array[:,:,0], 'L'), img_zero,img2))
  img.save('crypto2.bmp')
encode('redflower.bmp','message')
decode('crypto2.bmp')
