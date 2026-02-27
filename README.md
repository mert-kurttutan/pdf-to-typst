# pdf-to-typst

Convert a given PDF into Markdown or HTML using the Marker Python library.

## Requirements

- Python `>=3.10,<4.0`
- PyTorch supported environment (CPU/GPU/MPS) as required by `marker-pdf`

## Install

```bash
uv sync
```

## Usage

Convert to Markdown (default):

```bash
uv run pdf-to-typst /path/to/file.pdf
```

Convert to HTML:

```bash
uv run pdf-to-typst /path/to/file.pdf --format html
```

Custom output file:

```bash
uv run pdf-to-typst /path/to/file.pdf --format markdown --output /path/to/output.md
```

Compare two PDFs:

```bash
uv run pdf-compare /path/to/file1.pdf /path/to/file2.pdf
```

Write comparison report to file:

```bash
uv run pdf-compare /path/to/file1.pdf /path/to/file2.pdf --report-output /path/to/report.txt
```

Enable Marker options:

```bash
uv run pdf-to-typst /path/to/file.pdf --use-llm --force-ocr
```

Run modules directly:

```bash
uv run python -m pdf_to_typst.convert_cli /path/to/file.pdf --format markdown
uv run python -m pdf_to_typst.compare_cli /path/to/file1.pdf /path/to/file2.pdf
```

## Notes

- `--use-llm` requires configuring a Marker LLM backend (Gemini/Ollama/OpenAI/etc.).
- By default, output is written next to the input PDF:
  - Markdown: `input.md`
  - HTML: `input.html`
