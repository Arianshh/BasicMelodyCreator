import pygame
import math
import random

from note import *
from scale import *


class Mode(enum.Enum):
    SCALE = 'scale'
    CHORD = 'chord'


COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]


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
            note = note.upper()
            scale = input('Select scale: ' + ', '.join([s.value for s in ScaleName]) + '\n')
            while scale not in [s.value for s in ScaleName]:
                scale = input('Wrong Input.\nSelect scale: ' + ', '.join([s.value for s in ScaleName]) + '\n')
            variation = [s for s in ScaleName if s.value == scale][0]
            scale = Scale(variation, note)
            note_positions = self.generate_notes_coordinates(scale)
            note_play_list = []
            for i, note in enumerate(scale.notes):
                note_play_list += [
                    NotePlay(note, random.choice(COLORS), note_positions[i][0], note_positions[i][1], True)]
            self.note_play_list = note_play_list
        elif mode == Mode.CHORD:
            pass

    def generate_notes_coordinates(self, variation):
        if self.mode == Mode.SCALE:
            scale = variation
            notes = scale.notes
            num_of_notes = len(notes)
            max_radius = min(self.width, self.width) // (2 * math.ceil(math.sqrt(num_of_notes)))
            center_x, center_y = self.width // 2, self.height // 2
            circle_positions = []
            angle_between_circles = 2 * math.pi / num_of_notes
            for i in range(num_of_notes):
                angle = i * angle_between_circles
                x = center_x + int(1.2 * max_radius * math.cos(angle))
                y = center_y + int(1.2 * max_radius * math.sin(angle))
                circle_positions.append((x, y))
            return circle_positions

    def run(self):
        if self.mode == Mode.SCALE:
            self.run_scale()

    def run_scale(self):
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self.screen.fill(self.background_color)

        dot_x = self.width / 2 + self.movement.radius * math.cos(math.radians(self.movement.angle_x))
        dot_y = self.height / 2 + self.movement.radius * math.sin(math.radians(self.movement.angle_y))
        self.movement.angle_x += self.movement.speed_x
        self.movement.angle_y += self.movement.speed_y

        for i, note in enumerate(self.note_play_list):
            if pygame.math.Vector2((note.x_location, note.y_location)).distance_to(
                    pygame.math.Vector2(dot_x, dot_y)) < 50:
                if note.play:
                    note.play_note(pygame)
                    note.play = False
            if not note.play and (pygame.math.Vector2((note.x_location, note.y_location)).distance_to(
                    pygame.math.Vector2(dot_x, dot_y)) > 50):
                note.play = True
            for c_index in range(0, len(self.note_play_list)):
                if i == c_index:
                    pygame.draw.circle(self.screen, note.color, (note.x_location, note.y_location), 60)
        pygame.draw.circle(self.screen, (0, 0, 0), (dot_x, dot_y), 5)
        pygame.display.flip()

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
