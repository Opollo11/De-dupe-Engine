from flask import Flask, request, Response, send_from_directory
from flask_cors import CORS, cross_origin
import pandas as pd
from .helper import make_summary
import os
from datetime import datetime


# from openpyxl import load_workbook
app = Flask(__name__)
CORS(app, support_credentials=True)

uploads_dir = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/', methods=["POST"])
@cross_origin(supports_credentials=True)
def get_summary():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_csv(f)
        # f.save(os.path.join(uploads_dir, f.filename))
        summary_df = make_summary(df)
        now = datetime.now()
        summary_file_name = f"summary-{now}.xlsx"
        SUMMARY_DIR = "summary_excel_files"
        summary_file_path = os.path.join(
            os.getcwd(), SUMMARY_DIR, summary_file_name)
        summary_df.to_excel(summary_file_path)

        return send_from_directory(SUMMARY_DIR, summary_file_name, as_attachment=True)
        # return summary


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
