# Voice-to-Text and Text-to-Voice System

This project provides a simple graphical user interface (GUI) for performing Speech-to-Text (STT) and Text-to-Speech (TTS) operations. The application supports multiple languages and utilizes the `gTTS` and `speech_recognition` libraries for TTS and STT functionalities, respectively.

## Features

- **Speech-to-Text**: Converts speech input from a microphone into text.
- **Text-to-Speech**: Converts user-provided text into speech and plays it back.
- **Multi-language Support**: Specify the language for both STT and TTS via language codes (e.g., `hi-IN` for Hindi speech recognition, `hi` for Hindi text-to-speech).
- **Dynamic Status Updates**: Provides real-time feedback during operations.
- **Error Handling**: Alerts the user if input is missing or if operations fail.
- **Scrollable Widgets**: For convenient text input and output.

## Prerequisites

- Python 3.8+
- The following Python libraries:
  - `gTTS`
  - `speech_recognition`
  - `sounddevice`
  - `numpy`
  - `tkinter`

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

   ```bash
   pip install gTTS speechrecognition sounddevice numpy
   ```

## How to Run

1. Save the code in a Python file (e.g., `voice_text_gui.py`).
2. Run the script:

   ```bash
   python voice_text_gui.py
   ```
3. The GUI will open, allowing you to:
   - Enter a language code.
   - Record speech for STT or input text for TTS.
   - View the results or play the converted speech.

## Usage

1. **Speech-to-Text**:
   - Enter the desired language code (e.g., `en-IN`, `hi-IN`) in the `Language Code` field.
   - Click the `Convert Speech to Text` button.
   - Speak into the microphone when prompted.
   - The recognized text will be displayed in the `Speech-to-Text Output` box.

2. **Text-to-Speech**:
   - Enter the desired language code (e.g., `en`, `hi`) in the `Language Code` field.
   - Type the text you want to convert into the `Enter Text for Text-to-Speech` box.
   - Click the `Convert Text to Speech` button to hear the playback.

## Supported Languages

- For a complete list of supported languages and their codes, refer to the [gTTS Documentation](https://gtts.readthedocs.io/en/latest/module.html#available-languages).

## Screenshots

1. **Main GUI**:
   - Input field for language codes.
   - Text area for TTS input.
   - Scrollable output for STT results.

2. **Status Updates**:
   - Real-time feedback, such as "Recording...", "Recognizing speech...", or "Text-to-Speech conversion failed."

## Known Issues

- Ensure your microphone is properly configured and accessible.
- Background noise may affect speech recognition accuracy.

## License

This project is licensed under the MIT License. Feel free to use and modify the code.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

