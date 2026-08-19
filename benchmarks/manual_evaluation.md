# Manual Summarization Evaluation

## Model

- Model: `qwen3:4b`
- Temperature: `0.2`
- Thinking requested: disabled
- Benchmark runs per sample: `3`
- Warm-up request used before measurements

---

## Quality Evaluation

### Test 1 — Technical Note

- Faithfulness: Good
- Coverage: Good
- Clarity: Good
- Conciseness: Good

Notes:
The model preserved the main technical concepts without adding unsupported information.

### Test 2 — Meeting Notes

- Faithfulness: Good
- Coverage: Weak
- Clarity: Good
- Conciseness: Good

Notes:
The summary omitted the testing owner and incomplete database migration.

### Test 3 — Arabic + English Notes

- Faithfulness: Good
- Coverage: Mostly Good
- Clarity: Good
- Conciseness: Good

Notes:
The model handled mixed Arabic and English well but omitted the planned study topics.

---

# Performance Benchmark

## Technical Note

- Input tokens: 125
- Average output tokens: 424.33
- Average generation time: 11.24 sec
- Average total time: 11.45 sec
- Average speed: 37.88 tokens/sec

Run details:
- Run 1: 408 output tokens, 10.58 sec generation, 10.79 sec total, 38.58 tokens/sec
- Run 2: 379 output tokens, 9.83 sec generation, 10.04 sec total, 38.57 tokens/sec
- Run 3: 486 output tokens, 13.32 sec generation, 13.53 sec total, 36.50 tokens/sec

## Meeting Note

- Input tokens: 106
- Average output tokens: 1272.67
- Average generation time: 37.01 sec
- Average total time: 37.33 sec
- Average speed: 35.94 tokens/sec

Run details:
- Run 1: 2870 output tokens, 85.50 sec generation, 85.78 sec total, 33.57 tokens/sec
- Run 2: 474 output tokens, 12.90 sec generation, 13.32 sec total, 36.74 tokens/sec
- Run 3: 474 output tokens, 12.64 sec generation, 12.87 sec total, 37.50 tokens/sec

## Mixed-Language Note

- Input tokens: 124
- Average output tokens: 2257.67
- Average generation time: 65.97 sec
- Average total time: 66.31 sec
- Average speed: 34.32 tokens/sec

Run details:
- Run 1: 2270 output tokens, 65.70 sec generation, 66.00 sec total, 34.55 tokens/sec
- Run 2: 1911 output tokens, 54.58 sec generation, 54.94 sec total, 35.01 tokens/sec
- Run 3: 2592 output tokens, 77.64 sec generation, 77.99 sec total, 33.38 tokens/sec

## Long-Form Note

- Input tokens: 349
- Average output tokens: 633.33
- Average generation time: 17.35 sec
- Average total time: 17.72 sec
- Average speed: 36.51 tokens/sec

Run details:
- Run 1: 693 output tokens, 19.15 sec generation, 19.75 sec total, 36.18 tokens/sec
- Run 2: 612 output tokens, 16.56 sec generation, 16.82 sec total, 36.96 tokens/sec
- Run 3: 595 output tokens, 16.35 sec generation, 16.60 sec total, 36.39 tokens/sec

---

## Key Findings

- Generation throughput was generally stable at about 34–38 tokens/sec.
- Technical and long-form samples produced relatively stable latency.
- Meeting and mixed-language samples triggered much larger internal generation, causing major latency increases.
- The meeting benchmark contained one clear outlier: 2870 generated tokens and 85.50 sec generation time.
- Mixed-language input consistently triggered very high output-token counts across all three runs.
- Input size alone did not explain latency; generated-token count had a much stronger effect.
- Excessive hidden reasoning remains the main performance concern for `qwen3:4b` on this summarization workload.
- A second local model should be benchmarked with the same samples and settings before choosing the final default model.