# Manual Summarization Evaluation

## Test 1 — Technical Note

- Faithfulness: Good
- Coverage: Good
- Clarity: Good
- Conciseness: Good

Notes:
The model preserved the main technical concepts without adding unsupported information.

## Test 2 — Meeting Notes

- Faithfulness: Good
- Coverage: Weak
- Clarity: Good
- Conciseness: Good

Notes:
The summary omitted the testing owner and incomplete database migration.

## Test 3 — Arabic + English Notes

- Faithfulness: Good
- Coverage: Mostly Good
- Clarity: Good
- Conciseness: Good

## Notes:
The model handled mixed Arabic and English well but omitted the planned study topics.

- Model: qwen3:4b
- Input tokens: 96
- Generated tokens: 709
- Generation time: 18.50 sec
- Speed: ~38.3 tokens/sec
- Observed issue: excessive hidden reasoning for simple summarization