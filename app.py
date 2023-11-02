import customtkinter as tk
from tkinter import filedialog
import pyttsx3
from CTkMessagebox import CTkMessagebox
from PIL import Image

class TextToAudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Audio Converter")
        self.root.iconbitmap(r'icon.ico')
        self.root.geometry("800x600")
        self.root.configure(bg="#333333")  # Dark background color
        tk.set_default_color_theme("green")

        my_image = tk.CTkImage(light_image=Image.open("logo-v1.png"),
                               dark_image=Image.open("logo-v1.png"),
                               size=(150, 80))

        self.logo_label = tk.CTkLabel(self.root, image=my_image, text="")
        self.logo_label.pack(padx=10, pady=5,)

        # Set up main content area
        self.main_frame = tk.CTkFrame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        self.label_text = tk.CTkLabel(self.main_frame, text="Enter your text:", font=("Arial", 12))
        self.label_text.pack(pady=(20, 5))

        self.text_input = tk.CTkTextbox(self.main_frame, wrap="word", width=500, height=150)
        self.text_input.pack(pady=(0, 10))
        # Create a variable to hold the selected voice
        self.selected_voice = tk.StringVar(value="female")  # Default to female

        # Radio buttons for voice selection
        self.label_voice = tk.CTkLabel(self.main_frame, text="Select Voice:", font=("Arial", 12))
        self.label_voice.pack(pady=(10, 5))

        self.radio_female = tk.CTkRadioButton(self.main_frame, text="Female", variable=self.selected_voice, value="female")
        self.radio_female.pack(anchor=tk.CENTER, pady=(0, 10))

        self.radio_male = tk.CTkRadioButton(self.main_frame, text="Male", variable=self.selected_voice, value="male")
        self.radio_male.pack(anchor=tk.CENTER, pady=(0, 10))

        self.label_save = tk.CTkLabel(self.main_frame, text="Choose save location:", font=("Arial", 12), )
        self.label_save.pack(pady=(0, 5))

        self.save_location = tk.CTkEntry(self.main_frame, width=400, height=30)
        self.save_location.pack(pady=(0, 10),)
        self.browse_button = tk.CTkButton(self.main_frame, text="Browse", command=self.browse_save_location, )
        self.browse_button.pack(pady=(0, 10))


        self.convert_button = tk.CTkButton(self.main_frame, text="Convert", command=self.convert_text_to_audio, )
        self.convert_button.pack(pady=(0, 20))

    def browse_save_location(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        self.save_location.delete(0, tk.END)
        self.save_location.insert(0, file_path)

    def convert_text_to_audio(self):
        text = self.text_input.get("1.0", tk.END)
        save_path = self.save_location.get()

        if not text.strip():
            CTkMessagebox(title="warning", message="Please enter text.", icon="warning", option_1="Ok")
            return

        if not save_path:
            CTkMessagebox(title="warning", message="Please choose a save location.", icon="warning", option_1="Ok")
            return

        try:


            engine = pyttsx3.init("sapi5")
            voices = engine.getProperty('voices')
            selected_voice = self.selected_voice.get()  # Get the actual value

            if selected_voice == "female":
                engine.setProperty("voice", voices[1].id)
            elif selected_voice == "male":
                engine.setProperty("voice", voices[0].id)

            engine.save_to_file(text, save_path)
            engine.runAndWait()

            CTkMessagebox(message="Text converted to audio successfully!", icon="check", option_1="close")

        except Exception as e:
            CTkMessagebox(title="Error", message=f"An error occurred: {str(e)}", icon="warning", option_1="close")





if __name__ == "__main__":
    root = tk.CTk()
    app = TextToAudioConverterApp(root)
    root.mainloop()
