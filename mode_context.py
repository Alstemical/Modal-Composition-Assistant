MODE_CHARACTER = {
    'ionian': 'Bright and happy sound due to its major 3rd and perfect intervals; creates a sense of resolution and stability. Use it when you want uplifting, consonant melodies or harmonies—perfect for pop songs, classical symphonies, or any upbeat track where familiarity breeds comfort. Why? It\'s the "default" scale most people know, avoiding tension for straightforward emotional highs. Jam over major chord progressions like I-IV-V to feel heroic or joyful.',
    'dorian': 'Minor with a twist—a raised 6th gives it a brighter, less gloomy feel than natural minor, blending melancholy with hope. Use it for introspective or groovy vibes in jazz solos (over minor 7 chords), folk tunes like "Scarborough Fair," or rock riffs (e.g., Santana\'s "Oye Como Va"). Why? The flat 3rd adds sadness, but the major 6th lifts it, making it versatile for modal interchange without full resolution. When? In minor keys needing flavor without darkness—try improvising over i-IV progressions.',
    'phrygian': 'Dark and exotic, thanks to the flat 2nd creating tension right from the start, evoking mystery or intensity. Use it in flamenco guitar, heavy metal leads (for that "evil" edge), or Middle Eastern-inspired music. Why? The half-step from root to 2nd builds suspense, perfect for unresolved phrases or dramatic builds. When? Over dominant chords or when you want a Spanish/Arabic flair—experiment with i-bII progressions for cinematic drama.',
    'lydian': 'Bright and dreamy, with a raised 4th adding an ethereal, floating quality that avoids the pull of traditional major. Use it in film scores (e.g., Simpsons theme), jazz improv, or ambient tracks for a sense of wonder or otherworldliness. Why? The sharp 4th creates augmented intervals, suspending resolution for a magical lift. When? Over major chords needing space—try I-II-V for uplifting, non-cliché progressions in fusion or prog rock.',
    'mixolydian': 'Major but bluesy, with a flat 7th injecting a dominant, unresolved edge that feels laid-back yet energetic. Use it in rock (e.g., AC/DC riffs), blues solos, or folk for that "jam band" groove. Why? The b7 lowers tension compared to Ionian, making it great for cycling riffs without full cadence. When? Over dominant 7th chords or in songs blending major feel with soul—go for I-bVII-IV to capture that classic rock swagger.',
    'aeolian': 'Sad and melancholic, as the natural minor scale with flat 3rd, 6th, and 7th emphasizing emotional depth and introspection. Use it in ballads, classical laments, or pop/rock for heartfelt minor key tunes (e.g., many metal ballads). Why? It heightens tension with diminished leading tones, ideal for evoking loss or reflection. When? In minor progressions like i-VI-III-VII for dramatic storytelling—perfect for building to a chorus release.',
    'locrian': 'Dark and unstable, with a diminished root triad and flat everything except the 4th, making it tense and dissonant. Rarely used standalone due to lack of resolution; employ it for brief passages in jazz or experimental music to create unease or transition. Why? The flat 5th destabilizes the tonic, suiting horror soundtracks or avant-garde improv. When? Sparingly—over half-diminished chords or as a passing mode; try i°-bII for weird, unresolved effects in prog or fusion.'
}


# Ionian (Major) scale intervals in semitones
IONIAN_INTERVALS = [2, 2, 1, 2, 2, 2, 1]

# Chromatic notes
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Mode names and their starting positions (0-based index in Ionian scale)
MODES = {
    'ionian': 0,
    'dorian': 1,
    'phrygian': 2,
    'lydian': 3,
    'mixolydian': 4,
    'aeolian': 5,
    'locrian': 6
}

# Chord qualities for each mode (triads: maj, min, dim)
CHORD_QUALITIES = {
    'ionian': ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim'],
    'dorian': ['min', 'min', 'maj', 'maj', 'min', 'dim', 'maj'],
    'phrygian': ['min', 'maj', 'maj', 'min', 'dim', 'maj', 'min'],
    'lydian': ['maj', 'maj', 'min', 'dim', 'maj', 'min', 'min'],
    'mixolydian': ['maj', 'min', 'dim', 'maj', 'min', 'min', 'maj'],
    'aeolian': ['min', 'dim', 'maj', 'min', 'min', 'maj', 'maj'],
    'locrian': ['dim', 'maj', 'min', 'min', 'maj', 'maj', 'min']
}

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


def get_scale_notes(key, mode):
    """Generate notes for a given key and mode by rotating Ionian intervals."""
    if key not in NOTES:
        return None, "Invalid key. Choose from: " + ', '.join(NOTES)
    if mode.lower() not in MODES:
        return None, "Invalid mode. Choose from: " + ', '.join(MODES.keys())

    mode = mode.lower()
    # Rotate Ionian intervals based on mode's starting position
    start_pos = MODES[mode]
    intervals = IONIAN_INTERVALS[start_pos:] + IONIAN_INTERVALS[:start_pos]

    # Calculate notes
    start_idx = NOTES.index(key)
    notes = [key]
    current_idx = start_idx
    for interval in intervals[:-1]:  # Exclude last interval
        current_idx = (current_idx + interval) % 12
        notes.append(NOTES[current_idx])
    return notes, None


def get_ionian_relation(key, mode):
    """Find the relative Ionian key for the given mode."""
    mode = mode.lower()
    if mode == 'ionian':
        return f"{key} Ionian is the Major scale itself."

    # Calculate steps back to Ionian based on mode position
    start_pos = MODES[mode]
    steps_back = sum(IONIAN_INTERVALS[:start_pos]) % 12
    ionian_idx = (NOTES.index(key) - steps_back) % 12
    ionian_key = NOTES[ionian_idx]
    return f"{key} {mode.capitalize()} is the {start_pos + 1}th mode of {ionian_key} Ionian."


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


def main():
    print("Enter a key (e.g., C, C#):")
    key = input().strip()
    print("Enter a mode (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian):")
    mode = input().strip()
    print("Enter an emotion/feeling (e.g., Jazzy, Happy, Sad, Epic; leave blank for mode defaults):")
    emotion = input().strip()

    notes, error = get_scale_notes(key, mode)
    if error:
        print(error)
        return

    print(f"\nNotes in {key} {mode}:")
    print(' -> '.join(notes))
    print("\nContext and Usage:")
    print(MODE_CHARACTER.get(mode.lower(), "No context available."))
    print("\nRelation to Ionian Scale:")
    print(get_ionian_relation(key, mode))
    print("\nDiatonic Chords:")
    diatonic_chords = get_diatonic_chords(notes, mode)
    print('\n'.join(diatonic_chords))
    print("\nSuggested Progressions:")
    print('\n'.join(suggest_progressions(mode, diatonic_chords, emotion)))


if __name__ == "__main__":
    main()
