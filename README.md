Perfect 👌 I’ll clean it up:

* ✅ Removed the coin/logo
* ✅ Author is now **Sora**
* ✅ GitHub username linked as **sorapewnaldo**
* ✅ Removed the word “Windows” (so it looks OS-agnostic)
* ✅ Added nice badges (install + usage)

Here’s your **final `README.md`**:

````markdown
# 🎤 Somra – Voice Virtual Assistant

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Install](https://img.shields.io/badge/Install-pip%20install%20requirements.txt-brightgreen.svg)](#-installation)
[![Usage](https://img.shields.io/badge/Run-python%20main.py-orange.svg)](#️-run-the-assistant)

> A witty, sarcastic, and romantic AI voice assistant built with [ElevenLabs Conversational AI](https://elevenlabs.io/).

---

## 🚀 Features
- 🎙️ Listens to your voice in real-time  
- 🧠 Responds with personality (funny, sarcastic, and romantic)  
- 🔊 Speaks back with natural voice synthesis  
- 🔁 Handles interruptions smoothly  
- 🔐 Secure `.env` file for your API credentials  

---

## 📦 Requirements

- Python **3.11+**
- [ElevenLabs Python SDK](https://pypi.org/project/elevenlabs/)
- `python-dotenv`
- `pyaudio`

---

## ⚙️ Installation  

Clone the repository:
```bash
git clone https://github.com/sorapewnaldo/SomraVoiceAssist.git
cd SomraVoiceAssist
````

Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # On macOS/Linux use: source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

In the project root, create a file named `.env` and add:

```
AGENT_ID=your_agent_id
API_KEY=your_api_key
```

⚠️ **Important**:

* Do **not** upload `.env` to GitHub (it’s already in `.gitignore`).
* Get your Agent ID and API key from the [ElevenLabs Console](https://elevenlabs.io/).

---

## ▶️ Run the Assistant

Start the assistant:

```bash
python main.py
```

Speak into your microphone — Somra will listen, think, and reply with voice.

---

## 🛠️ Project Structure

```
SomraVoiceAssist/
│── main.py          # Main assistant script
│── .env             # Your secret API keys (ignored by git)
│── .gitignore       # Prevents uploading secrets and caches
│── requirements.txt # Dependencies
│── README.md        # Documentation
```

---

## 📖 How It Works

1. **Microphone Input** → Captures your speech
2. **ElevenLabs API** → Transcribes and generates a witty response
3. **Text-to-Speech** → Converts response into voice
4. **Audio Playback** → Speaks back to you in real time

Callbacks in `main.py`:

* `print_agent_response(response)` → shows AI responses
* `print_user_transcript(transcript)` → shows what you said
* `print_interrupted_response(original, corrected)` → handles cut-off replies

---

## 🎯 Next Steps

* 🎨 Add custom voice profiles for Somra
* 🖥️ Build a GUI (Tkinter or PyQt) for easier use
* 📅 Connect with calendar & reminders
* 🛠️ Expand personality via system prompts

---

## 📚 Resources

* [ElevenLabs Conversational AI Docs](https://elevenlabs.io/docs/conversational-ai/overview)
* [Python SDK](https://github.com/elevenlabs/elevenlabs-python)

---

## 👤 Author

**Sora**

* GitHub: [SoraPewnaldo](https://github.com/SoraPewnaldo)

---

## 📝 License

This project is licensed under the MIT License.

---

✨ *“Somra — Not just an assistant, but a personality.”* ❤️😏
