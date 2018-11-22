#! -*- coding:utf-8 -*-


class Settings:
    """存储《外星人入侵》的所有设置类"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (50, 50, 50)
        # 飞船设置
        self.ship_speed_factor = 0.2
        # 子弹设置
        self.bullet_speed_factor = 0.2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 8
        # 外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
