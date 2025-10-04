# Common progressions per mode (Roman numerals)
COMMON_PROGRESSIONS = {
    'ionian': ['I-IV-V', 'I-vi-IV-V', 'ii-V-I'],
    'dorian': ['i-IV-v', 'i-VII-IV', 'i-ii-IV'],
    'phrygian': ['i-bII-III', 'i-v-bVI-bII'],
    'lydian': ['I-II-V', 'I-IV#-V'],
    'mixolydian': ['I-bVII-IV', 'I-V-vi-IV'],
    'aeolian': ['i-VI-III-VII', 'i-iv-v', 'i-VII-VI'],
    'locrian': ['i°-bII-bIII', 'Rarely used, try i°-bVII-bVI']  # Locrian is tricky
}

# Emotion-based progressions (compiled from common sources)
EMOTIONS = {
    'jazzy': ['ii-V-I', 'ii-V-I-IV'],
    'happy': ['I-IV-V', 'I-V-vi-IV'],
    'sad': ['i-vi-IV-V', 'i-iv-v'],
    'epic': ['I-V-vi-IV', 'I-V-vi-iii-IV-I-IV-V'],
    'cool': ['ii-V-I', 'i-VII-IV'],
    'weird': ['I-vi-iii-V'],
    'love': ['vi-IV-I-V'],
    'mysterious': ['i-VII-i', 'i-bII']
    # Add more as needed, e.g., 'magical': ['i-vi-i-vi']
}

# Roman to degree mapping (ignoring flats/sharps for simplicity, adapt to diatonic)
ROMAN_TO_DEGREE = {
    'I': 1, 'i': 1,
    'II': 2, 'ii': 2, 'bII': 2,
    'III': 3, 'iii': 3, 'bIII': 3,
    'IV': 4, 'iv': 4, '#IV': 4, 'IV#': 4,
    'V': 5, 'v': 5,
    'VI': 6, 'vi': 6, 'bVI': 6,
    'VII': 7, 'vii': 7, 'bVII': 7
}

import random


def resolve_progression(prog_str, diatonic_chords):
    """Resolve Roman numeral progression to actual chord names in the key/mode."""
    parts = prog_str.split('-')
    resolved = []
    for p in parts:
        norm_p = p.upper().replace('#', '#').replace('B', 'b')  # Normalize
        degree = ROMAN_TO_DEGREE.get(norm_p, None)
        if degree:
            full_chord = diatonic_chords[degree - 1]
            # Extract chord name, e.g., 'C maj' -> 'C', 'D min' -> 'Dm', 'A dim' -> 'Adim'
            chord_parts = full_chord.split(': ')[1].split(' (')[0]  # 'C maj'
            root, qual = chord_parts.split(' ')
            if qual == 'maj':
                chord_name = root
            elif qual == 'min':
                chord_name = root + 'm'
            else:
                chord_name = root + 'dim'
            resolved.append(chord_name)
        else:
            resolved.append(p)  # Fallback if not resolvable
    return ' - '.join(resolved) + f" ({prog_str})"


def suggest_progressions(mode, diatonic_chords, emotion=''):
    """Suggest common or emotion-based progressions, resolved to chords."""
    mode = mode.lower()
    if emotion:
        progs = EMOTIONS.get(emotion.lower(), [])
        if not progs:
            return ["No progressions found for that emotion. Using mode defaults."] + suggest_progressions(mode,
                                                                                                           diatonic_chords)
    else:
        progs = COMMON_PROGRESSIONS.get(mode, ['No common progressions defined'])

    suggestions = [resolve_progression(p, diatonic_chords) for p in progs]

    # Add a random progression
    degrees = random.sample(range(1, 8), 4)
    random_roman = '-'.join([str(d) for d in degrees])  # Simple numeric
    random_resolved = ' - '.join([diatonic_chords[d - 1].split(': ')[1].split(' (')[0].replace(' maj', '').replace(
        ' min', 'm').replace(' dim', 'dim') for d in degrees]) + f" (Random: {random_roman})"
    suggestions.append(random_resolved)

    return suggestions