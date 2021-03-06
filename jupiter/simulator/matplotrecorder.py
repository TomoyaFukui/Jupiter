"""
imported from https://github.com/AtsushiSakai/matplotrecorder

A simple Python module for recording matplotlib animation

This tool use convert command of ImageMagick

author: Atsushi Sakai

How to use:

- import

    from matplotrecorder import matplotrecorder

- save file

    matplotrecorder.save_frame()

- generate movie

    matplotrecorder.save_movie("animation.gif", 0.1)
"""

import matplotlib.pyplot as plt
import subprocess
import os
LOGPATH = os.path.dirname(os.path.abspath(__file__)) + "/../"

iframe = 0
donothing = False  # switch to stop all recordering


def save_frame():
    """Save a frame for movie"""
    if not donothing:
        global iframe
        plt.savefig(LOGPATH + "pictures/recoder" +
                    '{0:04d}'.format(iframe) + '.png')
        iframe += 1


def save_movie(fname, d_pause, monitor=True):
    """
    Save movie as gif
    """
    if not donothing:
        if monitor:
            cmd = "convert -monitor -delay " + str(int(d_pause * 100)) + \
                " pictures/recoder*.png " + fname
        else:
            cmd = "convert -delay " + str(int(d_pause * 100)) + \
                " pictures/recoder*.png " + fname

        subprocess.call(cmd, shell=True)
        # cmd = "rm pictures/recoder*.png"
        # subprocess.call(cmd, shell=True)


# if __name__ == '__main__':
#     print("A sample recording start")
#     import math
#
#     time = range(50)
#
#     x1 = [math.cos(t / 10.0) for t in time]
#     y1 = [math.sin(t / 10.0) for t in time]
#     x2 = [math.cos(t / 10.0) + 2 for t in time]
#     y2 = [math.sin(t / 10.0) + 2 for t in time]
#
#     for ix1, iy1, ix2, iy2 in zip(x1, y1, x2, y2):
#         plt.plot(ix1, iy1, "xr")
#         plt.plot(ix2, iy2, "xb")
#         plt.axis("equal")
#         plt.pause(0.1)
#
#         save_frame()  # save each frame
#
#     save_movie(LOGPATH + "movies/animation.gif", 0.1)
#     #  save_movie("animation.mp4", 0.1)
