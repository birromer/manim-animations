from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3*TAU/8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class CircleToSquare(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.3)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        self.play(Create(blue_circle))
        self.wait()

        self.play(Transform(blue_circle, green_square))
        self.wait()

class ObjectsWithArrow(Scene):
    def construct(self):
        obj_1 = Circle(radius=0.2, color=BLUE_A, fill_opacity=1)
        obj_2 = Circle(radius=0.2, color=BLUE_B, fill_opacity=1)
        arrow = Arrow(buff=0.1, stroke_width=5.0, max_tip_length_to_length_ratio=0.5)
        arrow_label = Text("f").scale(0.75)
        arrow_label.next_to(arrow, DOWN, buff=0.1)

        obj_1 = obj_1.next_to(arrow, LEFT)
        obj_2 = obj_2.next_to(arrow, RIGHT)

        self.play(Create(obj_1), Create(obj_2))
        self.wait(0.2)
        self.play(Create(arrow), Write(arrow_label))
        self.wait()

        group_cat = Group(obj_1, obj_2, arrow, arrow_label)
        text_cat = Text("This is the category of sets!")

        self.play(group_cat.animate.next_to(text_cat, DOWN, buff=0.5))
        self.wait(3)
