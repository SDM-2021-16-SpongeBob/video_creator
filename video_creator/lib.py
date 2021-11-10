from cv2 import cv2
import numpy as np


class InputVideo:

    video = None
    fps = 0
    width = 0
    height = 0

    def __init__(self, video: str) -> None:
        self.video = cv2.VideoCapture(video)
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
