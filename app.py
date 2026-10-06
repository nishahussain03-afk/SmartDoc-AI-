import streamlit as st
from PIL import Image

from utils.ocr import extract_text
from utils.llm import analyze_document


st.set_page_config(
    page_title="SmartDoc AI",
    page_icon="📄",
    layout="wide"
)


st.title("📄 SmartDoc AI")

st.subheader(
    "Intelligent Document Understanding using OCR + LLM"
)

st.write(
    "Upload a document and SmartDoc AI will extract, "
    "understand, and summarize its important information."
)

st.divider()


uploaded_file = st.file_uploader(
    "📤 Upload your document",
    type=[
        "png",
        "jpg",
        "jpeg"
    ]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📷 Document")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("🤖 Smart Analysis")

        analyze_button = st.button(
            "🔍 Extract & Analyze",
            type="primary"
        )


    if analyze_button:

        with st.spinner(
            "🔍 Extracting text from document..."
        ):

            try:

                extracted_text, image_type, psm, confidence = (
                    extract_text(
                        image,
                        language="eng"
                    )
                )

            except Exception as e:

                st.error(
                    f"OCR error: {e}"
                )

                st.stop()


        if not extracted_text.strip():

            st.error(
                "No readable text was detected."
            )

            st.stop()


        st.success(
            "OCR completed successfully!"
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "OCR Confidence",
                f"{confidence:.2f}%"
            )

        with col2:

            st.metric(
                "Best PSM",
                str(psm)
            )

        with col3:

            st.metric(
                "Processing",
                image_type.title()
            )


        st.divider()


        with st.expander(
            "📝 View Extracted OCR Text",
            expanded=False
        ):

            st.text_area(
                "OCR Result",
                extracted_text,
                height=300
            )


        with st.spinner(
            "🤖 AI is understanding the document..."
        ):

            try:

                analysis = analyze_document(
                    extracted_text
                )

            except Exception as e:

                st.error(
                    f"LLM error: {e}"
                )

                st.stop()


        st.success(
            "AI document analysis completed!"
        )


        st.subheader(
            "🤖 SmartDoc AI Analysis"
        )

        st.markdown(analysis)