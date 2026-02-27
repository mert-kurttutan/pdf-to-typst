from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from pdf_to_typst.converter import extract_pdf_text


@dataclass(frozen=True)
class ComparisonResult:
    left_pdf: Path
    right_pdf: Path
    similarity_ratio: float
    line_match_ratio: float
    left_line_count: int
    right_line_count: int
    common_line_count: int

    @property
    def identical(self) -> bool:
        return self.similarity_ratio == 1.0 and self.line_match_ratio == 1.0


def _normalize_lines(text: str) -> set[str]:
    return {line.strip() for line in text.splitlines() if line.strip()}


def compare_texts(left_text: str, right_text: str) -> tuple[float, float, int, int, int]:
    left_lines = _normalize_lines(left_text)
    right_lines = _normalize_lines(right_text)
    common_lines = left_lines & right_lines

    similarity = SequenceMatcher(a=left_text, b=right_text).ratio()

    denom = len(left_lines | right_lines)
    line_match = 1.0 if denom == 0 else len(common_lines) / denom

    return similarity, line_match, len(left_lines), len(right_lines), len(common_lines)


def compare_pdfs(
    left_pdf: Path,
    right_pdf: Path,
    *,
    use_llm: bool = False,
    force_ocr: bool = False,
) -> ComparisonResult:
    left_text = extract_pdf_text(
        left_pdf,
        output_format="markdown",
        use_llm=use_llm,
        force_ocr=force_ocr,
    )
    right_text = extract_pdf_text(
        right_pdf,
        output_format="markdown",
        use_llm=use_llm,
        force_ocr=force_ocr,
    )

    similarity, line_match, left_count, right_count, common_count = compare_texts(left_text, right_text)
    return ComparisonResult(
        left_pdf=left_pdf,
        right_pdf=right_pdf,
        similarity_ratio=similarity,
        line_match_ratio=line_match,
        left_line_count=left_count,
        right_line_count=right_count,
        common_line_count=common_count,
    )


def format_comparison_report(result: ComparisonResult) -> str:
    return "\n".join(
        [
            f"Left PDF: {result.left_pdf}",
            f"Right PDF: {result.right_pdf}",
            f"Character similarity: {result.similarity_ratio:.4f}",
            f"Unique-line overlap: {result.line_match_ratio:.4f}",
            f"Left unique lines: {result.left_line_count}",
            f"Right unique lines: {result.right_line_count}",
            f"Common unique lines: {result.common_line_count}",
            f"Identical: {'yes' if result.identical else 'no'}",
        ]
    )
