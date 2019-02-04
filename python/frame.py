import imageio

reader = imageio.get_reader('imageio:cockatoo.mp4')
# ffmpeg is used for that
for i, im in enumerate(reader):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))
