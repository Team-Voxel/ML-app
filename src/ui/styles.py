

menu_style = """
            QPushButton {
                background-color: transparent;
                font-size: 13px;
                border: none;
                padding: 5px;
                border-radius: 3px;
            }



            QPushButton:hover {
                background-color: #41464a;
            }

            QPushButton::menu-indicator {
                image: none;
                width:0;
            }

            QMenu {
                background-color: #2d3136;
                color: white;
                border:none;
                border-radius: 4px;
                padding: 5px;
            }

            QMenu::item {
                padding: 5px 30px 5px 20px;
                border-radius: 3px;
            }

            QMenu::item:selected {
                background-color: #41464a;
            }

            QMenu::separator {
                height: 1px;
                background-color: #41464a;
                margin: 5px 0px;
            }
        """