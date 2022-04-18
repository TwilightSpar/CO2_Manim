from manim import *

# Stability Criterion
# 运行命令如下：
# manim TODO7.py Stability -pqm

class Stability(Scene):
    def construct(self):
        formula_22 = MathTex(r"Q\frac{\dd P_s}{\dd t}", r" = ", r"A_sP_s+B_sP^*_s")
        formula_23 = MathTex(r"SI", r"=", r"\frac{2Gt_d(P_{so}-P_I)}{\pi \lambda V_s} = \frac{UF}{SF} < 1")
        s_1 = MathTex(r"A_st_d<1")
        s_2 = MathTex(r"A_s<-B_s").next_to(s_1, DOWN)
        s_3 = MathTex(r"-B_st_d<\sqrt{(A_st_d)^2 + \rho_1^2};", r"\rho_1", r"\mbox{ is the root of }", r"\rho\cot \rho = A_st_d").next_to(s_2, DOWN)
        s_group = VGroup(s_1, s_2, s_3).next_to(formula_22, UP).scale(0.8)
        self.play(Write(formula_22))
        self.play(Write(s_group))
        self.play(TransformMatchingTex(formula_22, formula_23))
