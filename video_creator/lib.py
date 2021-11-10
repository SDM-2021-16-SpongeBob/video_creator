from cv2 import cv2
import numpy as np


class InputVideo:

    _video = None
    _fps = 0
    _width = 0
    _height = 0

    def __init__(self, video: str) -> None:
        self._video = cv2.VideoCapture(video)
        self._fps = self._video.get(cv2.CAP_PROP_FPS)
        self._width = int(self._video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._height = int(self._video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_video(self):
        return self._video

    def get_fps(self):
        return self._fps

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def read(self):
        return self._video.read()
