"""Run single ocr in loop"""

import os
import subprocess
import logging
from pathlib import Path
from time import sleep

from alive_progress import alive_bar

logging.basicConfig(level=os.getenv("LOG_LEVEL", "DEBUG"))
logger = logging.getLogger("alive_progress")


def run_marker(document_dir: Path):
    output_dir = Path("documents/extract_result") / f"{document_dir.name}_extracted"
    documents = list(document_dir.glob("*.pdf"))
    logger.debug(f"Found {len(documents)} pdf documents in {document_dir}")
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
            "--use_llm",
            "--gemini_api_key",
            os.getenv("GEMINI_API_KEY"),
            "--retry_wait_time",
            "7",
        ]

        logger.debug("Running command...")
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logger.debug("OCR completed successfully for: %s", doc)
            logger.debug("stdout: %s", result.stdout)
        except subprocess.CalledProcessError as e:
            logger.error("Error processing %s: %s", doc, e)
            logger.error("stderr: %s", e.stderr)
        except Exception as e:
            logger.error("Unexpected error processing %s: %s", doc, e)

    logger.debug(f"Finished processing {document_dir.name}")
    sleep(5)


def main():
    """Main function to run OCR with marker_single"""
    input_dirs = Path("documents/inputs")
    if not input_dirs.exists():
        raise ValueError("Input directory not found")
    else:
        input_dirs = list(Path("documents/inputs").glob("*"))
        input_dirs = [d for d in input_dirs if d.is_dir()]

    logger.debug(f"Found {len(input_dirs)} input directories to process")

    with alive_bar(len(input_dirs), bar="halloween", theme="scuba") as bar:
        for input_dir in input_dirs:
            logger.debug(f"Processing directory: {input_dir}")
            run_marker(input_dir)
            bar.text(f"Finished processing {input_dir.name}")
            bar()


if __name__ == "__main__":
    main()
