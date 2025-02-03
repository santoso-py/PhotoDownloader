import os
import requests
import pandas as pd
from urllib.parse import urlparse
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QProgressBar, QFileDialog, QTextEdit


class DownloadThread(QThread):
    progress_signal = pyqtSignal(int)
    result_signal = pyqtSignal(str)

    def __init__(self, input_path, output_folder):
        super().__init__()
        self.input_path = input_path
        self.output_folder = output_folder

    def download_image(self, image_url, folder_path, count, total):
        try:
            response = requests.get(image_url, timeout=10)
            if response.status_code == 200:
                url_components = urlparse(image_url)
                file_name = os.path.basename(url_components.path)
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "wb") as file:
                    file.write(response.content)
                result = f"{count}/{total} - Downloaded: {file_name}"
            else:
                result = f"{count}/{total} - Failed: {image_url}"
        except Exception as e:
            result = f"{count}/{total} - Error: {str(e)}"

        return result

    def run(self):
        df = pd.read_excel(self.input_path)
        photo_paths = df['photo_path']
        total = len(photo_paths)

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for count, url in enumerate(photo_paths, start=1):
            result = self.download_image(url, self.output_folder, count, total)
            self.result_signal.emit(result)
            self.progress_signal.emit(int(count / total * 100))

        self.result_signal.emit("Image download complete!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Downloader")
        self.setGeometry(100, 100, 600, 400)

        self.input_path = ''
        self.output_folder = ''

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Excel file input
        file_layout = QHBoxLayout()
        self.input_label = QLabel("Select Excel File:")
        file_layout.addWidget(self.input_label)
        self.input_button = QPushButton("Browse")
        self.input_button.clicked.connect(self.select_input)
        file_layout.addWidget(self.input_button)
        layout.addLayout(file_layout)

        # Folder selection
        folder_layout = QHBoxLayout()
        self.folder_label = QLabel("Select Output Folder:")
        folder_layout.addWidget(self.folder_label)
        self.folder_button = QPushButton("Browse")
        self.folder_button.clicked.connect(self.select_folder)
        folder_layout.addWidget(self.folder_button)
        layout.addLayout(folder_layout)

        # Progress bar
        self.progress = QProgressBar(self)
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.progress)

        # Result log
        self.log_text = QTextEdit(self)
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

        # Start button
        self.start_button = QPushButton("Start Download")
        self.start_button.clicked.connect(self.start_download)
        layout.addWidget(self.start_button)

        # Main widget
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def select_input(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel files (*.xlsx *.csv)")
        if file_path:
            self.input_path = file_path
            self.input_label.setText(f"Selected: {os.path.basename(file_path)}")

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.output_folder = folder_path
            self.folder_label.setText(f"Selected: {os.path.basename(folder_path)}")

    def start_download(self):
        if not self.input_path or not self.output_folder:
            self.log_text.append("Please select both input file and output folder.")
            return

        self.download_thread = DownloadThread(self.input_path, self.output_folder)
        self.download_thread.progress_signal.connect(self.update_progress)
        self.download_thread.result_signal.connect(self.update_log)
        self.download_thread.start()

    def update_progress(self, progress):
        self.progress.setValue(progress)

    def update_log(self, message):
        self.log_text.append(message)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
