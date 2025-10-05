import subprocess
import logging
import os

from datetime import datetime

# Generate current date as a string
date_string = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD

# Configure logging
log_folder = "log"
# os.makedirs(log_folder, exist_ok=True)  # Ensure the log folder exists
log_file = os.path.join(log_folder, f"application_{date_string}.log")

logging.basicConfig(
    filename=log_file,
    level=logging.WARNING,  # Set logging level to WARNING
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Date format
)

if __name__ == "__main__":
    pdf = "./pdf_documents"
    output_dir = "./ocr_results"
    output_format = "markdown"
    languages = "th,en"
    workers = "8"
    
    command = [
        "marker",
        pdf,
        "--output_dir", output_dir,
        "--debug",
        "--output_format", output_format,
        "--force_ocr",
        "--languages", languages,
        "--workers", workers,
    ]
    
    # Run the command
    try:
        subprocess.run(command, check=True)
        logging.info("Command executed successfully!")
    except subprocess.CalledProcessError as e:
        logging.warning(f"Error occurred: {e}")
        print("An error occurred. Check the log file for details.")

