import enum

from note import Note, NOTE_LIST


class ChordName(enum.Enum):
    MAJOR = 'major'
    MINOR = 'minor'
    MAJOR_SEVENTH = 'maj7'
    MINOR_SEVENTH = 'min7'
    DOMINANT_SEVENTH = 'dom7'
    MAJOR_NINTH = 'maj9'
    MINOR_NINTH = 'min9'
    DOMINANT_NINTH = 'dom9'
    MAJOR_ELEVENTH = 'maj11'
    MINOR_ELEVENTH = 'min11'
    DIMINISHED = 'dim'
    DIMINISHED_SEVENTH = 'dim7'
    SUS_TWO = 'sus2'
    SUS_FOUR = 'sus4'
    AUGMENTED = 'aug'


class Chord:
    def __init__(self, name, note):
        self.name = name
        self.note = Note(name=note.value)
        self.set_notes()

    def set_notes(self):
        if self.name == ChordName.MAJOR:
            self.notes = self.build_chord([0, 4, 7])
        elif self.name == ChordName.MINOR:
            self.notes = self.build_chord([0, 3, 7])
        elif self.name == ChordName.DIMINISHED:
            self.notes = self.build_chord([0, 3, 6])
        elif self.name == ChordName.DIMINISHED_SEVENTH:
            self.notes = self.build_chord([0, 3, 6, 9])
        elif self.name == ChordName.MAJOR_SEVENTH:
            self.notes = self.build_chord([0, 4, 7, 11])
        elif self.name == ChordName.MINOR_SEVENTH:
            self.notes = self.build_chord([0, 3, 7, 10])
        elif self.name == ChordName.DOMINANT_SEVENTH:
            self.notes = self.build_chord([0, 4, 7, 10])
        elif self.name == ChordName.SUS_TWO:
            self.notes = self.build_chord([0, 2, 7])
        elif self.name == ChordName.SUS_FOUR:
            self.notes = self.build_chord([0, 5, 7])
        elif self.name == ChordName.AUGMENTED:
            self.notes = self.build_chord([0, 4, 8])
        elif self.name == ChordName.MAJOR_NINTH:
            self.notes = self.build_chord([0, 4, 7, 11, 14])
        elif self.name == ChordName.MINOR_NINTH:
            self.notes = self.build_chord([0, 4, 7, 10, 14])
        elif self.name == ChordName.MAJOR_ELEVENTH:
            self.notes = self.build_chord([0, 4, 7, 11, 14, 17])
        elif self.name == ChordName.MINOR_ELEVENTH:
            self.notes = self.build_chord([0, 3, 7, 10, 14, 17])

    def build_chord(self, intervals):
        root_note = self.note.name
        notes = [NOTE_LIST[(Chord.get_interval(root_note) + i) % 12] for i in intervals]
        return [Note(n) for n in notes]

    @staticmethod
    def get_interval(note):
        return NOTE_LIST.index(note)
