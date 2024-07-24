import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Validate - DEEP Naming Tool",
    page_icon="👋",
)

st.markdown("# Validate Demo")
st.sidebar.header("Validate Demo")

st.write(
    """
    This demo illustrates a validation with FastAPI.  
    Enjoy!
    """
)

option = st.selectbox(
    "Select a name to validate:",
    ("A0001-net-p-Zerto-vRA-1234", "A0001-net-p-Zerto-vRA-2171", "A0001-net-p-Zerto-ZCC-2789", "A0001-net-u-MngWL1-WL1VMs-2789", "a0001-pvafwf001", "a0001-pvavmw001", "a0001-pvlipa001", "A0001-vmwdc-u-v01-m01-rcs-01", "A0001PPXY01", "A0001PVDB01", "A0001PVDF01", "A0001PVDX01", "A2222-vmwnp-u-v01-m01-np01", "A2465-ocp-u-ppv-001"),
    index=None,
    placeholder="Select name..."
)

st.write("You selected:", option)

if st.button("Validate"):
    res = requests.get(url="http://localhost:8080/validate/" + option)

    st.write(f"Response from API:")
    st.json(res.text)
