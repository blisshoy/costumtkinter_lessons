import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class SecondWindow(ctk.CTkToplevel):
    """The pop-up second window inheriting from CTkToplevel."""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Second Window")
        self.geometry("300x200")
        self.resizable(False, False)

        # Content in Second Window
        ctk.CTkLabel(
            self, text="Hello from Window #2!", font=("Helvetica", 16, "bold")
        ).pack(pady=(30, 20))

        # Close Button
        ctk.CTkButton(
            self,
            text="Close Window",
            fg_color="#D32F2F",
            hover_color="#9A0007",
            command=self.destroy,
        ).pack(pady=10)


class MainWindow(ctk.CTk):
    """The primary root window inheriting from CTk."""

    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("350x220")
        self.resizable(False, False)

        # Track the child window instance
        self.second_window = None

        # Content in Main Window
        ctk.CTkLabel(
            self, text="Main Application Window", font=("Helvetica", 18, "bold")
        ).pack(pady=(35, 20))

        # Button to trigger Second Window
        ctk.CTkButton(
            self, text="Open Second Window", command=self.open_second_window
        ).pack(pady=10)

    def open_second_window(self):
        # Open window if it doesn't exist, or bring it to focus if already open
        if self.second_window is None or not self.second_window.winfo_exists():
            self.second_window = SecondWindow(self)
        else:
            self.second_window.focus()  # Bring existing window to front


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()