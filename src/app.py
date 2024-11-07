import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
from pdf_utils import parse_pdf


if "pdf_doc" not in ss:
    ss.pdf_doc = None

def main():
    # set header for app
    st.header("Research Tutor")

    # create sidebar
    with st.sidebar:
        uploaded_doc = st.file_uploader(label="Upload File: ", type=("pdf"))
        if uploaded_doc:
            ss.pdf_doc = uploaded_doc


    # if pdf doc exist, show the pdf view
    if ss.pdf_doc is not None:
        binary_data = ss.pdf_doc.getvalue()
        pdf_viewer(input=binary_data, width=700)

        # start processing data from pdf to text chunk
        parse_pdf(ss.pdf_doc, n_pages=6)


if __name__ == "__main__":
    main()
