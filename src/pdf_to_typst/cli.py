from __future__ import annotations

import argparse
from pathlib import Path

from pdf_to_typst.converter import convert_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf2typst",
        description="Convert a PDF to markdown or HTML using marker-pdf.",
    )
    parser.add_argument("input_pdf", type=Path, help="Path to input PDF file.")
    parser.add_argument(
        "--format",
        choices=["markdown", "html"],
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file path. Defaults to input filename with .md/.html extension.",
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Use Marker LLM mode for improved accuracy.",
    )
    parser.add_argument(
        "--force-ocr",
        action="store_true",
        help="Force OCR for all text regions.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    output = convert_pdf(
        input_pdf=args.input_pdf,
        output_format=args.format,
        output_path=args.output,
        use_llm=args.use_llm,
        force_ocr=args.force_ocr,
    )
    print(f"Written: {output}")


if __name__ == "__main__":
    main()
