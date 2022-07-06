class Points1:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Points1(10, 20)
print(point1.x)
