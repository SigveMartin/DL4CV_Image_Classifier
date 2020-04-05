# import the nexessary packages
import numpy as np
import cv2
import os

class SimpleDatasetLoader:
    def __init__(self,preprocessors=None):
        # store the image preprocessor
        self.preprocessors = preprocessors

        # if the preprocessors are None, initialize them as emplty list
        if self.preprocessors is None:
            self.preprocessors = 
