from manim import *

class GaussSum(Scene):
    def construct(self):
        group = VGroup()
        # One pyramid
        group1 = VGroup()
        pyramid = self.create_pyramid(1)
        pyramid.shift(UP)
        equation1 = MathTex("1")
        equation1.next_to(pyramid, DOWN*2)
        self.play(FadeIn(pyramid))
        self.play(Write(equation1))
        group1.add(pyramid, equation1)
        self.play(group1.animate.shift(LEFT*5.5))
        
        # Two pyramid
        group2 = VGroup()
        pyramid = self.create_pyramid(2)
        pyramid.shift(UP)
        equation2 = MathTex("1+2 =", "3")
        equation2.next_to(pyramid, DOWN*2)
        self.play(FadeIn(pyramid))
        self.play(Write(equation2))
        group2.add(pyramid, equation2)
        self.play(group2.animate.next_to(group1, RIGHT*4).align_to(group1, DOWN))

        # Three pyramid
        group3 = VGroup()
        pyramid = self.create_pyramid(3)
        pyramid.shift(UP)
        equation3 = MathTex("1+2+3 =", "6")
        equation3.next_to(pyramid, DOWN*2)
        self.play(FadeIn(pyramid))
        self.play(Write(equation3))
        group3.add(pyramid, equation3)
        self.play(group3.animate.next_to(group2, RIGHT*4).align_to(group2, DOWN))     
           
        #
        group.add(group1, group2, group3)
        # self.play(group.animate.scale(0.6).align_to(group1, LEFT))
        text1 = Text(" ... ", font_size=23)
        text1.next_to(group, RIGHT)
        group.add(text1)
        self.play(FadeIn(text1))
        group.add(text1)
        
        # n pyramid
        groupn = VGroup()
        pyramid = self.create_pyramid(3)
        text2 = text1.copy()
        text2.next_to(pyramid, DOWN)
        equation4 = MathTex("1+2+3+...=", "?")
        equation4.next_to(text2, DOWN)
        groupn.add(pyramid, text2, equation4)
        # groupn.scale(0.6)
        groupn.next_to(text1, RIGHT)
        self.play(FadeIn(groupn))
        group.add(groupn)
        
        text3 = Text("如果是100层金字塔，怎么求和呢？", font_size=40)
        text3.next_to(group, DOWN*3)
        self.play(ApplyWave(text3))
        self.wait(1)
        self.clear()
        
        
# class scene2(Scene):
#     def construct(self):
        
        # Scene 2
        sum_eq = MathTex(r"1&+2+3+4+5+6+7+8+9+10\\ \
            &+11+12+13+14+15+16+17+18+19+20\\ \
            &+21+22+23+24+25+26+27+28+29+30\\ \
            &+31+32+33+34+35+36+37+38+39+40\\ \
            &+41+42+43+44+45+46+47+48+49+50\\ \
            &+51+52+53+54+55+56+57+58+59+60\\ \
            &+61+62+63+64+65+66+67+68+69+70\\ \
            &+71+72+73+74+75+76+77+78+79+80\\ \
            &+81+82+83+84+85+86+87+88+89+90\\ \
            &+91+92+93+94+95+96+97+98+99+100"
        )
        sum_eq.scale(0.8).align_on_border(UP)
        text5 = Text("我们当然不能傻傻的一个一个累加到100...", font_size=40)
        text5.next_to(sum_eq, DOWN*2)
        
        self.play(Write(sum_eq, run_time=5))
        self.wait(3)
        self.play(FadeIn(text5))
        self.wait(2)
        self.clear()

# class scene3(Scene):
#     def construct(self):
        text = Text("我们改变一下金字塔的形状，让他变成一个阶梯", font_size=40)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        
        self.clear()
        pyramid = self.create_pyramid(4)
        self.play(Create(pyramid))
        self.wait(1)
        # Change the shape of the pyramid to a ladder
        self.play(*[row.animate.align_to(pyramid, LEFT) for row in pyramid])
        self.wait(1)
        #
        pyramid2 = pyramid.copy()
        self.play(pyramid.animate.shift(LEFT*1.5), pyramid2.animate.shift(RIGHT*1.5))
        self.wait(1)
        self.play(Rotating(pyramid2, radians=PI, about_point=pyramid2.get_center()), run_time=1)
        # Combine the two ladders into a rectangle
        for i in range(len(pyramid)):
            self.play(pyramid2[i].animate.next_to(pyramid[len(pyramid)-i-1], RIGHT, buff=0.2*0.8))
        rectangle = VGroup(pyramid, pyramid2)
        brace_left = Brace(rectangle, LEFT)
        brace_up = Brace(rectangle, UP)
        text_width = brace_left.get_text("4")
        text_long = brace_up.get_text("4+1=","5")
        
        self.play(GrowFromCenter(brace_left), Write(text_width))
        self.play(GrowFromCenter(brace_up), Write(text_long))
        self.wait(1)
        
        
        equation1 = MathTex("4*5=","20")
        equation2 = MathTex(r"\frac{4*5}{2} =", "10")
        equation3 = MathTex(r"\frac{4*5}{2} =", "10 =", "1+2+3+4")
        equation1.next_to(rectangle, RIGHT*2)
        equation2.next_to(rectangle, RIGHT*2)
        equation3.next_to(rectangle, RIGHT*2)
        self.play(Write(equation1),run_time = 1.5)
        self.play(Transform(equation1, equation2),run_time = 1.5)
        self.play(Transform(equation2, equation3),run_time = 1.5)
        self.wait(1)
        # all = VGroup(*self.mobjects)
        
        text = Text("是不是有点思路了？")
        text.shift(DOWN*2)
        self.play(Write(text))
        self.wait(1)
        self.clear()


# class scene4(Scene):
#     def construct(self):
        text1 = Text("回到前面的问题，如果是100层金字塔，等式为：", font_size=40)
        equation1 = MathTex(r"1+2+3+4+ ... +100 =", "Sum")
        text1.next_to(equation1, UP*3)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(Write(equation1))
        self.wait(1)
        self.play(FadeOut(text1))
        self.wait(1)
        text2 = Text("如果我们把等式也旋转180度，效果会怎么样？", font_size=40)
        text2.next_to(equation1, UP*3)
        self.play(FadeIn(text2))
        self.wait(1)
        equation2 = equation1.copy()
        self.play(equation1.animate.shift(UP*0.4), equation2.animate.shift(DOWN*0.4))
        self.wait(1)
        equation3 = MathTex(r"100+ ... +4+3+2+1 =","Sum").align_to(equation2, DOWN)
        self.play(Transform(equation2, equation3))
        text3 = Text("根据前面的思路，我们把对齐的两个数字相加", font_size=40)
        text3.align_to(text2, UP)
        self.play(FadeOut(text2), FadeIn(text3))
        self.wait(1)
        equation4 = MathTex(r"101+101+101+101+ ... +101", "= Sum+Sum").next_to(equation3, DOWN)
        self.play(Write(equation4))
        self.wait(1)
        brace1 = Brace(equation4[0], DOWN)
        brace_text1 = brace1.get_text("100")
        equation5 = MathTex(r"(100+1)*100 =", "2*Sum").next_to(equation3, DOWN)
        self.play(GrowFromCenter(brace1), Write(brace_text1))
        self.wait(1)
        self.play(FadeOut(brace1), FadeOut(brace_text1))
        self.wait(0.5)
        self.play(Transform(equation4, equation5))
        self.wait(1)
        text4 = Text("现在我们很容易就能得到小球的总数了", font_size=40)
        equation6 = MathTex(r"Sum =", r"\frac{(100+1)*100}{2}").next_to(equation5, DOWN)
        text4.align_to(text1, UP)
        equation6.next_to(equation5, DOWN)
        self.play(FadeOut(text3), FadeIn(text4))
        self.wait(1)
        self.play(Write(equation6))
        self.wait(1)
        
        text5 = Text("按照这个规律，我们便可以得到n层金字塔小球总数公式", font_size=40).align_to(text4, UP)
        equation7 = MathTex(r"Sum =", r"\frac{(n+1)*n}{2}").next_to(equation5, DOWN)
        self.play(FadeOut(text4), FadeIn(text5))
        self.wait(2)
        self.play(Transform(equation6, equation7))
        self.wait(2)
        self.clear()
        
        text = Text("这种通过特殊情况得到一般情况的计算公式的方法叫做数学归纳法", font_size=30)
        text2 = Text("这种求和方式叫做高斯求和", font_size=30).next_to(text, DOWN)
        text3 = Text("这个金字塔问题可以看成是等差数列问题中的一种", font_size=30).next_to(text2, DOWN)
        self.play(Write(text))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        
        
    def create_pyramid(self, n, reverse=False):
        pyramid = VGroup()
        for i in range(1, n + 1):
            
            row = VGroup(*[Circle(color=WHITE, fill_opacity=1, radius=0.2) for _ in range(i)])
            row.arrange(buff=0.2)
            row.next_to(pyramid, DOWN*1)
            pyramid.add(row)
        # pyramid.scale(0.8)
        pyramid.shift([0, 0, 0]-pyramid.get_center())
        return pyramid
    
    def create_rectangle(self, rows, cols):
        rectangle = VGroup()
        for i in range(1, rows + 1):
            row = VGroup(*[Circle(color=WHITE, fill_opacity=1, radius=0.2) for _ in range(cols)])
            row.arrange(buff=0.2)
            row.next_to(rectangle, DOWN*1)
            rectangle.add(row)
        # rectangle.scale(0.8)
        rectangle.shift([0, 0, 0]-rectangle.get_center())
        return rectangle