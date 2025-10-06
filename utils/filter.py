from tqdm.auto import tqdm
from utils.utils import open_json, open_md
from utils.count_thai import detect_thai

def filter_by_image(marker_json_files: list[str], logger):
    """Filter PDFs where the number of 'Picture' blocks per page is less than 1."""
    remain = []
    for file_path in tqdm(marker_json_files):
        try:
            data = open_json(file_path)
            page_stats = data.get("page_stats", [])
            if not page_stats:
                logger.warning(f"No page stats found in {file_path}, skipping.")
                continue

            num_all_pic = sum(
                count
                for page in page_stats
                for block, count in page.get("block_counts", [])
                if block == "Picture"
            )
            num_all_pages = len(page_stats)
            if (num_all_pic / num_all_pages) < 1:
                remain.append(file_path)

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")

    logger.info(f"Num remain: {len(remain)}:,")
    return remain


def filter_by_lang(md_files: list[str], logger):
    """Filter PDFs that are detected to be in Thai with a probability > 0.5."""
    remain = []
    for md_path in tqdm(md_files):
        try:
            md_content = open_md(md_path)
            score = detect_thai(md_content)
            if score > 0.5:
                remain.append(md_path)

        except Exception as e:
            logger.error(f"Cannot read OCR result for {md_path}: {e}")

    logger.info(f"Num remain: {len(remain)}")
    return remain