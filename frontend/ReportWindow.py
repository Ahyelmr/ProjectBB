import customtkinter as ctk

class ReportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.report_label = ctk.CTkLabel(self, text="View Report")
        self.report_label.pack(side="top", fill="x")
