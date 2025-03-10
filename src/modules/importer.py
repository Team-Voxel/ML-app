import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem, QLabel, QComboBox
)

class CSVViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Viewer")
        self.setGeometry(200, 200, 800, 600)

        # Layout
        self.layout = QVBoxLayout()

        # Button to load CSV
        self.load_button = QPushButton("Open CSV File")
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        # Table Widget to display CSV
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Dropdown to select columns
        self.column_selector = QComboBox()
        self.column_selector.currentIndexChanged.connect(self.update_statistics)
        self.layout.addWidget(self.column_selector)

        # Label for statistics
        self.stats_label = QLabel("Statistics will appear here")
        self.layout.addWidget(self.stats_label)

        self.setLayout(self.layout)

    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.display_csv(file_path)

    def display_csv(self, file_path):
        self.df = pd.read_csv(file_path)  # Read CSV into Pandas DataFrame
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)

        # Populate table
        for row in range(len(self.df)):
            for col in range(len(self.df.columns)):
                item = QTableWidgetItem(str(self.df.iat[row, col]))
                self.table.setItem(row, col, item)

        # Update column selector
        self.column_selector.clear()
        self.column_selector.addItems(self.df.columns)

        # Update statistics for the first column
        self.update_statistics()

    def update_statistics(self):
        col_name = self.column_selector.currentText()
        if col_name:
            col_data = pd.to_numeric(self.df[col_name], errors='coerce').dropna()
            if not col_data.empty:
                stats = f"Mean: {col_data.mean():.2f}, Min: {col_data.min()}, Max: {col_data.max()}"
            else:
                stats = "Selected column is non-numeric."
            self.stats_label.setText(stats)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CSVViewer()
    viewer.show()
    sys.exit(app.exec())
