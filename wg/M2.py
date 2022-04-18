from manim import *
#assumption 3,4

class M2(Scene):
    def construct(self):

        # Add former assumptions
        Assumption_1 = MathTex(r"\mbox{CO2 is in chemical equilibrium}").scale(0.3).to_edge(UP + RIGHT)
        Assumption_2 = MathTex(r"\mbox{let RHS=0, consider stable situation}").scale(0.3).next_to(Assumption_1, DOWN)
        Assumption_3 = MathTex(r"\mbox{Consider a small amount of time(t is small), s is large}").scale(0.3).next_to(Assumption_2, DOWN)
        self.add(Assumption_1, Assumption_2, Assumption_3)

        M2_formula_7 = MathTex(r"P_{tis} = P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag{7}").shift(UP * 2)
        M2_formula_8 = MathTex(r"M_{tis} = M_m + M_{ot} \tag{8} ")
        M2_formula_8.next_to(M2_formula_7, DOWN)
        M2_formula_12 = MathTex(r"V_{tis} = Q^2/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}}) \tag{12}")
        M2_formula_12.next_to(M2_formula_8, DOWN)

        M2_formula_14 = MathTex(r"\derivative{P_{tis}}{t} = \frac {Q \tau_{tis} M_{tis}} {k} + \frac{(P_a^*-P_{tis})}{\tau_{tis}} \tag{14}")
        M2_formula_13 = MathTex(r"\derivative{P_A}{t}=\frac{(P_I-P_A)}{\tau_A}+\frac{(P_{tis}^*-P_A)}{\tau_e} \tag{13}")
        M2_formula_13.next_to(M2_formula_14, UP)

        M2_def_tau = MathTex(r"\tau_A = \frac{V_A}{\dot V_A}; \tau_e = \frac{V_A}{\lambda Q}")
        M2_def_tau.next_to(M2_formula_14, DOWN)
        # M1_Tis_1.to_edge(UP)

        self.play(Write(M2_formula_7))
        self.wait()

        self.play(Write(M2_formula_8))
        self.wait()

        self.play(Write(M2_formula_12))
        self.wait()

        #formula 7, 8, 12
        FGroup1 = VGroup(M2_formula_7, M2_formula_8, M2_formula_12)

        self.play(TransformMatchingTex(FGroup1, M2_formula_14))
        self.wait()

        self.play(Write(M2_formula_13))
        self.play(Write(M2_def_tau))
        self.wait()

        Assumption_4 = MathTex(r"\mbox{Assume} P_{tis}^* = P_v^*, P_A^*=P_v^*. \mbox{ get M2}", font_size=40).next_to(M2_def_tau, DOWN)
        self.play(Write(Assumption_4))
        self.wait(2)
        self.play(Assumption_4.animate.scale(0.3).next_to(Assumption_3, DOWN), run_time=2)


        #M2_part2
        M2_formula_15 = MathTex(r"\tau_{tis} \frac{\dd[2]P_{tis}}{\dd t^2} + (1+\frac{\tau_{tis}}{\tau_A} + \frac{"r"\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd t}",
            r"=", r"\frac{P_I-P_{tis}}{\tau_A} + \frac{M_{tis}Q}{k}(\frac{1}{\tau_A}+\frac{1}{\tau_e}) \tag{15}", font_size=40)
        M2_formula_15_LHS = MathTex(r"LHS", r"=", r"\tau_{tis} \frac{\dd[2]P_{tis}}{\dd t^2} + (1+\frac{\tau_{tis}}{\tau_A} + \frac{"r"\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd t}")

        M2_formula_15_LHS1 = MathTex(r"LHS", r"=", r"[", r"\frac{\dd[2]P_{tis}}{\dd \theta^2}", r"+", r"(", r"1", r"+",
                                     r"\frac{\tau_{tis}}{\tau_A}", r"+",
                                     r"\frac{\tau_{tis}}{\tau_e}", r")", r"\frac{\dd P_{tis}}{\dd \theta}", r"]",
                                     r"\frac{1}{\tau_{tis}}")
        M2_formula_15_LHS2 = MathTex(r"LHS", r"\approx", r"(", r"\frac{\tau_{tis}}{\tau_A}", r"+",
                                     r"\frac{\tau_{tis}}{\tau_e}", r")",
                                     r"\frac{\dd P_{tis}}{\dd \theta}", r"\frac{1}{\tau_{tis}}")
        M2_formula_15_LHS3 = MathTex(r"LHS", r"=", r"(", r"\frac{1}{\tau_A}", r"+", r"\frac{1}{\tau_e}", r")",
                                     r"\frac{\dd P_{tis}}{\dd \theta}")

        M2_formula_16 = MathTex(r"\frac{\dd P_{tis}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{tis})}{\lambda} + \frac{M_{tis}V_S}{k} \tag{16}")

        M2_theta = MathTex(r"\mbox{in dimensionless form: } \theta=\frac{t}{\tau_{tis}}")

        FGroup2 = VGroup(M2_formula_13, M2_formula_14)
        FGroup3 = VGroup(M2_formula_15_LHS, M2_theta)
        # M1_Tis_1.to_edge(UP)

        self.remove(M2_def_tau)
        self.wait()

        self.play(TransformMatchingTex(FGroup2, M2_formula_15))
        self.wait()

        self.play(TransformMatchingTex(M2_formula_15, M2_formula_15_LHS))
        self.wait()

        self.play(M2_formula_15_LHS.animate.move_to(UP).scale(0.8))
        self.wait()

        self.play(Write(M2_theta.scale(0.8)))
        self.wait()

        self.play(TransformMatchingTex(FGroup3, M2_formula_15_LHS1))
        self.wait()

        Assumption_5_1 = MathTex(r"\mbox{Plugin the real data for human, }\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e} \gg 1",
            font_size=35).next_to(M2_formula_15_LHS1, UP)
        self.play(Write(Assumption_5_1))
        self.wait()

        self.play(TransformMatchingTex(M2_formula_15_LHS1, M2_formula_15_LHS2))
        self.wait()

        self.play(Assumption_5_1.animate.scale(0.3).next_to(Assumption_4, DOWN), run_time=2)
        self.wait()

        self.play(TransformMatchingTex(M2_formula_15_LHS2, M2_formula_15_LHS3))
        self.wait()

        Assumption_5_2 = MathTex(r"\mbox{also, }\frac{1}{\tau_A} \ll \frac{1}{\tau_e}", font_size=35).next_to(M2_formula_15_LHS3, UP)
        self.play(Write(Assumption_5_2))
        self.wait()

        self.play(Write(M2_def_tau.next_to(M2_formula_15_LHS3, DOWN)))
        self.wait()

        FGroup4 = VGroup(M2_formula_15_LHS3, M2_def_tau)
        self.remove(Assumption_5_2) 
        self.wait()

        self.play(TransformMatchingTex(FGroup4, M2_formula_16))
        self.wait()

#manim M2.py M2 -pql