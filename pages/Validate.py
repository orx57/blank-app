import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Validate - DEEP Naming Tool",
    page_icon=":material/rule:",
)

st.markdown("# Validate Demo")

st.sidebar.markdown(
    """
    ## Validate Demo

    ### Names for testing

    To copy and paste.

    - :heavy_check_mark: A2465-ocp-u-ppv-001
    - :heavy_check_mark: a0001-pvafwf001
    - :x: A0001PPXY01
    """
)

st.markdown(
    '''
    This demo illustrates a validation with the API.   
    Enjoy!
    '''
)

asset_name = st.text_input("Asset name to validate:")

if asset_name: 
    res = requests.get(url="http://localhost:8080/validate/" + asset_name)

    if res.json()['is_valid']:
        st.markdown("Asset name is :green[valid] :heavy_check_mark:")
    else:
      st.markdown("Asset name is :red[invalid] :x:")

    st.write(f"Response from API:")
    st.json(res.text)
else:
   st.markdown("Enter an asset name...")