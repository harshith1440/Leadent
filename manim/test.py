from manim import *

class RationalIntro(Scene):
    def construct(self):

        def hold(t):
            self.wait(t)

        # TOTAL TARGET ≈ 220 seconds

        # -----------------------------
        # 1. Numbers in Daily Life (0–20s)
        # -----------------------------
        nums = VGroup(
            Text("1"), Text("2"), Text("3"),
            Text("-1"), Text("0")
        ).arrange(RIGHT, buff=1)

        self.play(FadeIn(nums), run_time=3)
        hold(17)
        self.play(FadeOut(nums), run_time=1)

        # -----------------------------
        # 2. Not Enough (20–35s)
        # -----------------------------
        txt = Text("Not Enough to Represent All Values")
        self.play(Write(txt), run_time=3)
        hold(12)
        self.play(FadeOut(txt), run_time=1)

        # -----------------------------
        # 3. Fractions Intro (35–55s)
        # -----------------------------
        frac = Text("Fractions → Rational Numbers", font_size=36)
        self.play(Write(frac), run_time=3)
        hold(17)
        self.play(FadeOut(frac), run_time=1)

        # -----------------------------
        # 4. Pens Example (55–85s)
        # -----------------------------
        pens = VGroup(*[Square().scale(0.3) for _ in range(5)]).arrange(RIGHT)
        price = Text("₹22", color=YELLOW).next_to(pens, DOWN)

        self.play(FadeIn(pens), Write(price), run_time=3)
        hold(12)

        division = Text("22 ÷ 5 = 22/5", font_size=36)
        division.next_to(pens, UP)

        self.play(Write(division), run_time=3)
        hold(10)

        self.play(FadeOut(pens), FadeOut(price), FadeOut(division), run_time=1)

        # -----------------------------
        # 5. Not Natural/Integer (85–105s)
        # -----------------------------
        checks = VGroup(
            Text("Natural Number? No"),
            Text("Whole Number? No"),
            Text("Integer? No")
        ).arrange(DOWN)

        self.play(FadeIn(checks), run_time=3)
        hold(17)
        self.play(FadeOut(checks), run_time=1)

        # -----------------------------
        # 6. Temperature Example (105–140s)
        # -----------------------------
        graph = Axes(
            x_range=[0, 5],
            y_range=[-10, 20],
            x_length=5,
            y_length=4
        )

        self.play(Create(graph), run_time=3)

        points = VGroup(
            Dot(graph.c2p(0, 11)),
            Dot(graph.c2p(1, 14)),
            Dot(graph.c2p(2, 17)),
            Dot(graph.c2p(3, 10)),
            Dot(graph.c2p(4, 5))
        )

        self.play(FadeIn(points), run_time=3)
        hold(12)

        frac_vals = Text("3/2 , 1 , -7/4 , -5/3", font_size=30)
        frac_vals.next_to(graph, DOWN)

        self.play(Write(frac_vals), run_time=3)
        hold(11)

        self.play(FadeOut(graph), FadeOut(points), FadeOut(frac_vals), run_time=1)

        # -----------------------------
        # 7. Rational Numbers Concept (140–160s)
        # -----------------------------
        rn = Text("Rational Numbers", color=BLUE)
        self.play(Write(rn), run_time=3)
        hold(17)
        self.play(FadeOut(rn), run_time=1)

        # -----------------------------
        # 8. Definition (160–180s)
        # -----------------------------
        formula = Text("p / q   (q ≠ 0)", font_size=36)
        self.play(Write(formula), run_time=3)
        hold(17)
        self.play(FadeOut(formula), run_time=1)

        # -----------------------------
        # 9. Examples (180–200s)
        # -----------------------------
        examples = Text("4/3 , 9/7 , -17/10 , -2/3", font_size=34)
        self.play(Write(examples), run_time=3)
        hold(17)
        self.play(FadeOut(examples), run_time=1)

        # -----------------------------
        # 10. All Numbers → Rational (200–215s)
        # -----------------------------
        mapping = VGroup(
            Text("5 = 5/1"),
            Text("0 = 0/1"),
            Text("-3 = -3/1")
        ).arrange(DOWN)

        self.play(FadeIn(mapping), run_time=3)
        hold(11)
        self.play(FadeOut(mapping), run_time=1)

        # -----------------------------
        # 11. Final Understanding (215–220s)
        # -----------------------------
        end = Text("Foundation of Mathematics", font_size=40)
        self.play(Write(end), run_time=2)
        hold(3)