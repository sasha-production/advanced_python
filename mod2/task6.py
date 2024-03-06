from flask import Flask
import os
app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    try:
        abs_path = os.path.abspath(relative_path)
    except FileNotFoundError:
        return 'file not found'
    with open(relative_path, encoding='utf-8') as file:
        result_text = file.read(size)
        result_size = len(result_text)
    return f"<b>{abs_path}</b> {result_size}<br>{result_text}"


if __name__ == "__main__":
    app.run(debug=True)