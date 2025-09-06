# 🎤 Somra – Voice Virtual Assistant

<p align="center">
  <img src="coin-logo.png" alt="Somra Logo" width="120"/>
</p>

> A witty, sarcastic, and romantic AI voice assistant built with [ElevenLabs Conversational AI](https://elevenlabs.io/)

---

## 🚀 Features
- 🎙️ Listens to your voice in real-time
- 🧠 Responds with personality (funny, sarcastic, and romantic)
- 🔊 Speaks back with natural voice synthesis
- 🔁 Handles interruptions smoothly

---

## 📦 Requirements

- **Windows 10/11**
- Python **3.11+**
- [ElevenLabs Python SDK](https://pypi.org/project/elevenlabs/)
- `python-dotenv`
- `pyaudio`

---

## ⚙️ Installation  

Clone the repository:
```bash
git clone https://github.com/your-username/SomraVoiceAssist.git
cd SomraVoiceAssist
Create a virtual environment:

python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
🔑 Setup Environment Variables
In the project root, create a file named .env and add:

AGENT_ID=your_agent_id
API_KEY=your_api_key
⚠️ Important:

Do not upload .env to GitHub (it’s already in .gitignore).

Get your Agent ID and API key from the ElevenLabs Console.

▶️ Run the Assistant
Start the assistant:


python main.py
Speak into your microphone — Somra will listen, think, and reply with voice.

🛠️ Project Structure
bash
Copy code
SomraVoiceAssist/
│── main.py          # Main assistant script
│── .env             # Your secret API keys (ignored by git)
│── .gitignore       # Prevents uploading secrets and caches
│── requirements.txt # Dependencies
│── README.md        # Documentation
📖 How It Works
Microphone Input → Captures your speech

ElevenLabs API → Transcribes and generates a witty response

Text-to-Speech → Converts response into voice

Audio Playback → Speaks back to you in real time

Callbacks in main.py:

print_agent_response(response) → shows AI responses

print_user_transcript(transcript) → shows what you said

print_interrupted_response(original, corrected) → handles cut-off replies

🎯 Next Steps
🎨 Add custom voice profiles for Somra

🖥️ Build a GUI (Tkinter or PyQt) for easier use

📅 Connect with calendar & reminders

🛠️ Expand personality via system prompts

📚 Resources
ElevenLabs Conversational AI Docs

Python SDK

👤 Author
Sora

GitHub: SoraPewnaldo

📝 License
This project is licensed under the MIT License.

✨ “Somra — Not just an assistant, but a personality.” ❤️😏