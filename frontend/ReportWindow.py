import datetime

import customtkinter as ctk

from FilePathing import resource_path
from backend.LoadItems import get_report
from backend.Order import Order
from frontend import UserWindow
from PIL import Image

class ReportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="#fdc30d")
        self.logo = Image.open(resource_path("Assets/BigBoyzLogo.png"))

        self.logoLabel = ctk.CTkLabel(self, text=" ", image=ctk.CTkImage(self.logo, size=(400, 400)))
        self.logoLabel.pack(padx=10, pady=10)

        self.report_label = ctk.CTkLabel(self, text="View Report", font = self.parent.get_main_font())
        self.report_label.pack(side="top", fill="x")
        self.return_button = ctk.CTkButton(self, text="Return to User Window", command=lambda:self.parent.show_frame("UserFrame"),
                                           font = self.parent.get_main_font())
        self.return_button.pack(side="top", fill="x")

        self.report_frame = ReportItemsFrame(self)
        self.report_frame.pack(side="top", fill="x")

class ReportItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="#fdc30d")


    def set_report_frames(self):
        report = get_report(resource_path("Records/" + str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".txt"))
        size = len(report)
        cols = 3
        rows = (size + cols - 1) // cols
        k = 1
        for i in range(rows):
            for j in range(cols):
                if k < size:
                    self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(j, weight=1)
                    order = report[k].strip().split(", ", 1)
                    print(order)
                    print(order[0])

                    report_frame = ReportItem(self, order)
                    report_frame.grid(row = i, column = j, sticky = "nsew")
                    k+=1
                else:
                    break

class ReportItem(ctk.CTkFrame):
    def __init__(self, parent, order):
        super().__init__(parent)
        self.parent = parent

        self.order_label = ctk.CTkLabel(self, text="Order Number: " + order[0], font = self.parent.parent.parent.get_sub_font())
        self.order_label.grid(row = 0, column = 0, sticky = "ns")

        self.item_label = ctk.CTkLabel(self, text="Items: " + order[1], font = self.parent.parent.parent.get_sub_font())
        self.item_label.grid(row = 1, column = 0, sticky = "ns")