import streamlit as st
import qrcode
from io import BytesIO

st.title("Mohitosh QR Code Generator")

# Input for link
data = st.text_input("Put the link to generate QR Code:")

# Input for file name
name = st.text_input("Enter the QR Code Name:")

if st.button("Generate QR Code"):
    if data and name:
        # Generate QR
        img = qrcode.make(data)

        # Save to memory
        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        # Show image
        st.image(buf, caption="Generated QR Code", use_column_width=True)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name=f"{name}.png",
            mime="image/png"
        )

        st.success("QR Code created successfully!")
    else:
        st.warning("Please enter both link and file name.")
