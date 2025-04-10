import datetime

import customtkinter as ctk

from FilePathing import resource_path
from backend.LoadItems import get_report
from backend.Order import Order
from frontend import UserWindow


class ReportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.report_label = ctk.CTkLabel(self, text="View Report")
        self.report_label.pack(side="top", fill="x")
        self.return_button = ctk.CTkButton(self, text="Return to User Window", command=lambda:self.parent.show_frame("UserWindow"))

        self.report_frame = ReportItemsFrame(self)

class ReportItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.report = get_report(resource_path("Records/"+str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".txt"))
        print(self.report)
        self.report_size = len(self.report)
        for i in range(1, self.report_size):
            parts = self.report[i].strip().split(", ", 1)

