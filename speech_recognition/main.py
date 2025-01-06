from gtts import gTTS
import os
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import messagebox, scrolledtext

def record_audio(duration=5, fs=16000):
    status_label.config(text="Recording... Please speak now.", fg="blue")
    root.update()
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return audio_data

def speechtotext(language):
    recognizer = sr.Recognizer()
    try:

        audio_data = record_audio()
        audio_data_instance = sr.AudioData(audio_data.tobytes(), 16000, 2)

        status_label.config(text="Recognizing speech...", fg="blue")
        root.update()
        text = recognizer.recognize_google(audio_data_instance, language=language)
        status_label.config(text="Speech recognized successfully!", fg="green")
        return text
    except sr.UnknownValueError:
        status_label.config(text="Could not understand the audio.", fg="red")
        messagebox.showerror("Error", "Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        status_label.config(text="Speech recognition request failed.", fg="red")
        messagebox.showerror("Error", f"Could not request results: {e}")
        return None

def texttospeech(text, language):
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        filename = "output.mp3"
        tts.save(filename)
        status_label.config(text="Playing the converted speech...", fg="green")
        os.system(f"start {filename}" if os.name == "nt" else f"open {filename}")
    except Exception as e:
        status_label.config(text="Text-to-Speech conversion failed.", fg="red")
        messagebox.showerror("Error", f"Text-to-Speech failed: {e}")

def handle_speechtotext():
    language = language_entry.get()
    if not language:
        messagebox.showwarning("Input Error", "Please enter a language code for recognition.")
        return
    text = speechtotext(language)
    if text:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, text)

def handle_texttospeech():
    text = text_input.get("1.0", tk.END).strip()
    language = language_entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to convert.")
        return
    if not language:
        messagebox.showwarning("Input Error", "Please enter a language code for TTS.")
        return
    texttospeech(text, language)

root = tk.Tk()
root.title("Voice-to-Text and Text-to-Voice System")
root.geometry("600x500")

tk.Label(root, text="Language Code (e.g., 'hi-IN' for Speech-to-Text, 'hi' for Text-to-Speech):").pack(pady=5)
language_entry = tk.Entry(root, width=30)
language_entry.pack(pady=5)

tk.Label(root, text="Enter Text for Text-to-Speech:").pack(pady=5)
text_input = scrolledtext.ScrolledText(root, height=5, width=60)
text_input.pack(pady=5)

tk.Label(root, text="Speech-to-Text Output:").pack(pady=5)
text_output = scrolledtext.ScrolledText(root, height=5, width=60)
text_output.pack(pady=5)

tk.Button(root, text="Convert Speech to Text", command=handle_speechtotext, bg="lightblue").pack(pady=10)
tk.Button(root, text="Convert Text to Speech", command=handle_texttospeech, bg="lightgreen").pack(pady=10)

status_label = tk.Label(root, text="Status: Waiting for input", fg="blue")
status_label.pack(pady=10)

root.mainloop()
