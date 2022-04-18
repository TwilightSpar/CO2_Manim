from manim import *

# Stability Criterion
# 运行命令如下：
# manim TODO7.py Stability -pqm

class Stability(Scene):
    def construct(self):
        formula_22 = MathTex(r"Q\frac{\dd P_s}{\dd t}", r" = ", r"A_sP_s+B_sP^*_s")
        formula_23 = MathTex(r"SI", r"=", r"\frac{2Gt_d(P_{so}-P_I)}{\pi \lambda V_s} = \frac{UF}{SF} < 1")
        Hayes_condition = MathTex(r"\mbox{by Hayes condition:}").to_edge(UP)
        s_1 = MathTex(r"\mbox{S.1: } A_st_d<1")
        s_2 = MathTex(r"\mbox{S.2: } A_s<-B_s").next_to(s_1, DOWN)
        s_3 = MathTex(r"\mbox{S.3: } -B_st_d<\sqrt{(A_st_d)^2 + \rho_1^2};", r"\rho_1", r"\mbox{ is the root of }", r"\rho\cot \rho = A_st_d").next_to(s_2, DOWN)
        s_group = VGroup(s_1, s_2, s_3).scale(0.8).next_to(Hayes_condition, DOWN)

        self.play(Write(formula_22))
        self.play(Write(Hayes_condition))
        self.play(Write(s_group))
        self.wait(2)
        self.play(TransformMatchingTex(formula_22, formula_23))

        self.remove(Hayes_condition)
        self.remove(s_group)
        self.play(Unwrite(formula_23))

        Limitation = MathTex(r"\mbox{Here is all the assumptions: }")
        self.play(Write(Limitation))

        Assumption_group = VGroup(Assumption_1, Assumption_2, Assumption_3, Assumption_4, Assumption_5)
        self.play(Assumption_group.animate.scale(10 / 3).move_to(ORIGIN), run_time=1.5)
