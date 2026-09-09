import sqlite3
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class NotesApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("SQLite Notes App")
        self.geometry("700x450")

        # Initialize SQLite Database
        self.init_db()

        # Build UI Layout
        self.create_widgets()

        # Load Existing Notes
        self.load_notes()

    def init_db(self):
        """Creates SQLite database connection and the notes table if it doesn't exist."""
        self.conn = sqlite3.connect("notes.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def create_widgets(self):
        # 2-Column Grid Layout: Column 0 = Input Form, Column 1 = Scrollable Notes Display
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Left Side: Input Form Frame
        self.input_frame = ctk.CTkFrame(self, corner_radius=10)
        self.input_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        ctk.CTkLabel(
            self.input_frame, text="New Note", font=("Helvetica", 16, "bold")
        ).pack(pady=(15, 10))

        self.title_entry = ctk.CTkEntry(
            self.input_frame, placeholder_text="Note Title"
        )
        self.title_entry.pack(padx=10, pady=5, fill="x")

        self.content_text = ctk.CTkTextbox(self.input_frame, height=140)
        self.content_text.pack(padx=10, pady=5, fill="x")

        self.save_btn = ctk.CTkButton(
            self.input_frame,
            text="Save Note",
            command=self.add_note,
            fg_color="#2e7d32",
            hover_color="#1b5e20",
        )
        self.save_btn.pack(padx=10, pady=15)

        # Right Side: Scrollable Notes Display
        self.notes_frame = ctk.CTkScrollableFrame(
            self, label_text="Saved Notes", label_font=("Helvetica", 16, "bold")
        )
        self.notes_frame.grid(
            row=0, column=1, padx=(0, 15), pady=15, sticky="nsew"
        )

    def add_note(self):
        """Inserts a new note into SQLite database and refreshes display."""
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", "end-1c").strip()

        if title and content:
            self.cursor.execute(
                "INSERT INTO notes (title, content) VALUES (?, ?)",
                (title, content),
            )
            self.conn.commit()

            # Clear inputs and reload list
            self.title_entry.delete(0, "end")
            self.content_text.delete("1.0", "end")
            self.load_notes()

    def load_notes(self):
        """Fetches notes from SQLite DB and dynamically populates cards in UI."""
        # Clear existing note cards from UI
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        # Query database for notes (newest first)
        self.cursor.execute(
            "SELECT id, title, content FROM notes ORDER BY id DESC"
        )
        notes = self.cursor.fetchall()

        # Render each note as a card widget
        for note_id, title, content in notes:
            card = ctk.CTkFrame(
                self.notes_frame, corner_radius=8, fg_color=("gray85", "gray20")
            )
            card.pack(fill="x", pady=5, padx=5)

            ctk.CTkLabel(
                card, text=title, font=("Helvetica", 14, "bold"), anchor="w"
            ).pack(fill="x", padx=10, pady=(8, 2))

            ctk.CTkLabel(
                card,
                text=content,
                font=("Helvetica", 12),
                wraplength=340,
                justify="left",
                anchor="w",
            ).pack(fill="x", padx=10, pady=(0, 5))

            # Delete button linked to note ID
            ctk.CTkButton(
                card,
                text="Delete",
                width=60,
                height=22,
                fg_color="#D32F2F",
                hover_color="#9A0007",
                font=("Helvetica", 10),
                command=lambda nid=note_id: self.delete_note(nid),
            ).pack(anchor="e", padx=10, pady=(0, 8))

    def delete_note(self, note_id):
        """Removes a note record from the database by ID."""
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()
        self.load_notes()

    def destroy(self):
        """Safely close database connection on app exit."""
        self.conn.close()
        super().destroy()


if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()