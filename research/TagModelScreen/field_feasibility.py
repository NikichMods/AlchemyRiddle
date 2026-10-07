"""Necessary author-level field floor for unique, jointly necessary clues."""


def supports_necessary_clues(compatible_count, clue_count):
    if compatible_count < 0 or clue_count < 1:
        raise ValueError('nonnegative compatible count and positive clue count required')
    return compatible_count >= clue_count + 1
