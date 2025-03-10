import sys
import pandas as pd
import re
import numpy as np
from src.ui.plotter import KDEPlotWidget

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem, QLabel, QComboBox, QGridLayout, QHBoxLayout, QFrame
)
from numpy.ma.core import left_shift

import styles as style
import src.modules.file_system as fs

class CSVViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.file_path = None
        self.col_name = ""
        self.df = None
        self.kde_plot = KDEPlotWidget()

        self.setWindowTitle("CSV Viewer")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet(style.menu_style)
        # Layout
        self.main_layout = QHBoxLayout()
        self.left_panel = QVBoxLayout()
        self.layout = QGridLayout()

        # Button to load CSV
        self.load_button = QPushButton("Open CSV File")
        self.load_button.clicked.connect(self.load_csv)
        self.left_panel.addWidget(self.load_button)

        # Table Widget to display CSV
        self.table = QTableWidget()
        self.left_panel.addWidget(self.table)

        self.left_frame = QFrame()
        self.left_frame.setLayout(self.left_panel)
        self.left_frame.setFrameShape(QFrame.StyledPanel)

        self.right_panel = QVBoxLayout()

        # Dropdown to select columns
        self.column_selector = QComboBox()
        self.column_selector.currentIndexChanged.connect(self.update_statistics)
        self.right_panel.addWidget(self.column_selector)

        # Label for statistics
        self.stats_label = QLabel("Statistics will appear here")
        self.right_panel.addWidget(self.stats_label)

        self.right_panel.addWidget(self.kde_plot)
        self.kde_plot.hide()

        self.convert_to_num_btn = QPushButton("Convert To Numeric")
        self.convert_to_num_btn.clicked.connect(self.convert_column)
        self.convert_to_num_btn.hide()
        self.right_panel.addWidget(self.convert_to_num_btn)

        self.right_frame = QFrame()
        self.right_frame.setLayout(self.right_panel)
        self.right_frame.setFrameShape(QFrame.StyledPanel)

        self.main_layout.addWidget(self.left_frame, 2)
        self.main_layout.addWidget(self.right_frame, 1)

        self.setLayout(self.main_layout)

    def load_csv(self):
        self.file_path = fs.open_file_browser(self, "C:\\Windows\\Users\\Tharuka\\Downloads", "CSV Files (*.csv)")
        if self.file_path:
            self.display_csv(self.file_path)

    def display_csv(self, file_path):
        self.df = pd.read_csv(file_path)
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)

        # Update column selector
        self.column_selector.clear()
        self.column_selector.addItems(self.df.columns)

        self.update_table()

    def update_table(self):
        for row in range(len(self.df)):
            for col in range(len(self.df.columns)):
                item = QTableWidgetItem(str(self.df.iat[row, col]))
                self.table.setItem(row, col, item)

        # Update statistics for the first column
        self.update_statistics()

    def update_statistics(self):

        self.col_name = self.column_selector.currentText()
        if self.col_name:

            col_type = 'nnum'
            # 1 try to convert to numeric
            try:
                mod_df = pd.to_numeric(self.df[self.col_name], errors='raise')
            except:
                col_type = 'fnum'
            else:
                col_type = 'pnum'

            missing_count = 0

            # if the col is not purely numeric check if it has any formattings
            if col_type != 'pnum':
                mod_df = self.df[self.col_name].apply(self.clean_numeric)
                mod_df = pd.to_numeric(mod_df, errors='coerce')
                if self.is_majority_numeric(mod_df):
                    col_type = 'fnum'
                else:
                    col_type = 'nnum'
                    missing_count = self.count_missing_values(mod_df)
            else:
                missing_count = self.count_missing_values(mod_df)

            dataRow1 = ""
            if col_type == "pnum":
                dataRow1 = f"Type: Numerical\nNo of Missing/Null Values: {missing_count}\n\n" + self.update_stats_table()
                self.convert_to_num_btn.hide()
                self.kde_plot.plot_kde(self.df, self.col_name)
                self.kde_plot.show()
            elif col_type == "fnum":
                dataRow1 = f"Type: Seems like numerical data\nCount: {self.df[self.col_name].count()}\nUnique: {self.df[self.col_name].nunique()}"
                self.convert_to_num_btn.show()
                self.kde_plot.hide()
            else:
                dataRow1 = f"Type: Non numeric\nNo of Missing/Null Values: {missing_count}\nCount: {self.df[self.col_name].count()}\nUnique: {self.df[self.col_name].nunique()}"
                self.convert_to_num_btn.hide()
                self.kde_plot.hide()

            self.stats_label.setText(dataRow1)

    def clean_numeric(self, val):
        # Remove any character that's not a digit or a dot.
        cleaned = re.sub(r'[^\d.]', '', val)
        if cleaned:
            return float(cleaned)
        else:
            return ''

    def is_majority_numeric(self, series):
        """
        Checks if the majority of values in a Pandas Series are numeric or NaN/empty strings.

        Args:
            series (pd.Series): The input column (Series) to check.

        Returns:
            bool: True if the majority of values are numeric, otherwise False.
        """
        # Count total values excluding NaN
        total_values = len(series)

        # Count numeric values
        numeric_count = series.apply(lambda x: isinstance(x, (int, float)) and not np.isnan(x)).sum()

        # Count empty strings or NaN
        empty_or_nan_count = series.isna().sum() + (series == "").sum()

        # Check if numeric values form the majority
        return numeric_count > empty_or_nan_count

    def count_missing_values(self, series):
        return series.isna().sum() + (series == "").sum()

    def convert_column(self):
        self.df[self.col_name] = pd.to_numeric(self.df[self.col_name].apply(self.clean_numeric), errors='coerce')
        self.update_table()

    def update_stats_table(self):
        col = self.df[self.col_name]
        count = col.count()
        min = col.min()
        max = col.max()
        mean = col.mean()
        var = col.var()
        return f"Count: {count}\nMin: {min}\nMax: {max}\nMean: {mean:.2f}\nVariance: {var:.2f}"