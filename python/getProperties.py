import imageio
import visvis as vv

im = imageio.imread('imageio:chelsea.png')
print(im.shape)

im = imageio.imread('http://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png')
vv.imshow(im)
