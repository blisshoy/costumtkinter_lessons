import customtkinter as ctk

ctk.set_appearance_mode("System")


class ColorfulAddApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Colorful Addition")
        self.geometry("300x260")
        self.resizable(False, False)

        # Window background color (Light Mode, Dark Mode)
        self.configure(fg_color=("#EAEAEA", "#181825"))

        # Card Frame with custom background and border colors
        self.card = ctk.CTkFrame(
            self,
            fg_color=("#FFFFFF", "#2B2D42"),
            border_color=("#CBD5E1", "#415A77"),
            border_width=2,
            corner_radius=12,
        )
        self.card.pack(padx=15, pady=15, fill="both", expand=True)

        # Title Label
        ctk.CTkLabel(
            self.card,
            text="Addition Calculator",
            font=("Helvetica", 16, "bold"),
            text_color=("#1E293B", "#EDF2F4"),
        ).grid(row=0, column=0, columnspan=2, pady=(15, 10))

        # Row 1: Num 1
        ctk.CTkLabel(
            self.card,
            text="Num 1:",
            font=("Helvetica", 12, "bold"),
            text_color=("#64748B", "#8D99AE"),
        ).grid(row=1, column=0, padx=(15, 5), pady=5, sticky="e")

        self.entry1 = ctk.CTkEntry(
            self.card,
            width=100,
            fg_color=("#F1F5F9", "#1E1E2E"),
            border_color=("#94A3B8", "#45475A"),
            text_color=("#0F172A", "#F8F8F2"),
        )
        self.entry1.grid(row=1, column=1, padx=(5, 15), pady=5, sticky="w")

        # Row 2: Num 2
        ctk.CTkLabel(
            self.card,
            text="Num 2:",
            font=("Helvetica", 12, "bold"),
            text_color=("#64748B", "#8D99AE"),
        ).grid(row=2, column=0, padx=(15, 5), pady=5, sticky="e")

        self.entry2 = ctk.CTkEntry(
            self.card,
            width=100,
            fg_color=("#F1F5F9", "#1E1E2E"),
            border_color=("#94A3B8", "#45475A"),
            text_color=("#0F172A", "#F8F8F2"),
        )
        self.entry2.grid(row=2, column=1, padx=(5, 15), pady=5, sticky="w")

        # Row 3: Vibrant Purple Button
        self.add_btn = ctk.CTkButton(
            self.card,
            text="Calculate",
            font=("Helvetica", 12, "bold"),
            fg_color="#7209B7",  # Normal button color
            hover_color="#560BAD",  # Color on hover
            text_color="#FFFFFF",
            width=150,
            command=self.add,
        )
        self.add_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Row 4: Result Box
        self.result_label = ctk.CTkLabel(
            self.card,
            text="Result: --",
            font=("Helvetica", 14, "bold"),
            text_color=("#4338CA", "#4CC9F0"),
        )
        self.result_label.grid(row=4, column=0, columnspan=2, pady=(0, 10))

    def add(self):
        try:
            total = float(self.entry1.get()) + float(self.entry2.get())
            formatted = int(total) if total.is_integer() else total
            # Green for success
            self.result_label.configure(
                text=f"Result: {formatted}",
                text_color=("#15803D", "#4EDA87"),
            )
        except ValueError:
            # Pink/Red for error
            self.result_label.configure(
                text="Enter valid numbers!", text_color=("#B91C1C", "#F72585")
            )


if __name__ == "__main__":
    app = ColorfulAddApp()
    app.mainloop()