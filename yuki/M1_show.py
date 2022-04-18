from manim import *


class M1(Scene):
    def construct(self):
        # .shift(UP) 写的初始位置相对屏幕中央上移一个单位
        # (r"",r"")


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

        self.wait(3)


class M1_PART2(Scene):
    def construct(self):
        # Add former assumptions
        Assumption_1 = MathTex(r"\mbox{CO2 is in chemical equilibrium}").scale(0.3).to_edge(UP + RIGHT)
        Assumption_2 = MathTex(r"\mbox{let RHS=0, consider stable situation}").scale(0.3).next_to(Assumption_1, DOWN)
        self.add(Assumption_1, Assumption_2)

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
        self.wait()
        self.play(TransformMatchingTex(Group(M1_formula_7, variables), M1_formula_7L))
        self.wait()
        # self.play(M1_formula_7L.animate.to_edge(UP).shift(DOWN))
        # 移动到M1_formula_9下方
        self.play(M1_formula_7L.animate.next_to(M1_formula_9, DOWN).scale(0.8))
        self.wait()

        # 动画 公式2变形
        M1_formula_2 = MathTex(r"V_m ", r"\derivative{P_m}{t}", r" = ", r"\frac {M_m} {k}", r" + ", r"Q_m", r"(", r"P_a^*", r"-", r"P_m", r")")
        M1_formula_2_a = MathTex(r"V_m ", r"\mathcal {L}(\derivative{P_m}{t})", r" = ", r"\frac {M_m} {k}", r" + ", r"Q_m", r"(",
                               r"\mathcal {L}(P_a^*)", r"-", r"\mathcal {L}(P_m)", r")")

        variables2a = VGroup(MathTex(r"\mathcal {L}(\derivative{P_m}{t})"), MathTex(r"\mathcal {L}(P_a^*)"),
                            MathTex(r"\mathcal {L}(P_m)")).arrange_submobjects().next_to(M1_formula_2, DOWN)
        M1_formula_2_1 = MathTex(r"V_m ", r"s", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"(", r"\bar P_a^*", r"-", r"\bar P_m(s)", r")")
        variables2 = VGroup(MathTex(r"\bar P_m(s)"), MathTex(r"\bar P_a^*"), MathTex(r"\bar P_m(s)")).arrange_submobjects().next_to(M1_formula_2, DOWN)
        M1_formula_2_2 = MathTex(r"V_m ", r"s", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"\bar P_a^*", r"-", r"Q_m", r"\bar P_m(s)")
        M1_formula_2_3 = MathTex(r"(", r"s", r"V_m ", r"+", r"Q_m", r")", r"\bar P_m(s)", r" = ", r"\frac {M_m} {ks}", r" + ", r"Q_m", r"\bar P_a^*")

        M1_formula_2_change = MathTex(r"\bar P_m(s)", r" =", r" \frac{M_{m}/(ks) + Q_{m}\bar P_a^*} {sV_{m}+Q_{m}}")
        Laplace_Transform = MathTex(r"\mathcal{L}(\derivative{P_m}{t})=s\bar P_m(s)-P_m(0)=s\bar P_m(s)").next_to(
            M1_formula_2_a, DOWN)

        # step 1 代换
        self.play(Write(M1_formula_2))
        self.wait()
        self.play(TransformMatchingTex(Group(M1_formula_2, variables2a), M1_formula_2_a))
        self.wait()

        # show laplace transform
        self.play(Write(Laplace_Transform))
        self.wait(2)
        self.remove(Laplace_Transform)
        self.wait()
        self.play(TransformMatchingTex(Group(M1_formula_2_a, variables2), M1_formula_2_1))
        self.wait()

        # step 2 乘法分配律
        self.play(TransformMatchingTex(M1_formula_2_1, M1_formula_2_2))
        # step 3 移项
        self.play(TransformMatchingTex(M1_formula_2_2, M1_formula_2_3))
        self.wait()
        # step 4 同除
        self.play(TransformMatchingTex(M1_formula_2_3, M1_formula_2_change))

        # 移动到M1_formula_7L下方
        self.play(M1_formula_2_change.animate.next_to(M1_formula_7L, DOWN).scale(0.8))
        self.wait()


        # 动画 公式3变形
        M1_formula_3 = MathTex(r"V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot})").next_to(M1_formula_2_change,DOWN)
        variables3 = VGroup(MathTex(r"\bar P_{ot}(s)"), MathTex(r"\bar P_a^*"), MathTex(r"\bar P_{ot}(s)")).arrange_submobjects().next_to(M1_formula_3, DOWN)
        M1_formula_3_change = MathTex(r"\bar P_{ot}(s) = \frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}")

        # 省略过程一步变换
        self.play(Write(M1_formula_3))
        self.play(ReplacementTransform(M1_formula_3, M1_formula_3_change))

        # 移动到M1_formula_2_change下方
        self.play(M1_formula_3_change.animate.next_to(M1_formula_2_change, DOWN).scale(0.8))
        self.wait()

        M1_formula_10 = MathTex(r"\bar P_{tis}(s)=(Q_{ot}\frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}+Q_{m}\frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}})/Q").next_to(M1_formula_3_change, DOWN*2)
        self.play(Write(M1_formula_10))
        self.wait()
        self.remove(M1_formula_9, M1_formula_7L, M1_formula_2_change, M1_formula_3_change)
        self.play(M1_formula_10.animate.move_to(ORIGIN), run_time=1)
        self.wait()

        Assumption_3 = MathTex(r"\mbox{Consider a small amount of time(t is small), s is large}").next_to(M1_formula_10, UP)
        self.play(Write(Assumption_3))
        self.wait(2)
        # self.play(Assumption_3.animate.scale(0.3).to_edge(UP + RIGHT), run_time=2)
        self.play(Assumption_3.animate.scale(0.3).next_to(Assumption_2, DOWN), run_time=2)

        M1_formula_10_1 = MathTex(r"\bar P_{tis}(s)=\bar P_a^*(\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}})/(sQ) =\frac{\bar P_a^*}{s\tau_{tis}}")
        self.play(TransformMatchingTex(M1_formula_10, M1_formula_10_1))
        self.wait()

        M1_formula_12 = MathTex(r"V_{tis} = Q^2/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}})")
        self.play(TransformMatchingTex(M1_formula_10_1, M1_formula_12))
        self.wait()

#manim M1_show.py M1 -pqm
#manim M1_show.py M1_PART2 -pqm