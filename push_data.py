import os
import sys
import json

import pandas as pd
import pymongo
import certifi

from dotenv import load_dotenv
load_dotenv()

# ================================
# Custom Exception
# ================================
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.line_no = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self):
        return (
            f"Error occured in python script name [{self.file_name}] "
            f"line number [{self.line_no}] error message [{self.error_message}]"
        )


# ================================
# Data Extraction Class
# ================================
class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_db_url = os.getenv("MONGO_DB_URL")
            if self.mongo_db_url is None:
                raise Exception("MONGO_DB_URL is not set in environment variables")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)

            # Convert dataframe to list of dictionaries
            records = json.loads(df.to_json(orient="records"))
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database_name, collection_name):
        try:
            client = pymongo.MongoClient(
                self.mongo_db_url,
                tls=True,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=30000
            )

            database = client[database_name]
            collection = database[collection_name]

            result = collection.insert_many(records)
            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


# ================================
# Main Execution
# ================================
if __name__ == "__main__":
    try:
        FILE_PATH = r"Network_Data\phisingData.csv"
        DATABASE_NAME = "aviral0012"
        COLLECTION_NAME = "NetworkData"

        network_obj = NetworkDataExtract()

        records = network_obj.csv_to_json_convertor(FILE_PATH)
        print(f"Total records read from CSV: {len(records)}")

        no_of_records = network_obj.insert_data_mongodb(
            records,
            DATABASE_NAME,
            COLLECTION_NAME
        )

        print(f"Successfully inserted {no_of_records} records into MongoDB")

    except Exception as e:
        print(e)
