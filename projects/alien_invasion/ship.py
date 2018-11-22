#! -*- coding:-utf-8 -*-
import pygame


class Ship:
    """管理飞船的大部分行为"""
    def __init__(self, ai_setting, screen):
        """接受两个参数，self与screen(指定飞船绘制到什么地方)，初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_setting
        # 加载飞船图像并获取其外接矩形, 返回一个飞船的surface，将其储存到self.image中
        self.image = pygame.image.load('images/ship.bmp')
        # 使用get_rect()获取相应surface的属性rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央,self.rect.centerx为矩形中心X坐标
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存最小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """方法blitem(),在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
