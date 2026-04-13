def detect_repetition(history):
    return len(history) != len(set(history))


def detect_stall(turns):
    return turns > 5
