from sqlpyhelper.db_helper import SQLPyHelper
import json

db = SQLPyHelper()


def log_to_postgres(features, result):
    try:
        query = """
            INSERT INTO predictions (features, fraud_probability, prediction, label)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            json.dumps(features),
            result["fraud_probability"],
            result["prediction"],
            result["label"]
        )
        db.execute_query(query, params)
    except Exception as e:
        print(f"[Logging Error] {e}")
