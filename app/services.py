import pandas as pd
from io import BytesIO

class DataProcessorService:
    @staticmethod
    def process_and_clean_csv(file_bytes: bytes) -> dict:
        # Uploaded file bytes ko Pandas DataFrame mein read karein
        df = pd.read_csv(BytesIO(file_bytes))

        # 1. Data Cleaning: Duplicate rows hatao aur Null values handle karo
        df.drop_duplicates(inplace=True)
        df.fillna({
            'status': 'UNKNOWN',
            'amount': 0.0
        }, inplace=True)

        # 2. Data Transformation: Ensure correct data types
        if 'amount' in df.columns:
            df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0.0)

        # 3. Analytics Aggregation: Summary metrics generate karo
        summary = {
            "total_records": len(df),
            "total_amount": float(df['amount'].sum()) if 'amount' in df.columns else 0.0,
            "average_amount": float(df['amount'].mean()) if 'amount' in df.columns else 0.0,
        }

        # Cleaned DataFrame ko SQL Insertion ke liye list of dicts mein convert karein
        cleaned_records = df.to_dict(orient="records")

        return {
            "summary": summary,
            "records": cleaned_records
        }
