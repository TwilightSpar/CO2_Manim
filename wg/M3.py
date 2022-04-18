from manim import *
#assumption 3,4

class M3(Scene):
    def construct(self):

        # Add former assumptions
        Assumption_1 = MathTex(r"\mbox{CO2 is in chemical equilibrium}").scale(0.3).to_edge(UP + RIGHT)
        Assumption_2 = MathTex(r"\mbox{let RHS=0, consider stable situation}").scale(0.3).next_to(Assumption_1, DOWN)
        Assumption_3 = MathTex(r"\mbox{Consider a small amount of time(t is small), s is large}").scale(0.3).next_to(Assumption_2, DOWN)
        Assumption_4 = MathTex(r"\mbox{Assume} P_{tis}^* = P_v^*, P_A^*=P_v^*. \mbox{ get M2}").scale(0.3).next_to(Assumption_3, DOWN)
        Assumption_5 = MathTex(r"\mbox{Plugin the real data for human, }\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e} \gg 1",font_size=35).scale(0.3).next_to(Assumption_4, DOWN)

        self.add(Assumption_1, Assumption_2, Assumption_3, Assumption_4, Assumption_5)


        Change_to_s = MathTex(r"\mbox{Only have one compartment, change subscript to s}").to_edge(UP)
        self.play(Write(Change_to_s))
        self.wait()
        self.remove(Change_to_s)

        M3_formula_17 = MathTex(r"\frac{\dd P_{s}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{s})}{\lambda} + \frac{M_{s}V_S}{k} \tag{17}").shift(UP)
        M3_formula_18 = MathTex(r"\dot V_A = GP_s^*-I \tag{18} ").next_to(M3_formula_17, DOWN)
        M3_formula_19 = MathTex(r"\frac{\dd P_s}{\dd t} = F(P_s^*, P_s)+M_sV_s/k \tag{19}")
        M3_formula_19_F = MathTex(r"F(P_s^*,P_s)=(GP_s^*-I)(P_I-P_s)V_s/\lambda").next_to(M3_formula_19, DOWN)
        M3_formula_19_1 = MathTex(r"P_{so} = \frac{P_I+I/G \pm \sqrt{\Delta}}{2} \tag{19-1}").next_to(M3_formula_19, DOWN)
        M3_formula_22 = MathTex(r"\frac{\dd P_s}{\dd t} = A_sP_s+B_sP^*_s \tag{22}")

        M3_def_A_B = MathTex(r"A_s = -\frac{\dot V_{Ao}^*V_s}{\lambda}; B_s = -\frac{GV_s(P_{so}-P_I)}{\lambda}").next_to(M3_formula_22, DOWN)

        self.play(Write(M3_formula_17))
        self.wait()

        Assumption_6 = MathTex(
            r"\mbox{assume the alveolar ventilation }\dot V_A \\ \mbox{is linearly related to CO2 partial pressure} P_s^*",
            font_size=35).next_to(M3_formula_17, UP)
        self.play(Write(Assumption_6))

        self.play(Write(M3_formula_18))
        self.wait(3)
        self.play(Assumption_6.animate.scale(0.3).next_to(Assumption_5, DOWN), run_time=1.5)
        self.wait()

        FGroup5 = VGroup(M3_formula_17, M3_formula_18)

        self.play(TransformMatchingTex(FGroup5, M3_formula_19))
        self.play(Write(M3_formula_19_F))
        self.wait()

        formula_19_explanation = MathTex(r"\mbox{This is an ODE with only one variable} P_s").next_to(M3_formula_19, UP)

        self.play(Unwrite(M3_formula_19_F, reverse=False))
        self.wait()

        self.play(Write(formula_19_explanation))
        self.wait()
        self.play(Unwrite(formula_19_explanation))

        self.play(M3_formula_19.animate.move_to(UP * 0.35))
        self.wait()

        M3_note_1 = MathTex(r"\mbox{let RHS equals zero and solve the equation to get the fixed point}").scale(0.8).next_to(M3_formula_19, UP)
        M3_note_2 = MathTex(r"\mbox{linearize the model near the fixed point}").scale(0.8).next_to(M3_formula_19, UP)

        self.play(Write(M3_note_1))
        self.wait()

        self.play(Write(M3_formula_19_1))
        self.wait()

        self.remove(M3_note_1)
        self.wait()

        self.play(Write(M3_note_2))
        self.wait()

        FGroup6 = VGroup(M3_formula_19, M3_formula_19_1)
        self.play(TransformMatchingTex(FGroup6, M3_formula_22))
        self.play(Write(M3_def_A_B))
        self.wait()

        self.remove(M3_note_2)
        self.wait()

        self.play(Unwrite(M3_def_A_B, reverse=False))
        self.wait()

        # Hayes stability analysis
        formula_22 = MathTex(r"Q\frac{\dd P_s}{\dd t}", r" = ", r"A_sP_s+B_sP^*_s")
        formula_23 = MathTex(r"SI", r"=", r"\frac{2Gt_d(P_{so}-P_I)}{\pi \lambda V_s} = \frac{UF}{SF} < 1")
        Hayes_condition = MathTex(r"\mbox{by Hayes condition:}").to_edge(UP)
        s_1 = MathTex(r"\mbox{S.1: } A_st_d<1")
        s_2 = MathTex(r"\mbox{S.2: } A_s<-B_s").next_to(s_1, DOWN)
        s_3 = MathTex(r"\mbox{S.3: } -B_st_d<\sqrt{(A_st_d)^2 + \rho_1^2};", r"\rho_1", r"\mbox{ is the root of }",
                      r"\rho\cot \rho = A_st_d").next_to(s_2, DOWN)
        s_group = VGroup(s_1, s_2, s_3).scale(0.8).next_to(Hayes_condition, DOWN)

        self.play(TransformMatchingTex(M3_formula_22, formula_22))
        self.play(Write(Hayes_condition))
        self.play(Write(s_group))
        self.play(TransformMatchingTex(formula_22, formula_23))
        self.wait(2)

        self.remove(Hayes_condition)
        self.remove(s_group)
        self.wait(3)
        self.play(Unwrite(formula_23))

        Limitation = MathTex(r"\mbox{Here is all the assumptions: }")
        self.play(Write(Limitation))
        self.wait()
        self.remove(Limitation)

        Assumption_group = VGroup(Assumption_1, Assumption_2, Assumption_3, Assumption_4, Assumption_5, Assumption_6)
        self.play(Assumption_group.animate.scale(3).move_to(ORIGIN), run_time=1.5)


#manim M3.py M3 -pql
