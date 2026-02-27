from __future__ import annotations

from pathlib import Path


def convert_pdf(
    input_pdf: Path,
    output_format: str,
    output_path: Path | None = None,
    use_llm: bool = False,
    force_ocr: bool = False,
) -> Path:
    from marker.config.parser import ConfigParser
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    if not input_pdf.exists():
        raise FileNotFoundError(f"Input file not found: {input_pdf}")
    if input_pdf.suffix.lower() != ".pdf":
        raise ValueError("Input file must be a PDF.")
    if output_format not in {"markdown", "html"}:
        raise ValueError("output_format must be one of: markdown, html")

    config = {
        "output_format": output_format,
        "use_llm": use_llm,
        "force_ocr": force_ocr,
    }
    config_parser = ConfigParser(config)

    converter = PdfConverter(
        config=config_parser.generate_config_dict(),
        artifact_dict=create_model_dict(),
        processor_list=config_parser.get_processors(),
        renderer=config_parser.get_renderer(),
        llm_service=config_parser.get_llm_service(),
    )
    rendered = converter(str(input_pdf))
    text, _, _ = text_from_rendered(rendered)

    if output_path is None:
        extension = "md" if output_format == "markdown" else "html"
        output_path = input_pdf.with_suffix(f".{extension}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path
