# Packaging Bottle Inspector

This is a quality inspection application for packaging bottles using computer vision. It captures images from multiple cameras simultaneously, analyzes them for defects (such as missing labels, wrinkles, folds, inverted bodies, etc.) using an RT-DETR model, and sends the inspection results to a control system (Athena) via OPC UA.

## Features
- Real-time video preview from 3 cameras.
- AI defect detection using the RT-DETR object detection model.
- Batch analysis (up to 24 bottles per batch).
- OPC UA Integration to send real-time inspection results and statuses to a PLC/Control system.
- Graphical User Interface (GUI) built with Tkinter.

## Requirements
- Python 3.8+ 
- Connected cameras (IDs configured in `main.py`)
- OPC UA Server accessible (default: `opc.tcp://172.16.40.150:49340`)

## Installation

1. Open your terminal and navigate to the project directory:
   ```bash
   cd package_bottle_inspector
   ```

2. (Optional but recommended) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Model Download

This project requires a specifically trained RT-DETR model to function correctly. 

You must download the model file from Hugging Face:
**[https://huggingface.co/bramiprudencio/package_bottle_inspectorq](https://huggingface.co/bramiprudencio/package_bottle_inspectorq)**

Once downloaded, ensure the file is named `rtdetr-x_4.pt` and place it directly into the root directory of this project (`package_bottle_inspector/`).

*(If the model is not found, the application will fallback to a standard `rtdetr-l.pt` model, which will not have the customized defect detection classes).*

## Desktop Shortcut (Windows & Linux)

To easily run the application directly from your Desktop without opening the terminal every time, an automated script is provided.

Run the following command once:
```bash
python create_shortcut.py
```
This will automatically generate a `PackageBottleInspector.desktop` file on Linux or a `Package Bottle Inspector.lnk` shortcut on Windows.

## Usage

1. Ensure the cameras are connected to your system.
2. If necessary, update the `OPC_URL` in `main.py` to match your local OPC UA server.
3. Run the main application via the desktop shortcut or manually via terminal:
   ```bash
   python main.py
   ```
4. The application window will open in full screen.
   - **ANALIZAR BOTELLA**: Click to capture images from the cameras and analyze the current bottle.
   - **ENVIAR A ATHENA**: Click to send the accumulated batch results to the OPC UA server and clear the local counters for the next batch.
   - The application automatically attempts to connect to the OPC UA server and the cameras upon startup.
