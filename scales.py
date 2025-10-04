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


def ordinal(n):
    """Convert number to ordinal string (1st, 2nd, 3rd, etc.)."""
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


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


def get_wh_pattern(intervals):
    """Convert semitone intervals to W-H string for user explanation.
    W = whole step (2 semitones), H = half step (1 semitone)."""
    wh_map = {2: 'W', 1: 'H'}
    return '-'.join(wh_map[interval] for interval in intervals)


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
    return f"{key} {mode.capitalize()} is the {ordinal(start_pos + 1)} mode of {ionian_key} Ionian."