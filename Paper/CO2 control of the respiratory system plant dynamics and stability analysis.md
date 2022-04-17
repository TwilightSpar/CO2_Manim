# CO2 control of the respiratory system: plant dynamics and stability analysis

Short-term Periodicities(STP) are cyclic changes in ventilation and composition of respiratory gases having periods ranging from 20 to 120 seconds.

The authors are trying to investigate the hypothesis that the stability characteristics associated with CO2 control of the respiratory system determine STP. The former study does not use both analytical and simulation techniques.

Model CO2 plant dynamics:

Three compartment model

A: alveolar; m: muscle; ot: other tissue. Suppose within each compartment, CO2 is in chemical equilibrium.

$P_A$: CO2 partial pressures of the alveolar gas = $P_a$: CO2 partial pressures of the arterial blood

The mass balance for alveolar CO2:

$V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a)$

$P_I$: inspired CO2 partial pressure; $P_v^*=P_v(t-t_v)$ is the mixed venous partial pressure with systemic venous delay time $t_v$. $V_A$ is an equivalent volume for alveolar gas and tissue. $\dot V_A$ is the alveolar ventilation. $Q$ is the pulmonary blood flow(equal cardiac output). $\lambda$ is the CO2 tissue-gas partition coefficient.



<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220415110035624.png" alt="image-20220415110035624" style="zoom:67%;" />

Muscle compartment CO2 mass balance:

$V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)$

$V_m$ is the muscle volume. $M_m$ is the metabolic rate. $Q_m$ is the muscle blood flow. $P_a^*=P_a(t-t_a)$ where $t_a$ is the systemic arterial delay time. $k$ is the slope of the CO2 equilibrium relation between total and free CO2 in blood, muscle and other tissue. $P_m$ is the CO2 partial pressure in muscle.

other tissue compartment CO2 mass balance:

$V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot})$

$V_{ot}$ is the other tissue volume. $M_{ot}$ is the metabolic rate. $Q_{ot}$ is the other tissue blood flow. $P_a^*=P_a(t-t_a)$ where $t_a$ is the systemic arterial delay time. $k$ is the slope of the CO2 equilibrium relation between total and free CO2 in blood, muscle and other tissue. $P_{ot}$ is the CO2 partial pressure in other tissue.

total blood flow is equals to the sum of parallel compartment output.

$Q = Q_m+Q_{ot}$

CO2 partial pressure of the mixed venous blood: ## mass conservation

$P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q$



#### M1: 

$\begin{equation}V_A \derivative{P_A}{t}=\dot V_A(P_I-P_A)+\lambda Q(P_v^*-P_a) \tag{1} \end{equation}$     

$\begin{equation} V_m \derivative{P_m}{t} = \frac {M_m} {k} + Q_m(P_a^*-P_m)  \tag{2} \end{equation}$  

$\begin{equation} V_{ot} \derivative{P_{ot}}{t} = \frac {M_{ot}} {k} + Q_{ot}(P_a^*-P_{ot}) \tag 3 \end{equation}$ 

$\begin{equation} Q = Q_m+Q_{ot} \tag 4 \end{equation}$ 

$\begin{equation} P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag 5 \end{equation}$ 



#### Reduce to two compartment model:

We want to merge two tissues compartment. get only one compartment "tis": 

$\begin{equation} V_{tis} \derivative{P_{tis}}{t} = \frac {M_{tis}} {k} + Q(P_a^*-P_{tis}) \tag 6 \end{equation}$ 

##### In order to find an expression of $M_{tis}$, rewrite (5):

$\begin{equation} P_{tis} = P_v=(Q_{ot}P_{ot}+Q_mP_m)/Q \tag 7 \end{equation}$  

Assumption####: consider stable, long term effect; 

$\begin{equation} M_{tis} = M_m + M_{ot} \tag 8 \end{equation}$ 

##### In order to find an expression of $V_{tis}$:

define effective tissue time constant: 

$\begin{equation} \tau_{tis} = \frac{V_{tis}}{Q} \tag{9} \end{equation}$ 

Laplace transform of (7) : $\begin{equation} \bar P_{tis}(s)=(Q_{ot}\bar P_{ot}(s)+Q_m\bar P_m(s))/Q \tag{7-L} \end{equation}$ 

Laplace transform of (2), (3):

$V_m  \mathcal L(P_m') = \frac {M_m} {ks} + Q_m(\mathcal L(P_a^*)-\mathcal L(P_m)) $

$V_m  [s\bar P_m(s)-P_m(0)] = \frac {M_m} {ks} + Q_m(\bar P_a^*(s)-\bar P_m(s))$

$(sV_{m}+Q_{m}) \bar P_m(s) = \frac {M_m} {ks} + Q_m\bar P_a^*(s)$ 

$\bar P_m(s) = \frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}}$

similarly: $\bar P_{ot}(s) = \frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}$, then plug in 7-L:

$\begin{equation} \bar P_{tis}(s)=(Q_{ot}\frac{M_{ot}/(ks) + Q_{ot}\bar P_a^*}{sV_{ot}+Q_{ot}}+Q_{m}\frac{M_{m}/(ks) + Q_{m}\bar P_a^*}{sV_{m}+Q_{m}})/Q \tag{10} \end{equation}$  

Assumption####: s is large(or t is small) we have:

$\bar P_{tis}(s)=\bar P_a^*(\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}})/(sQ) =\frac{\bar P_a^*}{s\tau_{tis}}$ 

$\begin{equation} \tau_{tis} = \frac{V_{tis}}{Q} = Q/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}}) \tag{11} \end{equation} $ 

then we have $V_{tis}$:

$\begin{equation} V_{tis} = Q^2/ (\frac{Q_{ot}^2}{V_{ot}}+\frac{Q_{m}^2}{V_{m}}) \tag{12} \end{equation} $ 



#### M2:

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416174543883.png" alt="image-20220416174543883" style="zoom:50%;" />

Assumption####:  $P_{tis}^* = P_v^*$ , $P_A^*=P_v^*$ 

$\begin{equation} \derivative{P_A}{t}=\frac{(P_I-P_A)}{\tau_A}+\frac{(P_{tis}^*-P_A)}{\tau_e} \tag{13} \end{equation}$

$\begin{equation} \derivative{P_{tis}}{t} = \frac {Q \tau_{tis} M_{tis}} {k} + \frac{(P_a^*-P_{tis})}{\tau_{tis}} \tag{14} \end{equation}$ 

$\tau_A = \frac{V_A}{\dot V_A}; \tau_e = \frac{V_A}{\lambda Q}$ 



#### Reduce to one compartment

Assumption####: In plant modeling, the time delays within the plant are negligible with respect to other system time constant.

plugin  $P_{tis}^*=P_{tis},P_A^*=P_A$ 

Combine (13)(14):

$\begin{equation} \tau_{tis}  \frac{\dd[2]P_{tis}}{\dd t^2} +(1+\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd t} = \frac{P_I-P_{tis}}{\tau_A} + \frac{M_{tis}Q}{k}(\frac{1}{\tau_A}+\frac{1}{\tau_e}) \tag{15} \end{equation}$ 

Focus on LHS, and conduct dimensionless $\theta=\frac{t}{\tau_{tis}}$: 
$$
LHS= [\frac{\dd[2]P_{tis}}{\dd \theta^2} +(1+\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}]\frac{1}{\tau_{tis}} \\
\approx (\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}\frac{1}{\tau_{tis}} \\
= (\frac{1}{\tau_A} + \frac{1}{\tau_e})\frac{\dd P_{tis}}{\dd \theta}
$$
Assumption####: plugin real data, $\frac{\tau_{tis}}{\tau_A} + \frac{\tau_{tis}}{\tau_e} \gg 1$ , $\frac{1}{\tau_A} \ll \frac{1}{\tau_e}$, 

plugin $\tau_e,\tau_A$

$\begin{equation} \frac{\dd P_{tis}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{tis})}{\lambda} + \frac{M_{tis}V_S}{k} \tag{16} \end{equation}$ 



#### M3:

$\begin{equation} \frac{\dd P_{s}}{\dd t} = \frac{\dot V_A V_S(P_I-P_{s})}{\lambda} + \frac{M_{s}V_S}{k} \tag{17} \end{equation}$ 

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416181315147.png" alt="image-20220416181315147" style="zoom:50%;" />





The below graph is the numerical simulation of the three models:

The y axis of M1, M2, M3 correspond to $P_v,P_v,P_s$ in each model.

<img src="CO2 control of the respiratory system plant dynamics and stability analysis.assets/image-20220416181946756.png" alt="image-20220416181946756" style="zoom:50%;" />

#### Stability criterion:

Assumption####: The alveolar ventilation $\dot V_A$ is linearly related to CO2 partial pressure 

$\begin{equation} \dot V_A = \begin{cases} GP_s^*-I \mbox{ if } P_s^*\gt I/G \\ 0 \mbox{ if } P_s^*\lt I/G \end{cases}  \tag{18} \end{equation}$ 

plug (18) into (17)

$\frac{\dd P_s}{\dd t} = F(P_s^*, P_s)+M_sV_s/k; F(P_s^*,P_s)=(GP_s^*-I)(P_I-P_s)V_s/\lambda$ 

Let RHS equal zero and solve the equation to get the fixed point:

$A_s = -\frac{\dot V_{Ao}^*V_s}{\lambda}; B_s = -\frac{GV_s(P_{so}-P_I)}{\lambda}$

$\begin{equation} \frac{\dd P_s}{\dd t} = A_sP_s+B_sP^*_s \tag{22} \end{equation}$ 



