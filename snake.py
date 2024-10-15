from turtle import Turtle,Screen
screen = Screen()
COORDINATE = [(0, 0), (-20, 0), (-40, 0)]
DIRECTION = {
    "Up" : 90,
    "Down" : 270,
    "Left" : 180,
    "Right" : 0
}
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for x in COORDINATE:
            self.create_segment(x)


    def create_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.create_segment(self.segment[-1].position())


    def move(self):
        for position in range(len(self.segment)-1, 0, -1):
            new_xcor = self.segment[position - 1].xcor()
            new_ycor = self.segment[position - 1].ycor()
            self.segment[position].goto(new_xcor, new_ycor)
        self.head.speed(0)
        self.head.fd(20)


    def boundaries_tail(self):
        for body in self.segment[1:]:
            if self.head.distance(body) < 15:
                return 0
    def boundaries_wall(self):
        if self.head.xcor() > 289 or self.head.ycor() > 290 or \
                self.head.xcor() < -299 or self.head.ycor() < -289:
            return 0

    def boundaries(self):
        if self.boundaries_tail() == 0 or self.boundaries_wall() == 0:
            return False
        else:
            return True



    def go_up(self):
        if self.head.heading() != DIRECTION["Down"]:
            self.head.setheading(DIRECTION["Up"])

    def go_right(self):
        if self.head.heading() != DIRECTION["Left"]:
            self.head.setheading(DIRECTION["Right"])

    def go_down(self):
        if self.head.heading() != DIRECTION["Up"]:
            self.head.setheading(DIRECTION["Down"])

    def go_left(self):
        if self.head.heading() != DIRECTION["Right"]:
            self.head.setheading(DIRECTION["Left"])
