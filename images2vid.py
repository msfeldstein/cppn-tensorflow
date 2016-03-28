FFMPEG_BIN = "ffmpeg"
import subprocess as sp
import os
import imageio
import sys
import numpy as np
try:
    from subprocess import DEVNULL  # py3k
except ImportError:
    DEVNULL = open(os.devnull, 'wb')
def writeVideo(filename, images):
    size = images[0].size
    writer = imageio.get_writer(filename, fps=30)
    for image in images:
        writer.append_data(np.asarray(image))
    writer.close()
    print("DONE")