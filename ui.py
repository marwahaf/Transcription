import tkinter as tk
from tkinter import Label, Message, N, StringVar, W, filedialog, messagebox

import main

window = tk.Tk()
window.geometry("400x300")
window.resizable(0, 0)
window.title("Transcription")

ourMessage = "Choose your model for the transcription"
messageVar = Label(window, text=ourMessage)
messageVar.config(bg="white", font=("Times", 10))
messageVar.place(x=0, y=0)
messageVar.pack()

model = tk.StringVar(window, "base")
tk.Radiobutton(window, text="tiny", variable=model, value="tiny").pack(anchor=W)
tk.Radiobutton(window, text="base", variable=model, value="base").pack(anchor=W)
tk.Radiobutton(window, text="medium", variable=model, value="medium").pack(anchor=W)
tk.Radiobutton(window, text="large", variable=model, value="large").pack(anchor=W)

folder_path = StringVar()


def loadtemplate():
    filename = filedialog.askopenfilename(
        parent=window,
        title="Browse File",
        filetypes=[("Audio Files", "*.mp3")],
    )
    folder_path.set(filename)
    return filename


button2 = tk.Button(window, text="Browse for the audio", width=25, command=loadtemplate)
button2.pack()

button = tk.Button(
    window,
    text="Transcrire",
    width=25,
    command=lambda: main.transcribe_audio(model.get(), folder_path.get()),
)
button.pack()

window.mainloop()
