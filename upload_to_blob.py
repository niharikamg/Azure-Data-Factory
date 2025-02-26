from azure.storage.blob import BlobServiceClient

# Azure Storage account details
storage_account_name = "your_storage_account"
storage_account_key = "your_storage_key"
container_name = "student-container"
file_path = "path/to/student.csv"
blob_name = "student.csv"

# Create a blob service client
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_key)

# Upload the file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Uploaded {blob_name} to Azure Blob Storage.")
