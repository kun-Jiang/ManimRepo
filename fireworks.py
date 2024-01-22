from manim import *
import random

class fireworks(Scene):
    def construct(self):
        # 设置画布大小
        self.camera.frame_width = 10
        self.camera.frame_height = 5

        # 获取画布边界的 x 范围
        x_min, x_max = self.camera.frame_width * LEFT, self.camera.frame_width * RIGHT

        # 在最下端生成随机分布的点
        text1 = Text("江楠楠生日快乐!").shift(UP * 0.5)
        text2 = Text("Happy Birthday!").shift(DOWN * 0.5)
        self.play(Wiggle(text1))
        self.play(Indicate(text2))
        for i in range(5):
            num_dots = 5
            color_list = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK]
            dots = VGroup(*[Dot(color=random.choice(color_list),radius=random.uniform(0.02,0.1)) for _ in range(num_dots)])
            for dot in dots:
                dot.move_to([random.uniform(-5,5), -2, 0])
                
            for dot in dots:
                dot_path = TracedPath(dot.get_center, dissipating_time=1, stroke_opacity=[0, 1])
                self.add(dot, dot_path)
            self.play(*[dot.animate.shift(UP * random.uniform(1,4)) for dot in dots])
            self.play(*[Flash(dot, flash_radius=1,run_time=random.uniform(1,2), lag_ratio = random.uniform(0,5)) for dot in dots])
            self.play(*[FadeOut(dot, run_time = random.random()) for dot in dots])