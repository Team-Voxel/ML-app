from ui.main_window import MainWindow


class Application:
    def __init__(self):
        # Initialize the main window and other necessary components
        self.window = MainWindow()

    def run(self):
        # Start the main application loop
        self.window.mainloop()
