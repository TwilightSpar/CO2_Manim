from manim import *


class M1(Scene):
    def construct(self):
        M1_formula_1 = MathTex(r"V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a) \tag{1}").shift(UP * 3)
        M1_formula_2 = MathTex(r"V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)  \tag{2} ").shift(UP * 1.5)
        M1_formula_3 = MathTex(r"V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot}) \tag 3")
        M1_formula_4 = MathTex(r"Q = Q_m+Q_{ot} \tag 4 ").shift(DOWN)
        Assumption_1 = MathTex(r"\mbox{CO2 is in chemical equilibrium}").next_to(M1_formula_4, DOWN)
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

        self.play(Write(Assumption_1))
        self.wait(2)
        self.play(Assumption_1.animate.scale(0.3).to_edge(UP + RIGHT), run_time=2)

        self.play(Write(M1_formula_5, run_time=1))  # Write()从左到右写出来
        self.wait()  # 等待一个单位时间

        # R2 = VGroup(M1_formula_4,M1_formula_5)
        self.remove(M1_formula_5, M1_formula_4)
        R1 = VGroup(M1_formula_1, M1_formula_2, M1_formula_3)
        # self.play(R1.animate.scale(0.3))
        # 边缩小，边移动
        self.play(R1.animate.scale(0.3).to_edge(UP + LEFT), run_time=1.5)

        self.wait(3)

        # get back Eq 2,3
        Eq2_3_group = VGroup(M1_formula_2, M1_formula_3)
        rectangle = Rectangle(fill_opacity=0.0,stroke_color= WHITE,width=4.5, height=1)

        rectangle.move_to(Eq2_3_group.get_center())
        rectangle.add_updater(lambda x: x.move_to(Eq2_3_group.get_center()))

        self.play(FadeIn(rectangle))
        self.remove(M1_formula_1)

        self.play(FadeOut(rectangle))
        self.play(Eq2_3_group.animate.scale(10/3).move_to(ORIGIN), run_time=1.5)
        self.wait()

        # Need to merge two equations to tissue
        M1_Tis_1 = MathTex(r"V_{tis} \derivative{P_{tis} }{t} = ", r"\frac {M_{tis} } {k} + Q", r"(", r"P_a^*", r"-", r"P_{tis})", r"\tag{6}").shift(UP)
        self.play(TransformMatchingTex(Eq2_3_group, M1_Tis_1))
        self.wait()

        rectangle_M = Rectangle(fill_opacity=0.0, stroke_color=ORANGE, width=1.3, height=0.6)
        rectangle_V = Rectangle(fill_opacity=0.0, stroke_color=ORANGE, width=1.3, height=0.6)
        rectangle_M.move_to(M1_Tis_1.get_center()).move_to((-3, 1.3, 0))
        rectangle_V.move_to(M1_Tis_1.get_center()).move_to((-5.7, 1, 0))
        self.play(FadeIn(rectangle_M))
        self.play(FadeIn(rectangle_V))
        self.wait()
        self.play(FadeOut(rectangle_M))
        self.play(FadeOut(rectangle_V))

        Assumption_2 = MathTex(r"\mbox{let RHS=0, consider stable situation}").next_to(M1_Tis_1, UP)
        self.play(Write(Assumption_2))
        self.wait(2)
        self.play(Assumption_2.animate.scale(0.3).next_to(Assumption_1, DOWN), run_time=2)

        self.wait()

        M1_Tis_1_equal_0_1 = MathTex(r"\frac {M_{tis} } {k} + Q", r"(", r"P_a^*", r"-", r"P_{tis})", r"=", r"0").shift(UP)
        self.play(TransformMatchingTex(M1_Tis_1, M1_Tis_1_equal_0_1))
        self.wait()

        M1_Tis_1_equal_0_2 = MathTex(r"\frac {M_{tis} } {k} + ", r"Q", r"P_a^*", r"=", r"Q", r"P_{tis}").shift(UP)
        self.play(TransformMatchingTex(M1_Tis_1_equal_0_1, M1_Tis_1_equal_0_2))
        self.wait()
        self.remove(M1_Tis_1_equal_0_1)
        self.wait()

        M1_Tis_1_equal_0_3 = MathTex(r"Q", r"P_{tis}", r"=", r"\frac {M_{tis} } {k} + ", r"Q", r"P_a^*").shift(UP*2)
        self.play(TransformMatchingTex(M1_Tis_1_equal_0_2, M1_Tis_1_equal_0_3))

        M1_ot_1_equal = MathTex(r"Q_{ot}", r"P_{ot}", r"=", r"\frac {M_{ot} } {k} + ", r"Q_{ot}", r"P_a^*").next_to(M1_Tis_1_equal_0_3, DOWN)
        M1_mu_1_equal = MathTex(r"Q_{m}", r"P_{m}", r"=", r"\frac {M_{m} } {k} + ", r"Q_{m}", r"P_a^*").next_to(M1_ot_1_equal, DOWN)
        M1_QP_group = VGroup(M1_Tis_1_equal_0_3, M1_ot_1_equal, M1_mu_1_equal)
        self.play(TransformMatchingTex(M1_Tis_1_equal_0_3, M1_QP_group))
        self.play(M1_QP_group.animate.shift(UP).scale(0.8))

        M_1_mass_conservation_1 = MathTex(r"P_{tis} = (", r"Q_{ot}", r"P_{ot}", r"+", r"Q_m", r"P_m", r") / Q").next_to(M1_QP_group, DOWN)
        M_1_mass_conservation_2 = MathTex(r"Q", r"P_{tis}", r"=", r"Q_{ot}", r"P_{ot}", r"+", r"Q_m", r"P_m").next_to(M1_QP_group, DOWN)
        M_1_mass_conservation_2_plugin = MathTex(r"\frac {M_{tis}} {k} + QP_a^*", r"=", r"\frac {M_{ot} } {k} + Q_{ot}P_a^*", r"+", r"\frac {M_{m} } {k} + Q_{m}P_a^*").next_to(M1_QP_group, DOWN)

        self.play(Write(M_1_mass_conservation_1))
        self.wait()
        self.play(TransformMatchingTex(M_1_mass_conservation_1, M_1_mass_conservation_2))
        self.wait()

        variables = VGroup(MathTex(r"\frac {M_{tis} } {k} + QP_a^*"), MathTex(r"\frac {M_{ot} } {k} + Q_{ot}P_a^*"), MathTex(r"\frac {M_{m} } {k} + Q_{m}P_a^*")).arrange_submobjects().next_to(M_1_mass_conservation_2, UP)

        self.play(TransformMatchingTex(Group(M_1_mass_conservation_2, variables), M_1_mass_conservation_2_plugin))
        self.remove(M1_QP_group)
        self.wait()

        Mass_conservation = MathTex(r"M_{tis}", r"=", r"M_m", r"+", r"M_{ot}")
        self.play(TransformMatchingTex(M_1_mass_conservation_2_plugin, Mass_conservation))
        self.wait()

        self.play(Mass_conservation.animate.move_to(ORIGIN), run_time=1)
        self.wait()
