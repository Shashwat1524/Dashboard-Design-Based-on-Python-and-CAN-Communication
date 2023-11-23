import pygame.gfxdraw
import serial
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
pygame.init()
green=(0,250,0)
Red=(255,70,50)
darkRed= (255,0,0)
Blue=(39,170,225)
yellow=(247,148,29)
grey=(61,61,61)
velocity_deg=80
(screen_width, screen_height) = (1024, 600)
background = pygame.image.load('MM01_DASH_BG.png')
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("circle window")
screen.fill((0,0,0))
game_font_digital_large = pygame.font.Font('digital-7.ttf', 280)
game_font_prototype = pygame.font.Font('Prototype.ttf', 20)
game_font_digital_small = pygame.font.Font('digital-7.ttf', 80)
run = True
current=0
rpm=0
voltage=0
speed=0
rpm2=0
if __name__ == '__main__':
    ser = serial.Serial('COM9',115200, timeout=1)
    ser.reset_input_buffer()

while(run):
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    if ser.in_waiting > 0:
        rpm = ser.readline().decode('utf-8').rstrip()
        current = ser.readline().decode('utf-8').rstrip()
        voltage = ser.readline().decode('utf-8').rstrip()
        rpm2=int(rpm)
        speed = int(0.1885*rpm2/4.8*0.12)
        score_surface = game_font_digital_large.render(f'{str(speed)}', True, (39,170,225))
        score_rect = score_surface.get_rect(center=(600, 290))
        screen.blit(score_surface, score_rect)
        score_surface2 = game_font_digital_small.render(f'{str(current)}', True, (39, 170, 225))
        score_rect2 = score_surface2.get_rect(center=(920, 50))
        screen.blit(score_surface2, score_rect2)
        score_surface3 = game_font_digital_small.render(f'{str(voltage)}', True, (39, 170, 225))
        score_rect3 = score_surface3.get_rect(center=(920, 542))
        screen.blit(score_surface3, score_rect3)
        score_surface4 = game_font_digital_small.render(f'{str(current_time)}', True, (255, 255, 255))
        score_rect4 = score_surface4.get_rect(center=(100, 50))
        screen.blit(score_surface4, score_rect4)
        pygame.display.update()