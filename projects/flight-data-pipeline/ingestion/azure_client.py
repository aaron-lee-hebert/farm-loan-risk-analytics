import os
from azure.storage.blob import BlobServiceClient  # type: ignore[reportMissingImports]
from config import (
    AZURE_STORAGE_ACCOUNT,
    AZURE_STORAGE_KEY,
)

class AzureClient:
    def __init__(self):
        conn_str = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={AZURE_STORAGE_ACCOUNT};"
            f"AccountKey={AZURE_STORAGE_KEY};"
            f"EndpointSuffix=core.windows.net"
        )

        self.client = BlobServiceClient.from_connection_string(conn_str)

    def upload_json(self, container, file_path, data):
        blob_client = self.client.get_blob_client(
            container=container,
            blob=file_path
        )

        blob_client.upload_blob(
            data,
            overwrite=True
        )