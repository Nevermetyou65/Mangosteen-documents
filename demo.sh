#!/bin/bash
export CUDA_VISIBLE_DEVICES="1"
export GOOGLE_API_KEY="AIzaSyA_K1KJpXVSSyLwp0ldFmLu_aqpKzDLSCY"
marker_single "./pdf_documents_demo/n_gram_language_model.pdf" \
    --output_dir "./pdf_demorun/" \
    --output_format "markdown" \
    --page_range "0-2" \
    --force_ocr \
    --debug \
    --languages "en" \

# marker_single "./pdf_documents_demo/n_gram_language_model.pdf" \
#     --output_dir "./pdf_demorun/n_gran_language_model_l_math/" \
#     --output_format "markdown" \
#     --page_range "0-5" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "en,_math" \

# marker_single "./pdf_documents_demo/n_gram_language_model.pdf" \
#     --output_dir "./pdf_demorun/n_gran_language_model_no_force_ocr/" \
#     --output_format "markdown" \
#     --page_range "0-5" \
#     --strip_existing_ocr \
#     --debug \
#     --languages "en,_math" \

# marker_single "./pdf_documents_demo/n_gram_language_model.pdf" \
#     --output_dir "./pdf_demorun/n_gran_language_model_new_processors/" \
#     --output_format "markdown" \
#     --page_range "0-5" \
#     --strip_existing_ocr \
#     --debug \
#     --processors "marker.processors.blockquote.BlockquoteProcessor,marker.processors.code.CodeProcessor,marker.processors.document_toc.DocumentTOCProcessor,marker.processors.equation.EquationProcessor,marker.processors.footnote.FootnoteProcessor,marker.processors.ignoretext.IgnoreTextProcessor,marker.processors.line_numbers.LineNumbersProcessor,marker.processors.list.ListProcessor,marker.processors.page_header.PageHeaderProcessor,marker.processors.sectionheader.SectionHeaderProcessor,marker.processors.text.TextProcessor,marker.processors.reference.ReferenceProcessor,marker.processors.debug.DebugProcessor" \
#     --languages "en,_math"

# marker_single "./pdf_documents_demo/JSON เบื้องต้น (Update).pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --disable_image_extraction \
#     --page_range "0-28" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00007.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --disable_image_extraction \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en" \
#     --paginate_output


# marker_single "./pdf_documents_demo/pdf_doc_00007.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00007_1_3_5" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en" \
#     --paginate_output
    
# marker_single "./pdf_documents_demo/pdf_doc_00007.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00007_1_3_5_force_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --force_ocr \
#     --languages "th,en" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00045.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en" \
#     --paginate_output \
#     --page_range "0-6" \

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --page_range "8-10" \

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_no_force_ocr" \
#     --output_format "markdown" \
#     # --force_ocr \
#     # --strip_existing_ocr c
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --page_range "8-10" \

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_llm" \
#     --output_format "markdown" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --page_range "8-9" \
#     --use_llm

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_html" \
#     --output_format "html" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --page_range "8-9" \

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_table_only" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --converter_cls "marker.converters.table.TableConverter"

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_1_3_5_force_ocr" \
#     --output_format "markdown" \
#     --force_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_1_3_5" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_1_3_5_force_ocr_llm" \
#     --output_format "markdown" \
#     --force_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --use_llm

# marker_single "./pdf_documents_demo/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง.pdf" \
#     --output_dir "./pdf_demorun/รายงานสถานการณ์การจำหน่ายไฟฟ้าและบทวิเคราะห์การไฟฟ้านครหลวง_1_3_5_llm" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --use_llm

# marker_single "./pdf_documents_demo/pdf_doc_00190.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --force_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00190.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00190_no_force_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output


# marker_single "./pdf_documents_demo/pdf_doc_00190.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00190_force_ocr" \
#     --output_format "markdown" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \


# marker_single "./pdf_documents_demo/pdf_doc_00190.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00190_force_ocr_only" \
#     --output_format "markdown" \
#     --force_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00039.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --page_range "0-20" \

# marker_single "./pdf_documents_demo/pdf_doc_00048.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00259.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \


# marker_single "./pdf_documents_demo/pdf_doc_00259.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00259_force_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --force_ocr \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00259.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00259_strip_existing_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --strip_existing_ocr \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00259.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00259_strip_existing_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --strip_existing_ocr \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00259.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00259_use_llm" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --use_llm \
#     --page_range "0-2"

# marker_single "./pdf_documents_demo/pdf_doc_00256.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --strip_existing_ocr \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00286.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00286.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00286_use_llm" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --use_llm

# marker_single "./pdf_documents_demo/pdf_doc_00286.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00286_table_only" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --force_ocr \
#     --converter_cls "marker.converters.table.TableConverter"


# marker_single "./pdf_documents_demo/pdf_doc_00007.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00007_v2" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00007.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00007_v2_force_ocr_strip_existing_ocr" \
#     --output_format "markdown" \
#     --force_ocr \
#     --strip_existing_ocr \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \

# marker_single "./pdf_documents_demo/pdf_doc_00001.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output
    
# marker_single "./pdf_documents_demo/pdf_doc_00001.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00001_force_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --force_ocr

# marker_single "./pdf_documents_demo/pdf_doc_00006.pdf" \
#     --output_dir "./pdf_demorun" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output

# marker_single "./pdf_documents_demo/pdf_doc_00006.pdf" \
#     --output_dir "./pdf_demorun/pdf_doc_00006_force_ocr" \
#     --output_format "markdown" \
#     --debug \
#     --languages "th,en,_math" \
#     --paginate_output \
#     --force_ocr