from pathlib import Path

from src.ollama_client import MODEL_NAME, _call_ollama


NUM_RUNS = 3

SAMPLE_NAMES = [
    "technical.txt",
    "meeting.txt",
    "mixed_language.txt",
    "long_form.txt",
]

benchmark_dir = Path(__file__).resolve().parent
samples_dir = benchmark_dir / "samples"

prompt_path = (
    benchmark_dir.parent
    / "prompts"
    / "summarize.txt"
)

template = prompt_path.read_text(encoding="utf-8")


# Warm up the model before benchmark measurements.
warmup_sample_path = samples_dir / SAMPLE_NAMES[0]
warmup_note = warmup_sample_path.read_text(encoding="utf-8")
warmup_prompt = template.format(note=warmup_note)

print(f"Warming up {MODEL_NAME}...\n")
_call_ollama(warmup_prompt)


print(f"Model: {MODEL_NAME}")
print(f"Runs per sample: {NUM_RUNS}")
print("=" * 50)


for sample_name in SAMPLE_NAMES:
    sample_path = samples_dir / sample_name

    note = sample_path.read_text(encoding="utf-8")
    prompt = template.format(note=note)

    generation_times = []
    total_times = []
    tokens_per_second_values = []
    output_token_counts = []

    input_tokens = 0

    print(f"\nSample: {sample_name}")
    print("-" * 50)

    for run_number in range(1, NUM_RUNS + 1):
        response = _call_ollama(prompt)

        input_tokens = response.prompt_eval_count
        output_tokens = response.eval_count

        generation_seconds = (
            response.eval_duration / 1_000_000_000
        )

        total_seconds = (
            response.total_duration / 1_000_000_000
        )

        tokens_per_second = (
            output_tokens / generation_seconds
        )

        generation_times.append(generation_seconds)
        total_times.append(total_seconds)
        tokens_per_second_values.append(tokens_per_second)
        output_token_counts.append(output_tokens)

        print(f"Run {run_number}")
        print(f"Input tokens: {input_tokens}")
        print(f"Output tokens: {output_tokens}")
        print(
            f"Generation time: "
            f"{generation_seconds:.2f} seconds"
        )
        print(
            f"Total time: "
            f"{total_seconds:.2f} seconds"
        )
        print(
            f"Tokens/sec: "
            f"{tokens_per_second:.2f}"
        )
        print()

    average_generation_time = (
        sum(generation_times) / NUM_RUNS
    )

    average_total_time = (
        sum(total_times) / NUM_RUNS
    )

    average_tokens_per_second = (
        sum(tokens_per_second_values) / NUM_RUNS
    )

    average_output_tokens = (
        sum(output_token_counts) / NUM_RUNS
    )

    print("Average Results")
    print(f"Input tokens: {input_tokens}")
    print(
        f"Average output tokens: "
        f"{average_output_tokens:.2f}"
    )
    print(
        f"Average generation time: "
        f"{average_generation_time:.2f} seconds"
    )
    print(
        f"Average total time: "
        f"{average_total_time:.2f} seconds"
    )
    print(
        f"Average tokens/sec: "
        f"{average_tokens_per_second:.2f}"
    )

    print("=" * 50)