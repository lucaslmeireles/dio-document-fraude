import os
from azure.storage.blob import BlobServiceClient
import streamlit as st

def upload_image_to_blob(file, file_name):
    try:
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        blob_client.upload_blob(file, overwrite=True)

        blob_url = blob_client.url
        return blob_url
    except Exception as e:
        st.error(f"Erro ao enviar a imagem para o Azure Blob Storage: {e}")
        return None
