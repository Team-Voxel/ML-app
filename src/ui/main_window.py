

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtCore import Qt, QPoint
from src.ui.UI_form import Ui_MainWindow
import src.modules.file_system as fs
import src.ui.styles as styles
from src.ui.csv_viewer import CSVViewer
from PySide6.QtGui import QAction  # QAction is in QtGui

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.viewer = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Window setup
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Button setup
        self.ui.maximize_btn.setCheckable(True)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.maximize_btn.clicked.connect(self.toggle_maximize_restore)
        self.ui.close_btn.clicked.connect(self.close)

        # Window drag state
        self.drag_start_position = None
        self.window_start_position = None
        self.is_dragging = False
        self.was_maximized = False

        # Connect mouse events to title bar
        self.ui.title_frame.mousePressEvent = self.titlebar_mouse_press
        self.ui.title_frame.mouseMoveEvent = self.titlebar_mouse_move
        self.ui.title_frame.mouseReleaseEvent = self.titlebar_mouse_release
        self.ui.title_frame.mouseDoubleClickEvent = self.titlebar_double_click

        # Create the File menu
        file_menu = QMenu(self)

        # Apply the styles
        self.ui.file_menu_btn.setStyleSheet(styles.menu_style)
        file_menu.setStyleSheet(styles.menu_style)
        
        # Create actions
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        save_as_action = QAction("Save As...", self)
        exit_action = QAction("Exit", self)
        
        # Add actions to the menu
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        # Set the menu for the file Button
        self.ui.file_menu_btn.setMenu(file_menu)
        
        # Connect actions to slots
        new_action.triggered.connect(self.new_file)
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        save_as_action.triggered.connect(self.save_as_file)
        exit_action.triggered.connect(self.close)

    # Add these methods to your MainWindow class:
    def new_file(self):
        # Open a new project
        pass

    def open_file(self):
        # Open a new file or project
        self.viewer = CSVViewer()
        self.viewer.show()

    def save_file(self):
        # Save current file
        pass

    def save_as_file(self):
        # Implement save as functionality
        pass

    def toggle_maximize_restore(self):
        """Toggle between maximized and normal window state"""
        if self.isMaximized():
            self.showNormal()
            self.ui.maximize_btn.setChecked(False)
        else:
            self.showMaximized()
            self.ui.maximize_btn.setChecked(True)

    def titlebar_mouse_press(self, event):
        """Handle mouse press events on the title bar"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            self.drag_start_position = event.globalPosition().toPoint()
            self.window_start_position = self.pos()
            self.was_maximized = self.isMaximized()
            
            if self.was_maximized:
                # Calculate the relative click position as a fraction of the window width
                click_x = event.position().x()
                window_width = self.ui.title_frame.width()
                self.relative_click_x = click_x / window_width

    def titlebar_mouse_move(self, event):
        """Handle mouse move events on the title bar"""
        if not self.is_dragging:
            return

        if self.was_maximized:
            # Restore window when starting to drag from maximized state
            self.showNormal()
            self.ui.maximize_btn.setChecked(False)
            
            # Adjust window position to maintain mouse under cursor
            cursor_pos = event.globalPosition().toPoint()
            new_width = self.width()
            new_x = cursor_pos.x() - (new_width * self.relative_click_x)
            new_y = cursor_pos.y()
            self.move(int(new_x), new_y)
            
            # Reset drag start position for smooth transition
            self.drag_start_position = cursor_pos
            self.window_start_position = self.pos()
            self.was_maximized = False
        else:
            # Normal window dragging
            new_pos = self.window_start_position + (event.globalPosition().toPoint() - self.drag_start_position)
            self.move(new_pos)

    def titlebar_mouse_release(self, event):
        """Handle mouse release events on the title bar"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            
            # Check if window should snap to maximized state
            if self.pos().y() < 10:  # Threshold for maximizing when dragged to top
                self.showMaximized()
                self.ui.maximize_btn.setChecked(True)

    def titlebar_double_click(self, event):
        """Handle double click events on the title bar"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle_maximize_restore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())