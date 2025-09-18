from azure.storage.blob import BlobServiceClient

# connection string
#connection_string = ""
container_name = "datasets"  # name of the container created in storage accounts
local_file_path = "Motor_Vehicle_Collisions_-_Crashes.csv"  # local file path that needs to be uploaded
blob_name = "Motor_Vehicle_Collisions_-_Crashes.csv"  # name it will have in Blob Storage

# Connect to the Blob service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload the file
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Uploaded '{local_file_path}' to container '{container_name}' as '{blob_name}'")
