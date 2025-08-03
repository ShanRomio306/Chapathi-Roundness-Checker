🌀 Chapathi Roundness Checker 🎯

🔍 Basic Details

👥 Team Name:

Glitch-gurus

👨‍💻 Team Members:

Team Lead: Jishnu Vijayan — Rajiv Gandhi Institute of Technology, Kottayam

Member 2: Shan Romio — Rajiv Gandhi Institute of Technology, Kottayam

📝 Project Description:

Our project analyzes the percentage of roundness of a chapathi using image processing. The roundness is calculated using the mathematical formula:

Roundness = (4 × π × Area) / (Perimeter²)

This formula helps us identify how close the shape of a chapathi is to a perfect circle.

🛫 The Problem (that doesn’t exist):

“How to scientifically measure how round a chapathi is?” — Nobody really asked, but we answered.

💡 The Solution (that nobody asked for):

We developed a roundness detector that evaluates a chapathi's shape and calculates its roundness. If the roundness percentage is greater than 90%, the chapathi is almost perfectly round.

🧪 Technical Details

🔧 Technologies/Components Used

🖥️ For Software:

HTML, CSS, JavaScript, Python

Flask (web framework)

OpenCV (image processing)

NumPy (numerical operations)

🔌 For Hardware:

Not Applicable for this project

⚙️ Implementation

🗕 Installation

git clone https://github.com/your-repo/chapatti-roundness-detector.git
cd chapatti-roundness-detector
pip install -r requirements.txt

▶️ Run

python app.py

📘️ Project Documentation

🖼️ Screenshots (At least 3)

Screenshot 1

![Screenshot1](https://drive.google.com/file/d/1OJhZqqmSuS3M7NkTeG6DB0oADhQXNapV/view?usp=drive_link)
Home Page: This shows the user interface with the upload option to select an image.

Screenshot 2

![Screenshot2](https://drive.google.com/file/d/1c-uoCGj3eFLbS-_IRql75OjLvAjkKTMM/view?usp=drive_link)
Result Page: Displays roundness percentage and motivational message after processing.

Screenshot 3

![Screenshot3](https://drive.google.com/file/d/1E8Q9YWNr5E1LYT3kgFMFdPHjKELvCcnE/view?usp=drive_link)
Error Case: Displays an error when a non-circular image is uploaded (e.g., not a chapathi).

📊 Diagrams

🧠 Workflow Diagram

![Workflow]()
Workflow Diagram: Shows how the image flows from user upload → backend processing → result response.

[User Uploads Image]
        ↓
[Flask Server Receives]
        ↓
[OpenCV Detects Circle]
        ↓
[Roundness Calculated]
        ↓
[JSON Response to Frontend]
        ↓
[Frontend Displays Result]

🔌 For Hardware (if any)

Not applicable for this software-only project.

🎥 Project Demo

📹 Video

[]
A short video showing how the user uploads the image, and how the result is displayed.

🎞️ Additional Demos

[]

🤝 Team Contributions

Jishnu Vijayan: Frontend UI design, HTML/CSS/JS

Shan Romio: Backend processing logic (Flask + OpenCV)

Made with ❤️ at TinkerHub Useless Projects

