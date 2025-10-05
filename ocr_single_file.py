import subprocess

if __name__ == "__main__":
    pdf = "./n_gram_language_model.pdf"
    output_dir = "./result_tmp_eq_copy2/"
    output_format = "markdown"
    page_range = "1-2"
    languages = "th,en"
    
    command = [
        "marker_single",
        pdf,
        "--output_dir", output_dir,
        "--debug",
        "--output_format", output_format,
        "--page_range", page_range,
        "--force_ocr",
        "--languages", languages
    ]
    
    # Run the command
    try:
        subprocess.run(command, check=True)
        print("Command executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
