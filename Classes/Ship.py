import pygame
from Classes.Vector import Vector


FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
TURN_UP = 3
TURN_DOWN = 4
BACKGROUND_COLOR = (0, 0, 0)
COLOR_SPACEHIP = (25, 0, 100)
COLOR_LINE = (0, 255, 0)
DISPLAY_W = 800
DISPLAY_H = 600


class Ship:
    def __init__(self, pos):
        self.pos = Vector(pos)
        self.image = pygame.Surface((50, 20), pygame.SRCALPHA)
        self.speed = Vector((50, 0))
        self.speed_rotate = 90
        self.boost = 100 # ускорение
        self.w = 50
        self.h = 20
        self.state = NORMAL
        self.last_state = NORMAL  # ?? тема с поворотом
        self.draw()

    def events(self, event):  # !
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
            if event.key == pygame.K_DOWN:
                self.state = TURN_DOWN
            if event.key == pygame.K_UP:
                self.state = TURN_UP
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self, dt):  # !
        if self.state == TURN_LEFT:
            self.speed.rotate(-self.speed_rotate*(dt/1000))
        if self.state == TURN_RIGHT:
            self.speed.rotate(self.speed_rotate*(dt/1000))
        if self.state == TURN_DOWN:
            self.speed -= self.speed.normalize()*self.boost*(dt/1000)
        if self.state == TURN_UP:
            self.speed += self.speed.normalize()*self.boost*(dt/1000)
        # self.speed *= (dt/1000)
        self.pos += self.speed*(dt/1000)
        #self.last_state = self.state
        if self.pos.x < 0:
            self.pos.x = DISPLAY_W - self.w
        if self.pos.x > DISPLAY_W - self.w:
            self.pos.x = 0
        if self.pos.y < self.h:
            self.pos.y = DISPLAY_H -  self.h
        if self.pos.y > DISPLAY_H - self.h:
            self.pos.y = self.h

    def draw(self):

        # pygame.draw.polygon(self.image, COLOR_SPACEHIP, [(0, 0), (0, self.h), (self.w * 0.75, self.h * (3 / 4)),
        #                                                  (self.w * (5 / 6), self.h * (3 / 4)), (self.w / 2, self.h / 2),
        #                                                  (self.w * (5 / 6), self.h * (1 / 4)),
        #                                                  (self.w / 4, self.h * (1 / 4)),
        #                                                  (0, 0)])
        # pygame.draw.rect(self.image, COLOR_SPACEHIP, [(0, 0), (self.w, self.h)], 1)
        pygame.draw.polygon(self.image, COLOR_SPACEHIP, [(0, 0), (0, self.h), (self.w, self.h * 0.5), (0, 0)])


    def render(self, screen):

        rot_image = pygame.transform.rotate(self.image, self.speed.angle)
        rot_rect = rot_image.get_rect()
        rot_rect.center = self.image.get_rect().center
        rot_rect.move_ip(self.pos.as_point())
        # self.image = image.subsurface(rot_rect).copy()
        #
        dv = Vector((self.w / 2, self.h / 2))
        screen.blit(rot_image, rot_rect)
        # screen.blit(self.image, self.pos.as_point())
        pygame.draw.line(screen, COLOR_LINE, (self.pos + dv).as_point(), (self.pos + dv + self.speed).as_point())
