# Azure Data Pipeline Project

## Project Overview
This project involves building an end-to-end data pipeline using **Azure Data Factory** to extract, transform, and load (ETL) data from a CSV file stored in **Azure Blob Storage** into **Azure SQL Database**.

## Technologies Used
- **Azure Storage Account** (for storing student.csv)
- **Azure SQL Database** (for structured data storage)
- **Azure Data Factory** (for data pipeline and ETL operations)
- **Python** (for uploading CSV data to Azure Blob Storage)
- **SQL** (for table creation and data validation)

## Setup Instructions
### Step 1: Create Azure Storage and Upload CSV File
1. Log in to **Azure Portal**.
2. Create a **Storage Account**.
3. Create a **Blob Container**.
4. Upload `student.csv` to the Blob Container.

### Step 2: Set Up Azure SQL Database
1. Create an **Azure SQL Server**.
2. Create an **Azure SQL Database**.
3. Configure firewall rules to allow connections.
4. Run the following SQL script to create the `Students` table:

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT,
    Country NVARCHAR(50),
    GPA FLOAT
);
```

### Step 3: Upload CSV to Azure Blob Storage
Use the provided **Python script** to upload `student.csv` to Azure Blob Storage.

```python
from azure.storage.blob import BlobServiceClient

# Azure Storage account details
storage_account_name = "your_storage_account"
storage_account_key = "your_storage_key"
container_name = "student-container"
file_path = "path/to/student.csv"
blob_name = "student.csv"

# Upload file
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_key)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Uploaded {blob_name} to Azure Blob Storage.")
```

### Step 4: Configure Azure Data Factory Pipeline
1. Create an **Azure Data Factory Instance**.
2. Set up **Linked Services** for Azure Blob Storage and Azure SQL Database.
3. Create **Datasets** for the CSV file and the SQL table.
4. Use **Copy Data Activity** to transfer data.
5. Deploy the following JSON pipeline configuration:

```json
{
    "name": "CopyStudentData",
    "properties": {
        "activities": [
            {
                "name": "CopyData",
                "type": "Copy",
                "inputs": [
                    {
                        "referenceName": "BlobStudentDataset",
                        "type": "DatasetReference"
                    }
                ],
                "outputs": [
                    {
                        "referenceName": "SQLStudentDataset",
                        "type": "DatasetReference"
                    }
                ],
                "typeProperties": {
                    "source": {
                        "type": "DelimitedTextSource",
                        "formatSettings": {
                            "type": "TextFormat",
                            "columnDelimiter": ",",
                            "rowDelimiter": "\n"
                        }
                    },
                    "sink": {
                        "type": "AzureSqlSink"
                    }
                }
            }
        ]
    }
}
```

### Step 5: Verify Data Transfer
1. Run the **Data Pipeline**.
2. Query the **Azure SQL Database** to check if the data is successfully transferred.
3. Run the following query to count students by country:

```sql
SELECT Country, COUNT(*) AS StudentCount FROM Students GROUP BY Country;
```

### Step 6 (Optional): Deploy a Static Web App for Extra Credit
- Set up an **Azure Static Web App**.
- Deploy an **Azure Function App** to fetch student counts.
- Ensure that the web app correctly displays the student count by country.

## Estimated Cost Breakdown
| Service | Estimated Monthly Cost |
|---------|----------------------|
| Azure Storage | $5 - $10 |
| Azure SQL Database | $10 - $20 |
| Azure Data Factory | $15 - $30 |
| Total | $30 - $60 |

> Costs may vary based on usage and selected pricing tiers.

## Conclusion
This project provides hands-on experience in building an ETL pipeline in Azure. It involves cloud storage, database management, and automated data processing using **Azure Data Factory**.

🚀 Happy Learning!

