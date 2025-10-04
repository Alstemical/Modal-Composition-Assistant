CHORD_QUALITIES = {
    'ionian': ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim'],
    'dorian': ['min', 'min', 'maj', 'maj', 'min', 'dim', 'maj'],
    'phrygian': ['min', 'maj', 'maj', 'min', 'dim', 'maj', 'min'],
    'lydian': ['maj', 'maj', 'min', 'dim', 'maj', 'min', 'min'],
    'mixolydian': ['maj', 'min', 'dim', 'maj', 'min', 'min', 'maj'],
    'aeolian': ['min', 'dim', 'maj', 'min', 'min', 'maj', 'maj'],
    'locrian': ['dim', 'maj', 'min', 'min', 'maj', 'maj', 'min']
}


def get_diatonic_chords(notes, mode):
    """Generate diatonic triads with qualities for the mode."""
    mode = mode.lower()
    qualities = CHORD_QUALITIES[mode]
    chords = []
    is_minorish = qualities[0] in ['min', 'dim']
    roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'] if is_minorish else ['I', 'II', 'III', 'IV', 'V', 'VI',
                                                                                     'VII']

    for i in range(7):
        root = notes[i]
        third = notes[(i + 2) % 7]
        fifth = notes[(i + 4) % 7]
        quality = qualities[i]
        roman = roman_numerals[i].upper() if quality == 'maj' else roman_numerals[i]
        if quality == 'dim':
            roman += '°'
        chords.append(f"{roman}: {root} {quality} ({root}-{third}-{fifth})")
    return chords