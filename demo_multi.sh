#!/bin/bash
export CUDA_VISIBLE_DEVICES="2"
marker "./pdf_documents_demo_v2" \
    --output_dir "./pdf_demorun_multi_v2" \
    --output_format "markdown" \
    --languages "th,en,_math" \
    --skip_existing \
    --disable_image_extraction \
    --disable_multiprocessing