from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QTextCursor, QKeyEvent
import subprocess
import os

class terminal_widget(QWidget):
    """
    A widget that simulates a terminal like CMD or PowerShell
    """
    commandExecuted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.command_history = []
        self.history_index = -1
        self.current_directory = os.getcwd()
        self.setup_ui()
        self.current_command = ""
        self.prompt_position = 0

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Single TextEdit for both input and output
        self.terminal = QTextEdit()
        self.terminal.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                font-family: Consolas, Monaco, monospace;
                border: none;
                padding: 5px;
            }
        """)
        layout.addWidget(self.terminal)

        # Connect key press event
        self.terminal.keyPressEvent = self.handle_key_press
        
        # Show initial prompt
        self.show_prompt()

    def show_prompt(self):
        self.terminal.append(f"{self.current_directory}> ")
        cursor = self.terminal.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.terminal.setTextCursor(cursor)
        self.prompt_position = self.terminal.textCursor().position()

    def handle_key_press(self, event: QKeyEvent):
        cursor = self.terminal.textCursor()
        
        # Only allow editing after the prompt
        if cursor.position() < self.prompt_position and event.key() not in [Qt.Key.Key_Left, Qt.Key.Key_Right, Qt.Key.Key_Up, Qt.Key.Key_Down]:
            cursor.movePosition(QTextCursor.End)
            self.terminal.setTextCursor(cursor)
            
        if event.key() == Qt.Key.Key_Return:
            self.handle_return()
        elif event.key() == Qt.Key.Key_Up:
            self.handle_up_key()
        elif event.key() == Qt.Key.Key_Down:
            self.handle_down_key()
        elif event.key() == Qt.Key.Key_Backspace:
            if cursor.position() > self.prompt_position:
                QTextEdit.keyPressEvent(self.terminal, event)
        else:
            QTextEdit.keyPressEvent(self.terminal, event)

    def handle_return(self):
        cursor = self.terminal.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.terminal.setTextCursor(cursor)
        
        # Get the current line
        cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
        current_line = cursor.selectedText()
        
        # Extract command (remove prompt)
        prompt_text = f"{self.current_directory}> "
        if current_line.startswith(prompt_text):
            command = current_line[len(prompt_text):].strip()
        else:
            command = current_line.strip()

        # Add command to history if not empty
        if command:
            self.command_history.append(command)
            self.history_index = len(self.command_history)

        self.terminal.append("")  # New line

        if command:
            try:
                # Handle cd command specially
                if command.startswith('cd '):
                    new_dir = command[3:].strip()
                    try:
                        os.chdir(os.path.expanduser(new_dir))
                        self.current_directory = os.getcwd()
                    except Exception as e:
                        self.terminal.append(f"cd: {str(e)}")
                else:
                    # Execute command
                    process = subprocess.Popen(
                        command,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=self.current_directory
                    )
                    stdout, stderr = process.communicate()

                    # Display output
                    if stdout:
                        self.terminal.append(stdout.rstrip())
                    if stderr:
                        self.terminal.append(stderr.rstrip())

            except Exception as e:
                self.terminal.append(f"Error: {str(e)}")

            self.commandExecuted.emit(command)

        self.show_prompt()

    def handle_up_key(self):
        if self.command_history and self.history_index > 0:
            self.history_index -= 1
            self.set_command(self.command_history[self.history_index])

    def handle_down_key(self):
        if self.history_index < len(self.command_history) - 1:
            self.history_index += 1
            self.set_command(self.command_history[self.history_index])
        else:
            self.history_index = len(self.command_history)
            self.set_command("")

    def set_command(self, command):
        cursor = self.terminal.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
        cursor.removeSelectedText()
        cursor.insertText(f"{self.current_directory}> {command}")

# # Example usage
# if __name__ == '__main__':
#     from PySide6.QtWidgets import QApplication
#     import sys

#     app = QApplication(sys.argv)
#     terminal = terminal_widget()
#     terminal.resize(800, 600)
#     terminal.show()
#     sys.exit(app.exec())