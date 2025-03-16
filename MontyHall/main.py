from manim import *


class MontyHall(Scene):
    def construct(self):
        door_width, door_height, door_gap = 2, 4.9, 2
        door1 = Rectangle(width=door_width, height=door_height, color=WHITE)
        door2 = Rectangle(width=door_width, height=door_height, color=WHITE)
        door3 = Rectangle(width=door_width, height=door_height, color=WHITE)
        door1.shift(LEFT * (door_width + door_gap))
        door2.shift(ORIGIN)
        door3.shift(RIGHT * (door_width + door_gap))

        lab1 = Text("1/3", font_size=32, color=BLACK).move_to(door1.get_center())
        lab3 = Text("1/3", font_size=32, color=BLACK).move_to(door3.get_center())

        door1_group = VGroup(door1, lab1)
        door2_group = VGroup(door2)
        door3_group = VGroup(door3, lab3)

        self.play(
            FadeIn(door1_group), FadeIn(door2_group), FadeIn(door3_group), run_time=2
        )
        self.wait(1)

        d1_number = Text("1", font_size=44, color=WHITE).next_to(door1, UP)
        d2_number = Text("2", font_size=44, color=WHITE).next_to(door2, UP)
        d3_number = Text("3", font_size=44, color=WHITE).next_to(door3, UP)
        self.play(Write(d1_number), Write(d2_number), Write(d3_number), run_time=1)
        self.wait(2)
        self.play(
            FadeOut(d1_number), FadeOut(d2_number), FadeOut(d3_number), run_time=1
        )

        self.play(
            door1.animate.set_color(BLUE), lab1.animate.set_color(BLUE), run_time=1
        )
        you_chose = Text("You chose door 1", font_size=38, color=WHITE).next_to(
            door1_group, DOWN
        )
        self.play(Write(you_chose), run_time=1)
        self.wait(1)
        self.play(FadeOut(you_chose), run_time=1)

        reveal_text = Text("The host opens door 3...", font_size=38).next_to(
            door3_group, DOWN
        )
        self.play(Write(reveal_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(reveal_text), run_time=1)

        goat_text = Text("Goat", font_size=42, color=RED).move_to(door3.get_center())
        self.play(
            FadeOut(lab3),
            FadeOut(lab1),
            Write(goat_text),
            door3.animate.set_color(RED),
            run_time=1,
        )
        self.wait(1)

        question = Text(
            "Do you want to switch to door 2\nor stick with door 1?",
            font_size=38,
            color=YELLOW,
        ).to_edge(DOWN)
        self.play(Write(question), door2.animate.set_color(YELLOW), run_time=1)
        self.wait(3)
        self.play(FadeOut(question), run_time=1)

        mis1 = Text("1/2", font_size=36, color=BLUE).move_to(door1.get_center())
        mis2 = Text("1/2", font_size=36, color=YELLOW).move_to(door2.get_center())
        self.play(Write(mis1), Write(mis2), run_time=1)

        misconception = Text(
            "Most think it's 50/50, but it's not!", font_size=38, color=YELLOW
        ).to_edge(UP)
        self.play(Write(misconception), run_time=2)
        self.wait(2)
        self.play(FadeOut(misconception), run_time=1)

        correction = Text(
            "It's actually 66.7% if you switch!", font_size=38, color=YELLOW
        ).to_edge(UP)
        correct1 = Text("1/3", font_size=36, color=RED).move_to(door1.get_center())
        correct2 = Text("2/3", font_size=36, color=GREEN).move_to(door2.get_center())
        self.play(
            Write(correction),
            ReplacementTransform(mis1, correct1),
            ReplacementTransform(mis2, correct2),
            run_time=3,
        )

        self.wait(5)
        self.play(FadeOut(correction), FadeOut(correct1), FadeOut(correct2), run_time=2)

        self.play(
            door1.animate.set_color(RED),
            door2.animate.set_color(GREEN),
            door3.animate.set_color(RED),
            run_time=1,
        )
        reveal1 = Text("Goat", font_size=42, color=RED).move_to(door1.get_center())
        reveal2 = Text("Car", font_size=42, color=GREEN).move_to(door2.get_center())
        self.play(Write(reveal1), Write(reveal2), run_time=2)
        self.wait(5)

        final_message = Text(
            "Switching wins you the car!", font_size=42, color=GREEN
        ).to_edge(DOWN)
        self.play(Write(final_message), run_time=2)
        self.wait(15)
        self.play(FadeOut(final_message), run_time=1)
