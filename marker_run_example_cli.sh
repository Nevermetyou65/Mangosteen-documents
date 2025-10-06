marker_single "./documents/inputs/sample_data/pdf_doc_00007.pdf" \
    --output_dir "./documents/extract_result/sample_data_extracted" \
    --ocr_task_name "ocr_without_boxes" \
    --output_format "markdown" \
    --pdftext_workers 8 \
    --disable_image_extraction \
    --force_ocr \
    --use_llm \
    --gemini_api_key $GEMINI_API_KEY \
    --retry_wait_time 7