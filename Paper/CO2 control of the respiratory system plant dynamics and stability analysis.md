# CO2 control of the respiratory system: plant dynamics and stability analysis

Short-term Periodicities(STP) are cyclic changes in ventilation and composition of respiratory gases having periods ranging from 20 to 120 seconds.

The authors are trying to investigate the hypothesis that the stability characteristics associated with CO2 control of the respiratory system determine STP. The former studies lack neither analytical or simulation techniques.

The paper is organized in two parts. The first part is modeling the CO2 dynamics. The authors use a three compartment model first, then adding several assumptions and plugging in the real data to reduce the model to two compartments and final to one compartment. The second part is the stability analysis part. The author linearize the one compartment model, and derived an explicit criterion which maps the parameters into a unified index of ventilatory stability.

### Model CO2 plant dynamics:

#### Three compartment model

The authors suppose we have three compartment to consider: A: alveolar; m: muscle; ot: other tissue. Suppose within each compartment, CO2 is in chemical equilibrium.

$P_A$ is the CO2 partial pressures of the alveolar gas. $P_a$ is the CO2 partial pressures of the arterial blood. In balance state, $P_A=P_a$

##### The mass balance for alveolar CO2:

$V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a)$

$P_I$ is the inspired CO2 partial pressure; $P_v^*(t)=P_v(t-t_v)$ is the mixed venous partial pressure with systemic venous delay time $t_v$. $V_A$ is an equivalent volume for alveolar gas and tissue. $\dot V_A$ is the alveolar ventilation. $Q$ is the pulmonary blood flow(equal cardiac output). $\lambda$ is the CO2 tissue-gas partition coefficient.

Below is the CO2 flows in three compartment:

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220415110035624.png" alt="image-20220415110035624" style="zoom:67%;" />

##### Muscle compartment CO2 mass balance:

$V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)$

$V_m$ is the muscle volume. $M_m$ is the metabolic rate. $Q_m$ is the muscle blood flow. $P_a^*(t)=P_a(t-t_a)$ where $t_a$ is the systemic arterial delay time. $k$ is the slope of the CO2 equilibrium relation between total and free CO2 in blood, muscle and other tissue. $P_m$ is the CO2 partial pressure in muscle.

##### other tissue compartment CO2 mass balance:

$V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot})$

$V_{ot}$ is the other tissue volume. $M_{ot}$ is the metabolic rate. $Q_{ot}$ is the other tissue blood flow. $P_a^*(t)=P_a(t-t_a)$ where $t_a$ is the systemic arterial delay time. $k$ is the slope of the CO2 equilibrium relation between total and free CO2 in blood, muscle and other tissue. $P_{ot}$ is the CO2 partial pressure in other tissue.

In addition, total blood flow should equal to the sum of parallel compartment output.

$Q = Q_m+Q_{ot}$

And from mass conservation, CO2 partial pressure of the mixed venous blood is:

$P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q$



#### M1: 

Now we have five equations to form M1:

$\begin{equation}V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a) \tag{1} \end{equation}$     

$\begin{equation} V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)  \tag{2} \end{equation}$  

$\begin{equation} V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot}) \tag 3 \end{equation}$ 

$\begin{equation} Q = Q_m+Q_{ot} \tag 4 \end{equation}$ 

$\begin{equation} P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag 5 \end{equation}$ 



#### Reduce to two compartment model:

The authors want to simplify the model M1 by merging two tissues compartment, and get only one compartment "tissue"(tis) like (6): 

$\begin{equation} V_{tis} \derivative{P_{tis}}{t} = \frac {M_{tis}} {k} + Q(P_a^*-P_{tis}) \tag 6 \end{equation}$ 

In this equation we need to find expression for $V_{tis}$ and $M_{tis}$.

##### Find $M_{tis}$:

by our assumption,  CO2 partial pressures of two tissues $P_{tis}$ , should equal to CO2 partial pressures of the venous $P_v$

$\begin{equation} P_{tis} = P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag 7 \end{equation}$  

Now the authors only consider the stable, long term effect behaviors of the model. So they calculate the stable $P_m,P_{ot}$, by setting the RHS of (2)=0.

set (2) RHS=0:

$\frac {M_m} {k} + Q_m(P_a^*-P_m) =0$

$\begin{equation} Q_mP_m = \frac {M_m} {k} + Q_mP_a^* \tag{2-1} \end{equation}$ 

set (3) RHS=0:

 $\begin{equation}Q_{ot}P_{ot} = \frac {M_{ot}} {k} + Q_{ot}P_a^* \tag{3-1} \end{equation}$ 

plug (2-1),(3-1) into (5) :

$\begin{equation} M_{tis} = M_m + M_{ot} \tag 8 \end{equation}$ 

##### Find $V_{tis}$:

define effective tissue time constant: 

$\begin{equation} \tau_{tis} = \frac{V_{tis}}{Q} \tag{9} \end{equation}$ 

Laplace transform of (7):

​	Laplace transform: $F(s) = \int_0^\infin f(t)e^{-st} dt$

​	Laplace transform of first derivative: $\mathcal{L}(\derivative{P_m}{t})=s\bar P_m(s)-P_m(0)=s\bar P_m(s)$ 

 $\begin{equation} \bar P_{tis}(s)=(Q_{ot}\bar P_{ot}(s)+Q_m\bar P_m(s))/Q \tag{7-L} \end{equation}$ 

Laplace transform of (2), (3):

$V_m  \mathcal L(P_m') = \frac {M_m} {ks} + Q_m(\mathcal L(P_a^*)-\mathcal L(P_m)) $

$V_m  [s\bar P_m(s)-P_m(0)] = \frac {M_m} {ks} + Q_m(\bar P_a^*(s)-\bar P_m(s))$

$(sV_{m}+Q_{m}) \bar P_m(s) = \frac {M_m} {ks} + Q_m\bar P_a^*(s)$ 

$\bar P_m(s) = \frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}}$

similarly: $\bar P_{ot}(s) = \frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}$, then plug in 7-L:

$\begin{equation} \bar P_{tis}(s)=(Q_{ot}\frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}+Q_{m}\frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}})/Q \tag{10} \end{equation}$  

The authors assume we only consider the situation that s is large(or t is small) we have:

$\bar P_{tis}(s)=\bar P_a^*(\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}})/(sQ) =\frac{\bar P_a^*}{s\tau_{tis}}$ 

$\begin{equation} \tau_{tis} = \frac{V_{tis}}{Q} = Q/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}}) \tag{11} \end{equation} $ 

then we have $V_{tis}$:

$\begin{equation} V_{tis} = Q^2/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}}) \tag{12} \end{equation} $ 



#### M2:

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416174543883.png" alt="image-20220416174543883" style="zoom:50%;" />

Assume $P_{tis}^* = P_v^*$ , $P_A^*=P_v^*$ . Now the we have two equations to form M2:

$\begin{equation} \derivative{P_A}{t}=\frac{(P_I-P_A)}{\tau_A}+\frac{(P_{tis}^*-P_A)}{\tau_e} \tag{13} \end{equation}$

$\begin{equation} \derivative{P_{tis}}{t} = \frac {Q \tau_{tis} M_{tis}} {k} + \frac{(P_a^*-P_{tis})}{\tau_{tis}} \tag{14} \end{equation}$ 

$\tau_A = \frac{V_A}{\dot V_A}; \tau_e = \frac{V_A}{\lambda Q}$ 



#### Reduce to one compartment

In order to further reduce the model, in plant modeling, the authors assume that the time delays within the plant are negligible with respect to other system time constant.

So, $P_{tis}^*=P_{tis},P_A^*=P_A$ 

Combine (13)(14):

$\begin{equation} \tau_{tis}  \frac{\dd[2]P_{tis}}{\dd t^2} +(1+\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd t} = \frac{P_I-P_{tis}}{\tau_A} + \frac{M_{tis}Q}{k}(\frac{1}{\tau_A}+\frac{1}{\tau_e}) \tag{15} \end{equation}$ 

Focus on LHS, and conduct dimensionless transform $\theta=\frac{t}{\tau_{tis}}$: 
$$
LHS= [\frac{\dd[2]P_{tis}}{\dd \theta^2} +(1+\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}]\frac{1}{\tau_{tis}} \\
\approx (\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}\frac{1}{\tau_{tis}} \\
= (\frac{1}{\tau_A} + \frac{1}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}
$$
Here the authors plugin the real data for human, and find that, $\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e} \gg 1$ , $\frac{1}{\tau_A} \ll \frac{1}{\tau_e}$. And they plugin $\tau_e,\tau_A$, we will have:

$\begin{equation} \frac{\dd P_{tis}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{tis})}{\lambda} + \frac{M_{tis}V_S}{k} \tag{16} \end{equation}$ 



#### M3:

Now we only have one compartment(M3), so the authors will change name to s.

$\begin{equation} \frac{\dd P_{s}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{s})}{\lambda} + \frac{M_{s}V_S}{k} \tag{17} \end{equation}$ 

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416181315147.png" alt="image-20220416181315147" style="zoom:50%;" />



The below graph is the numerical simulation of the three models:

The y axis of M1, M2, M3 correspond to $P_v,P_v,P_s$ in each model.

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416181946756.png" alt="image-20220416181946756" style="zoom:50%;" />

### Stability criterion:

In order to find the conditions where the system M3 is stable, we need to linearize the model,

The authors sssume the alveolar ventilation $\dot V_A$ is linearly related to CO2 partial pressure 

$\begin{equation} \dot V_A = \begin{cases} GP_s^*-I \mbox{ if } P_s^*\gt I/G \\ 0 \mbox{ if } P_s^*\lt I/G \end{cases}  \tag{18} \end{equation}$ 

G is the controller gain, $I$ is the linear intercept. $P_s^* = P_s(t-t_d)$ is the CO2 partial pressure, $t_d$ is the systemic arterial delay.

plug (18) into (17):

$\begin{equation} \frac{\dd P_s}{\dd t} = F(P_s^*, P_s)+M_sV_s/k \tag{19} \end{equation} $

$F(P_s^*,P_s)=(GP_s^*-I)(P_I-P_s)V_s/\lambda$  

Let RHS equals zero and solve the equation to get the fixed point:

$P_{so} = \frac{P_I+I/G \pm \sqrt{\Delta}}{2}$ （19-1）

The authors want to linearize the model near the fixed point. So they have:

$\begin{equation} \frac{\dd P_s}{\dd t} = A_sP_s+B_sP^*_s \\ \tag{22} \end{equation}$ 

$A_s = -\frac{\dot V_{Ao}^*V_s}{\lambda}; B_s = -\frac{GV_s(P_{so}-P_I)}{\lambda}$

 In order to find the condition where (22) is stable, the authors use "Hayes" condition

If the following three conditions are satisfied, (22) is stable.

S.1 $A_st_d<1$

S.2 $A_s<-B_s$

S.3 $-B_st_d<\sqrt{(A_st_d)^2 + \rho_1^2}$;   $\rho_1$ is the root of $\rho\cot \rho = A_st_d$ 

The authors define a stability index to characterize the stability.

$\begin{equation} SI=\frac{2Gt_d(P_{so}-P_I)}{\pi \lambda V_s} = \frac{UF}{SF}\lt 1  \tag{23} \end{equation}$  

If $SI\lt 1$ or $UF \lt SF$, $P_s,\dot V_A$ is stable.

Below is the graph of the SI with respect to parameters:

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220417100208306.png" alt="image-20220417100208306" style="zoom:50%;" />

We can see from the graph, that inspired CO2 partial pressure $P_I$, metabolic rate $M_s$, do not affect the stability of the system that much. time delay $t_d$, controller gain $G$, effective tissue volume $V_s$ is closely related to stability of the system. If the the systemic arterial delay time is large, the fixed point is not stable. When inspired CO2 or the effective tissue volume increase, the system is more stable



### Limitation

The authors make a lot of biological assumptions:

A1: Suppose within each compartment, CO2 is in chemical equilibrium

A2: Consider only the stable partial pressure of the gas

A3:  Consider a small amount of time(t is small)

A4: use time delay data measured from human adults.

A5: Assume that the time delays within the plant are negligible with respect to other system time constant

A6: alveolar ventilation $\dot V_A$ is linearly related to CO2 partial pressure

The authors(1988) say in the paper: "Exhaustive simulations of different combinations of all parameters would be a formidable task". But now more numerical simulation is possible.

equation (9,16,17,22) was not validated and (16,17) do not include the effect of inspired CO2 concentration.



