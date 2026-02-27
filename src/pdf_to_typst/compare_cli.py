from __future__ import annotations

import argparse
from pathlib import Path

from pdf_to_typst.compare import compare_pdfs, format_comparison_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf-compare",
        description="Compare two PDFs by extracted text similarity and overlap.",
    )
    parser.add_argument("left_pdf", type=Path, help="Path to first PDF file.")
    parser.add_argument("right_pdf", type=Path, help="Path to second PDF file.")
    parser.add_argument(
        "--report-output",
        type=Path,
        default=None,
        help="Optional output file path for the comparison report.",
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

    result = compare_pdfs(
        left_pdf=args.left_pdf,
        right_pdf=args.right_pdf,
        use_llm=args.use_llm,
        force_ocr=args.force_ocr,
    )
    report = format_comparison_report(result)

    if args.report_output is not None:
        args.report_output.parent.mkdir(parents=True, exist_ok=True)
        args.report_output.write_text(report + "\n", encoding="utf-8")
        print(f"Written comparison report: {args.report_output}")

    print(report)


if __name__ == "__main__":
    main()
