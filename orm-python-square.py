class Square:
    
    def __init__(self, initialDim):
        self.dim = initalDim
        
    def getArea (self):
        return self.dim * self.dim

    def setArea (self, area):
        return self.dim = area **0.5
    
    def __str__(self):
        return "Square of dim " + str(self.dim)
    

