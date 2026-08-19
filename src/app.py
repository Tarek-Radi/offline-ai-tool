import argparse

from summarizer import summarize_note


MAX_NOTE_BYTES = 10000


def main() -> None:
    # Create the CLI parser
    parser = argparse.ArgumentParser(
        description="Summarize a note using a local LLM through Ollama."
    )

    # Add the note file path argument
    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the text file containing the note to summarize.",
    )

    # Add optional hosted inference flag
    parser.add_argument(
        "--hosted",
        action="store_true",
        help="Use the hosted inference backend instead of local Ollama.",
    )

    # Parse CLI arguments
    args = parser.parse_args()

    file_path = args.file_path
    use_hosted = args.hosted

    # Read the note file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            note = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    except PermissionError:
        print(f"Error: Permission denied while reading '{file_path}'.")
        return

    except UnicodeDecodeError:
        print(f"Error: Could not decode '{file_path}' as UTF-8.")
        return

    # Validate note content
    if not note.strip():
        print("Error: The note file is empty.")
        return

    # Validate note size
    note_size = len(note.encode("utf-8"))

    if note_size > MAX_NOTE_BYTES:
        print(
            f"Error: Note is too large. "
            f"Maximum supported size is {MAX_NOTE_BYTES} bytes."
        )
        return

    # Model routing
    try:
        summary = summarize_note(
            note,
            use_hosted=use_hosted,
        )

    except RuntimeError as error:
        print(f"Error: {error}")
        return

    # Local inference
    try:
        summary = summarize_note(note, use_hosted=use_hosted)

    except RuntimeError as error:
        print(f"Error: {error}")
        return

    # Display the result
    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()