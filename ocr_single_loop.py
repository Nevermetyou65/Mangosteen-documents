"""Run single ocr in loop"""

import subprocess
from pathlib import Path

from loguru import logger
from alive_progress import alive_bar


def run_marker(document_dir):
    output_dir = Path("documents/extract_result") / f"{document_dir.name}_extracted"
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Output directory: {output_dir}")
    else:
        logger.debug(f"Output directory already exists: {output_dir}")

    documents = list(document_dir.glob("*"))
    logger.info(f"Found {len(documents)} documents in {document_dir}")

    for doc in documents:
        command = [
            "marker_single",
            str(doc),
            "--output_dir",
            str(output_dir),
            "--output_format",
            "markdown",
            "--disable_image_extraction",
            "--force_ocr",
            "--strip_existing_ocr",
            "--redo_inline_math",
            "--use_llm",
            "--llm_service",
            "marker.services.ollama.OllamaService",
            "--ollama_base_url",
            "http://localhost:11434",
            "--ollama_model",
            "llama3.2-vision:11b",
            "--debug"
        ]

        # logger.debug(f"Running command: {' '.join(command)}")

        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logger.info("OCR completed successfully for: %s", doc)
            logger.debug("stdout: %s", result.stdout)
        except subprocess.CalledProcessError as e:
            logger.error("Error processing %s: %s", doc, e)
            logger.error("stderr: %s", e.stderr)
        except Exception as e:
            logger.error("Unexpected error processing %s: %s", doc, e)

        break


def main():
    """Main function to run OCR with marker_single"""
    input_dirs = Path("documents/inputs")
    if not input_dirs.exists():
        raise ValueError("Input directory not found")
    else:
        input_dirs = list(Path("documents/inputs").glob("*"))
        input_dirs = [d for d in input_dirs if d.is_dir()]

    logger.info(f"Found {len(input_dirs)} input directories to process")

    with alive_bar(len(input_dirs), bar="halloween", theme="scuba") as bar:
        for input_dir in input_dirs:
            logger.info(f"Processing directory: {input_dir}")

            run_marker(input_dir)

            bar.text(f"Finished processing {input_dir.name}")
            bar()


if __name__ == "__main__":
    main()
