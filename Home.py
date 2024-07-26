import socket
import subprocess
import sys
import streamlit as st

def check_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def start_uvicorn_server():
    if not check_port_in_use(8080):
        subprocess.run([f"{sys.executable}", "-m", "uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--reload"])

st.set_page_config(
    page_title="Home - DEEP Naming Tool",
    page_icon=":material/dns:",
)

st.write("# DEEP Naming Tool")
st.sidebar.success("Select a demo above.")
st.markdown("**👈 Select a demo from the sidebar** to see some examples!")

start_uvicorn_server()
