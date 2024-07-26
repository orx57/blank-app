import streamlit as st
import subprocess
import sys

subprocess.run([f"{sys.executable}", "-m", "uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--reload"])

st.set_page_config(
    page_title="Home - DEEP Naming Tool",
    page_icon=":material/dns:",
)

st.write("# DEEP Naming Tool")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    **👈 Select a demo from the sidebar** to see some examples!
    """
)
