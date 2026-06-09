import streamlit as st
from PIL import Image
import io

st.set_page_config(
    page_title="Image DPI & Resolution Tool",
    layout="wide"
)

st.title("🖼️ Image DPI & Resolution Tool")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg", "tif", "tiff"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Original Image")

    width, height = image.size

    st.subheader("Original Properties")
    st.write(f"Width: {width}px")
    st.write(f"Height: {height}px")

    col1, col2 = st.columns(2)

    with col1:
        scale_percent = st.slider(
            "Resize (%)",
            min_value=10,
            max_value=500,
            value=100
        )

    with col2:
        dpi_value = st.number_input(
            "DPI",
            min_value=1,
            max_value=1200,
            value=300
        )

    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)

    resized = image.resize(
        (new_width, new_height),
        Image.LANCZOS
    )

    st.subheader("Preview")
    st.image(resized)

    format_choice = st.selectbox(
        "Output Format",
        ["PNG", "JPEG", "TIFF"]
    )

    buffer = io.BytesIO()

    if format_choice == "JPEG":
        resized = resized.convert("RGB")

    resized.save(
        buffer,
        format=format_choice,
        dpi=(dpi_value, dpi_value)
    )

    st.download_button(
        label="⬇ Download",
        data=buffer.getvalue(),
        file_name=f"converted.{format_choice.lower()}",
        mime=f"image/{format_choice.lower()}"
    )
