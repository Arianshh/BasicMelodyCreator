import pygame
import math
import enum

from note import *
from chord import *
from scale import *


class Mode(enum.Enum):
    SCALE = 'scale'
    CHORD = 'chord'


class Simulation:
    def __init__(self, frame_per_second, width, height, movement, initial_x, initial_y):
        self.frame_per_second = frame_per_second
        self.width = width
        self.height = height
        self.movement = movement
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = (255, 150, 113)
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.clock = pygame.time.Clock()

        # initial_x = WIDTH / 2 + r * math.cos(math.radians(angle_x))
        # initial_y = HEIGHT / 2 + r * math.sin(math.radians(angle_y))

    def initialize(self):
        mode = input('Select Mode: 1-Scale 2-Chord\n')
        while mode not in ['1', '2']:
            mode = input('Wrong Input.\nSelect Mode: 1-Scale 2-Chord\n')
        mode = Mode.SCALE if mode == '1' else Mode.CHORD
        self.mode = mode
        if mode == Mode.SCALE:
            note = input('Select Note: C, D, E, F, G, A, B\n')
            while note.upper() not in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
                note = input('Wrong Input.\nSelect Note: Select Note: C, D, E, F, G, A, B\nn')
            self.note = note.upper()
            scale = input('Select scale: ' + ', '.join([s.value for s in ScaleName]) + '\n')
            while scale not in [s.value for s in ScaleName]:
                scale = input('Wrong Input.\nSelect scale: ' + ', '.join([s.value for s in ScaleName]) + '\n')
            self.variation = [s for s in ScaleName if s.value == scale][0]
        elif mode == Mode.CHORD:
            pass
        self.run_function = self.fetch_run_function

    def fetch_run_function(self, mode, note, variation):
        pygame.init()
        if mode == Mode.SCALE:
            scale = Scale(variation, note)
            return self.run_scale(scale)
        elif mode == Mode.CHORD:
            return self.run_chord(note, variation)

    def run_scale(self, scale):
        print(scale.notes)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()
        # self.screen.fill(self.background_color)
        #
        # dot_x = self.width / 2 + self.movement.radius * math.cos(math.radians(self.movement.angle_x))
        # dot_y = self.height / 2 + self.movement.radius * math.sin(math.radians(self.movement.angle_y))
        # self.movement.angle_x += self.movement.speed_x
        # self.movement.angle_y += self.movement.speed_y
        # if pygame.math.Vector2((initial_x, initial_y)).distance_to(
        #         pygame.math.Vector2(dot_x, dot_y)) < 30:
        #     chord_cycle += 1
        #     if chord_cycle == change_limit:
        #         c_change = True
        #         chord_cycle = 0

        # if c_change:
        #     c_change = False
        #     chord_option = chord_option + 1 if chord_option < len(chords) - 1 else 0

        # for i, note in enumerate(chords[chord_option]):
        #     if pygame.math.Vector2((note.x_location, note.y_location)).distance_to(
        #             pygame.math.Vector2(dot_x, dot_y)) < 50:
        #         if note.play:
        #             note.play_note(pygame)
        #             note.play = False
        #     # Draw the circles on the screen
        #     if not note.play and (pygame.math.Vector2((note.x_location, note.y_location)).distance_to(
        #             pygame.math.Vector2(dot_x, dot_y)) > 50):
        #         note.play = True
        #     if i == 0:
        #         pygame.draw.circle(self.screen, c1, (note.x_location, note.y_location), 60)
        #     elif i == 1:
        #         pygame.draw.circle(self.screen, c2, (note.x_location, note.y_location), 60)
        #     elif i == 2:
        #         pygame.draw.circle(self.screen, c3, (note.x_location, note.y_location), 60)
        #     else:
        #         pygame.draw.circle(self.screen, c4, (note.x_location, note.y_location), 60)
        #
        # # Draw the dot on the screen
        # pygame.draw.circle(self.screen, (0, 0, 0), (dot_x, dot_y), 5)
        #
        # # Update the display
        # pygame.display.flip()

    def run_chord(self, note, variation):
        pass


class Movement:
    def __init__(self, radius, speed_x, speed_y, dot_x=0, dot_y=0, angle_x=0, angle_y=0):
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.dot_x = dot_x
        self.dot_y = dot_y
        self.angle_x = angle_x
        self.angle_y = angle_y
