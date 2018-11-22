#! -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()
    # 创建Settings实例ai_settings
    ai_settings = Settings()
    # 窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 窗口标题
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船实例
    ship = Ship(ai_settings, screen)
    # 创建子弹、外星人编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 飞船、子弹、外星人更新
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
        gf.update_aliens(ai_settings, ship, aliens)
        # 每次循环都会重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
