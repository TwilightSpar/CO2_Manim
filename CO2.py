from manim import *


class M1(Scene):
    def construct(self):
        M1_Tis_1 = MathTex(r"V_{tis} \derivative{P_{tis} }{t} = ", r"\frac {M_{tis} } {k} + Q(P_a^*-P_{tis})").shift(UP)
        Text_consider_nullcline = Tex("let RHS=0, consider stable situation").shift(2*UP)
        M1_Tis_1_equal_0_1 = MathTex(r"\frac {M_{tis} } {k} + Q(P_a^*-P_{tis})","= 0").shift(UP)
        M1_Tis_1_equal_0_2 = MathTex(r"\frac {M_{tis} } {k} + QP_a^*","=","QP_{tis}").shift(UP)
        M1_Tis_1_equal_0_3 = MathTex(r"QP_{tis}","=",r"\frac {M_{tis} } {k} + QP_a^*").shift(UP)

        M_1_mass_conservation_1 = MathTex(r" P_{tis} = (Q_{ot}P_{ot}+Q_mP_m) / Q")
        M_1_mass_conservation_2 = MathTex(r" QP_{tis} = (Q_{ot}P_{ot}+Q_mP_m)")
        M_1_mass_conservation_2_plugin_Tis = MathTex(r" \frac {M_{tis}} {k} + QP_a^* = (Q_{ot}P_{ot}+Q_mP_m)")

        # M1_Tis_1.to_edge(UP)

        self.play(Write(M1_Tis_1))
        self.wait()

        self.play(Write(Text_consider_nullcline))
        self.wait()

        self.remove(Text_consider_nullcline)
        self.wait()

        self.play(TransformMatchingTex(M1_Tis_1, M1_Tis_1_equal_0_1))
        self.wait()

        self.play(M1_Tis_1_equal_0_1.animate.shift(UP))

        self.play(Write(M1_Tis_1_equal_0_2))
        self.wait()
        self.remove(M1_Tis_1_equal_0_1)
        self.wait()

        self.play(TransformMatchingTex(M1_Tis_1_equal_0_2, M1_Tis_1_equal_0_3))

        self.play(M1_Tis_1_equal_0_3.animate.shift(UP*2))

        self.play(Write(M_1_mass_conservation_1))
        self.wait()
        self.play(M_1_mass_conservation_1.animate.shift(UP))

        self.play(Write(M_1_mass_conservation_2))
        self.wait()
        self.remove(M_1_mass_conservation_1)
        self.wait()
        self.play(M_1_mass_conservation_2.animate.shift(UP))

        self.play(Write(M_1_mass_conservation_2_plugin_Tis))
        self.wait()
        self.remove(M_1_mass_conservation_2)
        self.wait()
        self.remove(M1_Tis_1_equal_0_3)
        self.wait()
        self.remove(M_1_mass_conservation_2_plugin_Tis)

        self.wait()
