def adapt(score, issues):
    if score < 0.5:
        return 'rephrase_or_escalate'
    if 'repetition_detected' in issues:
        return 'change_prompting_strategy'
    return 'continue'
