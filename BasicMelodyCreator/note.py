import enum
import numpy as np
import pygame.midi as midi

BASE_FREQ = 440

NOTE_MIDI_DICT = {'C': 24, 'D': 26, 'E': 28, 'F': 29, 'G': 31, 'A': 33, 'B': 35, 'C#': 25, 'D#': 27, 'F#': 30, 'G#': 32,
                  'A#': 34}

NOTE_LIST = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


class NoteName(enum.Enum):
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    A = 'A'
    B = 'B'
    C_DIEZ = 'C#'
    D_DIEZ = 'D#'
    F_DIEZ = 'F#'
    G_DIEZ = 'G#'
    A_DIEZ = 'A#'


class Note:
    def __init__(self, name, octave=3):
        self.name = self.get_name(name)
        self.octave = octave
        self.midi_code = NOTE_MIDI_DICT[self.name] + octave * 12
        self.frequency = self.get_frequency()

    def get_frequency(self):
        freq = midi.midi_to_frequency(NOTE_MIDI_DICT[self.name] + (self.octave - 1) * 12)
        return freq

    def get_name(self, name):
        if isinstance(name, str):
            return name
        return name.value

    def __str__(self):
        return self.name


class NotePlay:
    def __init__(self, note, color, x_location, y_location, play):
        self.note = note
        self.color = color
        self.x_location = x_location
        self.y_location = y_location
        self.play = play

    def play_note(self, pygame, duration=0, midi=False):
        if midi:
            buffer = np.sin(2 * np.pi * np.arange(44100) * self.note.frequency / 44100).astype(np.float32)
            sound = pygame.mixer.Sound(buffer)
            sound.play(0)
            pygame.time.wait(duration)
        else:
            self.play_wav(pygame)

    def play_wav(self, pygame, duration=0):
        filename = 'data/Notes/{}.wav'.format(self.note.name)
        sound = pygame.mixer.Sound(filename)
        sound.play()
        pygame.time.wait(duration)
