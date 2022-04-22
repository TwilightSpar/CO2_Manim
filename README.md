# CO2_Manim
CO2_Manim

This is a Manim animation making project for my presentation for "Mathematic Biology" course. <br/>
The paper I present is "CO2 control of the respiratory system: plant dynamics and stability analysis" <br/>
by Ahmed ElHefnawy, Gerald M. Saidel, Eugen N. Bruce

[Recorded presention](https://youtu.be/kB1zh1AncHQ)

## Manim method learned:
- 'MathTex': Add 'LaTex' equation object. Can break one equation to a list of 'Tex' objects.
- 'VGroup': Group some object for future transformation.
- 'TransformMatchingTex': transform From 'MathText' objects A to B, if A,B are list of objects and some of them are the same, this method will generate a smooth transformation.
- 'Write', 'add', 'remove', 'Unwrite', 'shift', 'scale': useful animation command
- 'add_updater': Ex: 'rectangle.add_updater(lambda x: x.move_to(Eq2_3_group.get_center()))', 'rectangle' will always stay in the center of Eq2_3_group object.
