class BlobInterface:
    def __init__(self, container_name):
        from os import getenv
        self.container_name = container_name
        self.connect_str = getenv('AZURE_STORAGE_CONNECTION_STRING')

    def blob_upload(self, full_file_path):
        try:
            from azure.storage.blob import BlobServiceClient
            blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
            from os import path
            if path.exists(full_file_path):
                upload_file_name = path.basename(full_file_path)
                blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=upload_file_name)
                with open(full_file_path, 'rb') as data:
                    blob_client.upload_blob(data)
            print(f'File {upload_file_name} uploaded successfully')
        except Exception as ex:
            print('Exception in uploading file')
            print(ex)

    def blob_download(self, download_file_name):
        try:
            from azure.storage.blob import BlobServiceClient
            blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
            blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=download_file_name)
            with open(download_file_name, 'wb') as data:
                data.write(blob_client.download_blob().readall())
            print(f'File {download_file_name} downloaded successfully')
        except Exception as ex:
            print('Exception in downloading file')
            print(ex)

    def blob_list(self):
        try:
            from azure.storage.blob import BlobServiceClient
            blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
            container_client = blob_service_client.get_container_client(self.container_name)
            blob_list = container_client.list_blobs()
            for blob in blob_list:
                print('\t' + blob.name)
        except Exception as ex:
            print('Exception occurred in listing files from blob')
            print(ex)


if __name__ == "__main__":
    # from os import path, getcwd
    new_blob_client = BlobInterface('teamrokecontainer')
    new_blob_client.blob_list()
