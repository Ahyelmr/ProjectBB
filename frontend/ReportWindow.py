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
        self.return_button = ctk.CTkButton(self, text="Return to User Window", command=lambda:self.parent.show_frame("UserFrame"))
        self.return_button.pack(side="top", fill="x")

        self.report_frame = ReportItemsFrame(self)
        self.report_frame.pack(side="top", fill="x")

class ReportItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.report = get_report(resource_path("Records/"+str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".txt"))
        print(self.report)
        self.report_size = len(self.report)
        """
        for i in range(1, self.report_size):
            parts = self.report[i].strip().split(", ", 1)
            items = parts[1]
            order_label = ctk.CTkLabel(self, text=("Order Number: " + parts[0]))
            order_label = order_label.pack(side="top", fill="x")
            for j in range(items):
                item_label = ctk.CTkLabel(self, text=("Item: " + items[j]))
                item_label = item_label.pack(side="top", fill="x")
        """

    def set_report_frames(self):
        size = len(self.report)
        cols = 5
        rows = (size + cols - 1) // cols
        k = 1
        for i in range(rows):
            for j in range(cols):
                if k < size:
                    self.grid_rowconfigure(i, weight=1)
                    self.grid_columnconfigure(j, weight=1)
                    order = self.report[k].strip().split(", ", 1)
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

        self.order_label = ctk.CTkLabel(self, text="Order Number: " + order[0])
        self.order_label.grid(row = 0, column = 0, sticky = "ns")

        self.item_label = ctk.CTkLabel(self, text="Items: " + order[1])
        self.item_label.grid(row = 1, column = 0, sticky = "ns")