#class shape
class Rectangle():
    #https://pygame.readthedocs.io/en/latest/4_text/text.html
    def __init__(self, left, top, width, height):        
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        
    def set_Left (self, left):
        self.left = left        
    def get_Left(self):
        return self.left
    
    def set_Top(self, top):
        self.top = top
    def get_Top(self):
        return self.top
    
    def set_Width(self, width):
        self.width = width
    def get_Width(self):
        return self.width
    
    def set_Height(self, height):
        self.height = height
    def get_Height(self):
        return self.height
    
    