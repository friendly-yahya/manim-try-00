from manim import *
import numpy as np

class Video1_BasicLimits(Scene):
    def construct(self):
        # Title
        title = Text("Fundamental Limits", font_size=48, color=BLUE)
        subtitle = Text("Building the Foundation", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

class Scene1_PolynomialLimits(Scene):
    def construct(self):
        # Scene title
        scene_title = Text("Polynomial Limits", font_size=36, color=YELLOW)
        scene_title.to_edge(UP)
        self.play(Write(scene_title))
        
        # Show the basic rule
        rule = MathTex(r"\lim_{x \to a} P(x) = P(a)", font_size=40)
        rule.shift(UP * 2)
        self.play(Write(rule))
        
        # Example
        example = MathTex(r"\lim_{x \to 2} (x^2 - 3x + 1)", font_size=32)
        example.shift(UP)
        self.play(Write(example))
        
        # Solution steps
        step1 = MathTex(r"= 2^2 - 3(2) + 1", font_size=32)
        step2 = MathTex(r"= 4 - 6 + 1", font_size=32)
        step3 = MathTex(r"= -1", font_size=32, color=GREEN)
        
        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT)
        steps.next_to(example, DOWN, buff=0.5)
        
        for step in steps:
            self.play(Write(step))
            self.wait(1)
        
        # Graph visualization
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-3, 5, 1],
            axis_config={"color": WHITE}
        ).scale(0.6).to_corner(DR)
        
        func = axes.plot(lambda x: x**2 - 3*x + 1, color=BLUE)
        point = Dot(axes.coords_to_point(2, -1), color=RED, radius=0.08)
        
        self.play(Create(axes), Create(func))
        self.play(Create(point))
        
        # Highlight the point
        circle = Circle(radius=0.2, color=RED).move_to(point.get_center())
        self.play(Create(circle))
        
        self.wait(3)

class Scene2_RationalLimits(Scene):
    def construct(self):
        scene_title = Text("Rational Function Limits", font_size=36, color=YELLOW)
        scene_title.to_edge(UP)
        self.play(Write(scene_title))
        
        # Indeterminate form example
        problem = MathTex(r"\lim_{x \to 1} \frac{x^2 - 1}{x - 1}", font_size=36)
        problem.shift(UP * 2)
        self.play(Write(problem))
        
        # Show 0/0 form
        indeterminate = MathTex(r"= \frac{0}{0}", font_size=32, color=RED)
        indeterminate.next_to(problem, RIGHT)
        self.play(Write(indeterminate))
        
        # Factoring
        factoring = MathTex(r"= \lim_{x \to 1} \frac{(x-1)(x+1)}{x-1}", font_size=32)
        factoring.next_to(problem, DOWN, buff=0.5)
        self.play(Write(factoring))
        
        # Cancellation
        simplified = MathTex(r"= \lim_{x \to 1} (x+1)", font_size=32)
        simplified.next_to(factoring, DOWN)
        self.play(Write(simplified))
        
        # Final answer
        answer = MathTex(r"= 1 + 1 = 2", font_size=32, color=GREEN)
        answer.next_to(simplified, DOWN)
        self.play(Write(answer))
        
        self.wait(3)

class Scene3_TrigLimits(Scene):
    def construct(self):
        scene_title = Text("Essential Trigonometric Limits", font_size=36, color=YELLOW)
        scene_title.to_edge(UP)
        self.play(Write(scene_title))
        
        # The fundamental trig limit
        fundamental = MathTex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1", font_size=40, color=BLUE)
        fundamental.shift(UP * 1.5)
        self.play(Write(fundamental))
        
        # Related limits
        related1 = MathTex(r"\lim_{x \to 0} \frac{\tan x}{x} = 1", font_size=32)
        related2 = MathTex(r"\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}", font_size=32)
        
        related_group = VGroup(related1, related2).arrange(DOWN, buff=0.5)
        related_group.next_to(fundamental, DOWN, buff=1)
        
        self.play(Write(related1))
        self.play(Write(related2))
        
        self.wait(3)

class Scene4_LimitOperations(Scene):
    def construct(self):
        scene_title = Text("Limit Operations", font_size=36, color=YELLOW)
        scene_title.to_edge(UP)
        self.play(Write(scene_title))
        
        # Rules
        rule1 = MathTex(r"\lim(f + g) = \lim f + \lim g", font_size=28)
        rule2 = MathTex(r"\lim(f \cdot g) = \lim f \cdot \lim g", font_size=28)
        rule3 = MathTex(r"\lim\left(\frac{f}{g}\right) = \frac{\lim f}{\lim g}", font_size=28)
        
        rules = VGroup(rule1, rule2, rule3).arrange(DOWN, buff=0.5)
        rules.shift(UP * 0.5)
        
        for rule in rules:
            self.play(Write(rule))
            self.wait(1)
        
        # Note
        note = Text("(provided limits exist and denominators ≠ 0)", 
                   font_size=20, color=GRAY)
        note.next_to(rules, DOWN, buff=0.3)
        self.play(Write(note))
        
        self.wait(3)