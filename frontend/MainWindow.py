from PIL import Image
import customtkinter as ctk

from FilePathing import resource_path

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.configure(fg_color="#fdc30d")

        self.logo = Image.open(resource_path("Assets/BigBoyzLogo.png"))

        self.logoLabel = ctk.CTkLabel(self, text = " ", image=ctk.CTkImage(self.logo, size = (400, 400)))
        self.logoLabel.pack(padx = 10, pady = 10)

        self.MainLabel = ctk.CTkLabel(self, text="Project BB\nWelcome", font = self.parent.get_main_font(),
                                      fg_color="#ed1e24", text_color="#1a1a1a", width = 200, height = 150, corner_radius=50)
        self.MainLabel.pack(padx = 10, pady = 10)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(anchor = "center", padx = 10, pady = 10)

        self.SignupButton = ctk.CTkButton(self.button_frame,text="Sign Up", command=lambda: self.on_signup_click(), font = self.parent.get_main_font())
        self.SignupButton.pack(side = "left", anchor="center", padx = 10, pady = 10)

        self.LoginButton = ctk.CTkButton(self.button_frame, text="Login", command=lambda: self.on_login_click(), font = self.parent.get_main_font())
        self.LoginButton.pack(side = "left", anchor="center", padx = 10, pady = 10)

    def on_signup_click(self):
        print("Sign Up button clicked")  # Debugging
        self.parent.set_login(False)  # Set login state for registration
        print(f"Login state after signup: {self.parent.get_login()}")  # Debugging
        self.parent.show_frame("CredentialsFrame")


    def on_login_click(self):
        print("Login button clicked")  # Debugging
        self.parent.set_login(True)  # Set login state for login
        print(f"Login state after login: {self.parent.get_login()}")  # Debugging
        self.parent.show_frame("CredentialsFrame")
