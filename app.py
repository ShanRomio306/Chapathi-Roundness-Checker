from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from roundness import calculate_roundness, is_likely_chapati

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    roundness = None
    warning = None
    image_name = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            image_name = filename

            if not is_likely_chapati(filepath):
                warning = "This doesn't look like a chapati. Please upload a valid chapati image."
            else:
                roundness = calculate_roundness(filepath)

    return render_template("index.html", result=roundness, warning=warning, image_name=image_name)

if __name__ == "__main__":
    app.run(debug=True)
