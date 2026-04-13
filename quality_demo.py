from agents.quality_evaluator import evaluate_conversation
from agents.adaptive_policy import adapt

history = ['hello','help me','help me','help me']
score, issues = evaluate_conversation(history, 6)
action = adapt(score, issues)
print(score, issues, action)
