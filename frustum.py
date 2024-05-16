from settings import *

class Frustum:
    def __init__(self, camera):
        self.cam: Camera =  camera
        
    def is_on_frustum(self, chunk):
        return True