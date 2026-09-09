import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class SimpleAddApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Grid Addition")
        self.geometry("260x180")
        self.resizable(False, False)

        # Row 0: Num 1 Input
        ctk.CTkLabel(self, text="Num 1:").grid(row=0, column=0, padx=10, pady=8)
        self.entry1 = ctk.CTkEntry(self, width=100)
        self.entry1.grid(row=0, column=1, padx=10, pady=8)

        # Row 1: Num 2 Input
        ctk.CTkLabel(self, text="Num 2:").grid(row=1, column=0, padx=10, pady=8)
        self.entry2 = ctk.CTkEntry(self, width=100)
        self.entry2.grid(row=1, column=1, padx=10, pady=8)

        # Row 2: Add Button (Spans 2 columns)
        ctk.CTkButton(self, text="Add", command=self.add, width=120).grid(
            row=2, column=0, columnspan=5, pady=8
        )

        # Row 3: Result Label (Spans 2 columns)
        self.result_label = ctk.CTkLabel(
            self, text="Result: ", font=("Arial", 14, "bold")
        )
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

    def add(self):
        try:
            total = float(self.entry1.get()) + float(self.entry2.get())
            formatted = int(total) if total.is_integer() else total
            self.result_label.configure(
                text=f"Result: {formatted}", text_color=("#2e7d32", "#4caf50")
            )
        except ValueError:
            self.result_label.configure(
                text="Enter valid numbers!", text_color=("#d32f2f", "#f44336")
            )


if __name__ == "__main__":
    app = SimpleAddApp()
    app.mainloop()