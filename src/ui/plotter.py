import pandas as pd
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class KDEPlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create layout and add the canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_kde(self, df, column_name):
        self.ax.clear()
        df[column_name].plot(kind="kde", ax=self.ax, title=f"KDE of '{column_name}'")
        self.canvas.draw()