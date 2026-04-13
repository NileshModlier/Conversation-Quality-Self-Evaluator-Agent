from agents.quality_signals import detect_repetition, detect_stall

def evaluate_conversation(history, turn_count):
    issues = []
    if detect_repetition(history):
        issues.append('repetition_detected')
    if detect_stall(turn_count):
        issues.append('conversation_stalled')
    score = max(0, 1 - 0.2 * len(issues))
    return score, issues
