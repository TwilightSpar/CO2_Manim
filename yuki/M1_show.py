from manim import *


class M1(Scene):
    def construct(self):
        # .shift(UP) 写的初始位置相对屏幕中央上移一个单位
        # (r"",r"")

        # 示例
        # M1_Tis_1 = MathTex(r"V_{tis} \derivative{P_{tis} }{t} = ", r"\frac {M_{tis} } {k} + Q(P_a^*-P_{tis})").shift(UP)
        # Text_consider_nullcline = Tex("let RHS=0, consider stable situation").shift(2 * UP)

        # 公式对象
        M1_formula_1 = MathTex(r"V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a) \tag{1}").shift(UP*3)
        M1_formula_2 = MathTex(r"V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)  \tag{2} ").shift(UP*1.5)
        M1_formula_3 = MathTex(r"V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot}) \tag 3")
        M1_formula_4 = MathTex(r"Q = Q_m+Q_{ot} \tag 4 ").shift(DOWN)
        M1_formula_5 = MathTex(r"P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag 5 ")
        M1_formula_5.next_to(M1_formula_4, DOWN)

        # 展示动画
        self.play(Write(M1_formula_1, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间
        self.play(Write(M1_formula_2, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间
        self.play(Write(M1_formula_3, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间
        self.play(Write(M1_formula_4, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间
        self.play(Write(M1_formula_5, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间

        # R2 = VGroup(M1_formula_4,M1_formula_5)
        self.remove(M1_formula_5, M1_formula_4)
        R1 = VGroup(M1_formula_1, M1_formula_2, M1_formula_3)
        # self.play(R1.animate.scale(0.3))
        # 边缩小，边移动
        self.play(R1.animate.scale(0.3).to_edge(UP + LEFT), run_time=1.5)
        # 先缩小，再移动
        # self.play(R1.animate.scale(0.35), run_time=0.8)
        # self.play(R1.animate.to_edge(UP + LEFT), run_time=0.8)

        self.wait(3)

class M1_PART2(Scene):
    def construct(self):
        # 公式对象 #公式7的两项可以前后换位置？
        M1_formula_9 = MathTex(r" \tau_{tis} = \frac{V_{tis}}{Q}")
        M1_formula_7 = MathTex(r"P_{tis} = P_v", r"=", r"(Q_{ot}", r"P_{ot}", r"+", r"Q_m", r"P_m", r")", r"/Q").shift(UP)
        M1_formula_7L = MathTex(r"\bar P_{tis}(s)", r"=", r"(Q_{ot}", r"\bar P_{ot}(s)", r"+", r"Q_m", r"\bar P_m(s)", r")", r"/Q").next_to(M1_formula_7, DOWN)
        variables = VGroup(MathTex(r"\bar P_{tis}(s)"), MathTex(r"\bar P_{ot}(s)"), MathTex(r"\bar P_m(s)")).arrange_submobjects().next_to(M1_formula_7L, DOWN)

        # 动画 公式9,7
        # self.play(M1_formula_9.animate.to_edge(UP))
        self.play(Write(M1_formula_9))
        self.play(M1_formula_9.animate.to_edge(UP).scale(0.8))

        self.play(Write(M1_formula_7))
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(M1_formula_7, variables), M1_formula_7L))
        self.wait(0.5)
        # self.play(M1_formula_7L.animate.to_edge(UP).shift(DOWN))
        # 移动到M1_formula_9下方
        self.play(M1_formula_7L.animate.next_to(M1_formula_9, DOWN).scale(0.8))
        self.wait(1)

        # 动画 公式2变形
        M1_formula_2 = MathTex(r"V_m ", r"\derivative{P_m}{t}", r" = ", r"\frac {M_m} {k}", r" + ", r"Q_m", r"(", r"P_a^*", r"-", r"P_m", r")")
        M1_formula_2_1 = MathTex(r"V_m ", r"s", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"(", r"\bar P_a^*", r"-", r"\bar P_m(s)", r")")
        variables2 = VGroup(MathTex(r"\bar P_m(s)"), MathTex(r"\bar P_a^*"), MathTex(r"\bar P_m(s)")).arrange_submobjects().next_to(M1_formula_2, DOWN)
        M1_formula_2_2 = MathTex(r"V_m ", r"s", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"\bar P_a^*", r"-", r"Q_m", r"\bar P_m(s)")
        M1_formula_2_3 = MathTex(r"V_m ", r"s", r"\bar P_m(s)", r"+", r"Q_m", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"\bar P_a^*")

        M1_formula_2_change = MathTex(r"\bar P_m(s)", r" =", r" \frac{M_{m}/(ks) + Q_{m}\bar P_a^*} {sV_{m}+Q_{m}}")


        # step 1 代换
        self.play(Write(M1_formula_2))
        self.play(TransformMatchingTex(Group(M1_formula_2, variables2), M1_formula_2_1))
        # step 2 乘法分配律
        self.play(TransformMatchingTex(M1_formula_2_1, M1_formula_2_2))
        # step 3 移项
        self.play(TransformMatchingTex(M1_formula_2_2, M1_formula_2_3))
        self.wait(0.5)
        # step 4 同除
        self.play(TransformMatchingTex(M1_formula_2_3, M1_formula_2_change))

        # 移动到M1_formula_7L下方
        self.play(M1_formula_2_change.animate.next_to(M1_formula_7L, DOWN).scale(0.8))
        self.wait(1)


        # 动画 公式3变形
        M1_formula_3 = MathTex(r"V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot})").next_to(M1_formula_2_change,DOWN)
        variables3 = VGroup(MathTex(r"\bar P_{ot}(s)"), MathTex(r"\bar P_a^*"), MathTex(r"\bar P_{ot}(s)")).arrange_submobjects().next_to(M1_formula_3, DOWN)
        M1_formula_3_change = MathTex(r"\bar P_{ot}(s) = \frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}")

        # 省略过程一步变换
        self.play(Write(M1_formula_3))
        self.play(ReplacementTransform(M1_formula_3, M1_formula_3_change))

        # 移动到M1_formula_2_change下方
        self.play(M1_formula_3_change.animate.next_to(M1_formula_2_change, DOWN).scale(0.8))
        self.wait(1)

        '''# 大括号
        M1_formula_all = MathTex(r"\left\{\begin{aligned}",
                                 r"\bar P_{tis}(s)", r"&=&", r"(Q_{ot}", r"\bar P_{ot}(s)", r"+", r"Q_m", r"\bar P_m(s)", r")", r"/Q \\",
                                 r"\bar P_m(s)", r" &=&", r" \frac{M_{m}/(ks) + Q_{m}\bar P_a^*} {sV_{m}+Q_{m}} \\",
                                 r"\bar P_{ot}(s) &=& \frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}",
                                 r"\end{aligned}\right.")
        R3 = VGroup(M1_formula_7L, M1_formula_2_change, M1_formula_3_change)
        self.play(ReplacementTransform(R3, M1_formula_all))'''

        M1_formula_10 = MathTex(r"\bar P_{tis}(s)=(Q_{ot}\frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}+Q_{m}\frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}})/Q").next_to(M1_formula_3_change, DOWN*2)
        self.play(Write(M1_formula_10))
        self.wait(3)
        # self.play(TransformMatchingTex(M1_formula_7, M1_formula_7))
        '''
        #TransformMatchingTex的官方文档 示例
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)'''


#manim M1_show.py M1 -pqm
#manim M1_show.py M1_PART2 -pqm