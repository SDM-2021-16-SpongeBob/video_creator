from cv2 import cv2
import numpy as np


class Video:

    _video = None
    _fps = 0
    _width = 0
    _height = 0

    def get_video(self):
        return self._video

    def get_fps(self):
        return self._fps

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


class InputVideo(Video):

    def __init__(self, video: str) -> None:
        self._video = cv2.VideoCapture(video)
        self._fps = self._video.get(cv2.CAP_PROP_FPS)
        self._width = int(self._video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._height = int(self._video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def read(self):
        return self._video.read()


class OutputVideo(Video):

    _video_queue = []

    def __init__(self, video: str) -> None:
        self._video = video

    def input(self, video: Video):
        self._video_queue.append(video)
        self._width = self._width + video.get_width()
        for v in self._video_queue:
            old_height = self._height
            old_fps = self._fps
            new_height = v.get_height()
            new_fps = v.get_fps()
            self._height = new_height if new_height > old_height else old_height
            self._fps = new_fps if new_fps < old_fps else old_fps
