import streamlit as st
from PIL import Image
from helper import generate_caption
import time

st.set_page_config(
    page_title="Image Captioning Model",
    page_icon="🖼️",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle { text-align: center; color: #666; margin-bottom: 2rem; }
    .caption-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        font-size: 1.2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🖼️ Image Captioning Model</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload an image and get an AI-generated caption</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    model_choice = st.selectbox("Select Model", ["custom"])  # Single model for now
    st.subheader("Generation Parameters")
    max_length = st.slider("Max Caption Length", 10, 100, 50)
    st.divider()
    st.subheader("📖 How to Use")
    st.write("1. Upload an image\n2. Adjust parameters\n3. Click 'Generate Caption'\n4. View your caption!")

# Main area
col1, col2 = st.columns([1,1])

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png','jpg','jpeg','webp'],
        help="Supported formats: PNG, JPG, JPEG, WEBP"
    )
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.caption(f"Image size: {image.size[0]} x {image.size[1]} pixels")

with col2:
    st.subheader("✨ Generated Caption")
    if uploaded_file is not None:
        if st.button("🚀 Generate Caption"):
            with st.spinner("Generating caption..."):
                start = time.time()
                caption = generate_caption(
                    image=image,
                )
                elapsed = round(time.time() - start, 2)
                
                # Display
                st.markdown(f'<div class="caption-box">"{caption}"</div>', unsafe_allow_html=True)
                
                # Metrics
                st.divider()
                col_b, col_c = st.columns(2)
               
                with col_b: st.metric("Processing Time", f"{elapsed}s")
                with col_c: st.metric("Word Count", len(caption.split()))
                
               
    else:
        st.info("👆 Please upload an image to generate a caption")

# Footer
st.divider()
st.markdown("<div style='text-align:center;color:#666;padding:1rem;'>Built with ❤️ using Streamlit | Powered by AI</div>", unsafe_allow_html=True)
