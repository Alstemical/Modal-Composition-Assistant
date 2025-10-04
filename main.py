from scales import MODES, IONIAN_INTERVALS, get_scale_notes, get_wh_pattern, get_ionian_relation
from chords import get_diatonic_chords
from progressions import suggest_progressions
from mode_context import MODE_CHARACTER

def main():
    while True:
        print("Enter a key (e.g., C, C#):")
        key = input().strip().upper()
        print("Enter a mode (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian):")
        mode = input().strip().upper()
        print("Enter an emotion/feeling (e.g., Jazzy, Happy, Sad, Epic; leave blank for mode defaults):")
        emotion = input().strip().upper()

        notes, error = get_scale_notes(key, mode)
        if error:
            print(error)
            continue  # Retry on error

        mode_lower = mode.lower()
        start_pos = MODES[mode_lower]
        intervals = IONIAN_INTERVALS[start_pos:] + IONIAN_INTERVALS[:start_pos]
        wh_pattern = get_wh_pattern(intervals)

        print(f"\nNotes in {key} {mode}:")
        print(' -> '.join(notes))
        print(f"\nInterval Pattern (W=whole step, H=half step): {wh_pattern}")
        print("\nContext and Usage:")
        print(MODE_CHARACTER.get(mode_lower, "No context available."))
        print("\nRelation to Ionian Scale:")
        print(get_ionian_relation(key, mode))
        print("\nDiatonic Chords:")
        diatonic_chords = get_diatonic_chords(notes, mode)
        print('\n'.join(diatonic_chords))
        print("\nSuggested Progressions:")
        print('\n'.join(suggest_progressions(mode, diatonic_chords, emotion)))

        print("\nAnother round? (y/n): ")
        if input().strip().lower() != 'y':
            print("Done.")
            break


if __name__ == "__main__":
    main()
