class Snake:

    def __init__(self,defcount):
        self.Count = defcount 
        self.Width = int(10)
        self.Height = int(10)
        self.Color = "red"
        self.Body = []
        self.Xstart = int(250)
        self.Ystart = int(250)