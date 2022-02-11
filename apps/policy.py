import os
import geopandas as gpd
import streamlit as st

def save_uploaded_file(file_content, file_name):
    """
    Save the uploaded file to a temporary directory
    """
    import tempfile
    import os
    import uuid

    _, file_extension = os.path.splitext(file_name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(file_content.getbuffer())

    return file_path
#%%
# define containers:
container_1 = st.empty() 
with container_1.container():
    st.write('## Select a NDC to comparre to')
    options = st.multiselect('Select categories from the taxonomy:', ['South Africa','Ethiopia']
                                            , format_func=lambda x: 'Select a category' if x == '' else x)