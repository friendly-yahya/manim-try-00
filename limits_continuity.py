from manim import *
import math

class LimitsAndContinuity(Scene):
    def construct(self):
        # Title
        title = Text("Limites et Continuité", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Part 1: Introduction to Limits
        self.next_section("Introduction to Limits", skip_animations=False)
        
        limit_intro = Text("I. Limite d'une fonction en un point", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(limit_intro))
        self.wait(1)
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 5, 1],
            axis_config={"color": BLUE},
        )
        
        # Create a function with a limit
        def func(x):
            return (x**2 - 1) / (x - 1) if x != 1 else 2
        
        graph = axes.plot(func, color=YELLOW, x_range=[-2.5, 2.5, 0.01])
        
        # Point discontinuity at x=1
        discontinuity = Dot(axes.c2p(1, 2), color=RED)
        open_circle = Circle(radius=0.1, color=RED).move_to(axes.c2p(1, 2))
        
        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(1)
        
        # Highlight the discontinuity
        self.play(Create(open_circle))
        self.play(FadeIn(discontinuity))
        self.wait(1)
        
        # Show the limit using plain text
        limit_text = Text("lim f(x) = 2", font_size=24).next_to(axes, RIGHT, buff=0.5)
        limit_label = Text("lim (x->1) (x^2-1)/(x-1) = 2", font_size=24).next_to(limit_text, DOWN)
        
        self.play(Write(limit_text))
        self.play(Write(limit_label))
        self.wait(2)
        
        # Part 2: Continuity
        self.next_section("Continuity", skip_animations=False)
        
        continuity_title = Text("II. Continuité en un point", font_size=28).next_to(limit_intro, DOWN, buff=0.5)
        self.play(Write(continuity_title))
        self.wait(1)
        
        # Create a continuous function
        def continuous_func(x):
            return x**2
        
        continuous_graph = axes.plot(continuous_func, color=GREEN, x_range=[-2, 2, 0.01])
        
        # Point at x=1
        point = Dot(axes.c2p(1, 1), color=GREEN)
        
        self.play(Transform(graph, continuous_graph), FadeOut(discontinuity), FadeOut(open_circle))
        self.play(Create(point))
        self.wait(1)
        
        # Continuity definition
        continuity_def = Text("f est continue en a si lim f(x) = f(a)", font_size=24).next_to(continuity_title, DOWN, buff=0.5)
        
        self.play(Write(continuity_def))
        self.wait(2)
        
        # Part 3: Intermediate Value Theorem
        self.next_section("Intermediate Value Theorem", skip_animations=False)
        
        ivt_title = Text("Théorème des Valeurs Intermédiaires", font_size=28).next_to(continuity_def, DOWN, buff=0.5)
        self.play(Write(ivt_title))
        self.wait(1)
        
        # Create a function for IVT
        def ivt_func(x):
            return x**3 - 2*x - 1
        
        ivt_graph = axes.plot(ivt_func, color=PURPLE, x_range=[-2, 2, 0.01])
        
        # Points at x=-1 and x=2
        point_a = Dot(axes.c2p(-1, 1), color=RED)
        point_b = Dot(axes.c2p(2, 3), color=RED)
        
        # Horizontal line at y=0
        h_line = Line(start=axes.c2p(-2, 0), end=axes.c2p(2, 0), color=BLUE)
        
        # Intersection point
        intersection = Dot(axes.c2p(1.618, 0), color=YELLOW)  # Approximate root
        
        self.play(Transform(graph, ivt_graph), FadeOut(point))
        self.play(Create(point_a), Create(point_b))
        self.play(Create(h_line))
        self.wait(1)
        
        # IVT statement
        ivt_statement = Text("Si f(a) < 0 < f(b) alors il existe c dans [a,b] tel que f(c)=0", font_size=20).next_to(ivt_title, DOWN, buff=0.5)
        
        self.play(Write(ivt_statement))
        self.wait(1)
        
        # Highlight the intersection
        self.play(Create(intersection))
        self.wait(2)
        
        # Part 4: Operations on Continuous Functions
        self.next_section("Operations on Continuous Functions", skip_animations=False)
        
        ops_title = Text("Opérations sur les fonctions continues", font_size=28).next_to(ivt_statement, DOWN, buff=0.5)
        self.play(Write(ops_title))
        self.wait(1)
        
        # Examples of operations
        sum_text = Text("f + g", font_size=24).shift(LEFT*3)
        prod_text = Text("f * g", font_size=24).shift(LEFT*1)
        comp_text = Text("f o g", font_size=24).shift(RIGHT*1)
        quot_text = Text("f / g", font_size=24).shift(RIGHT*3)
        
        self.play(Write(sum_text), Write(prod_text), Write(comp_text), Write(quot_text))
        self.wait(2)
        
        # Conclusion
        self.next_section("Conclusion", skip_animations=False)
        
        conclusion = Text("Les limites et la continuité sont fondamentales en analyse", font_size=28).next_to(ops_title, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(VGroup(
            title, limit_intro, continuity_title, ivt_title, ops_title, conclusion,
            limit_text, limit_label, continuity_def, ivt_statement,
            sum_text, prod_text, comp_text, quot_text,
            axes, graph, point_a, point_b, h_line, intersection
        )))
        self.wait(1)