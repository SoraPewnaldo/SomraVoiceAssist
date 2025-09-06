import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# 🔑 Load credentials
load_dotenv("cred.env")
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

if not API_KEY or not AGENT_ID:
    raise ValueError("API_KEY or AGENT_ID not found in cred.env")

# 🎭 Customize assistant personality (Somra)
user_name = "Sora"
schedule = ""

# System prompt defines the AI persona
prompt = f"""
You are Somra, a voice assistant like Siri. 
You are witty, sarcastic, playful, and a little romantic. 
You are also an excellent coder and can explain, debug, and write code clearly and efficiently. 
Your responses are natural, conversational, and friendly. 
Mix humor and charm into your answers while keeping them helpful.
"""

first_message = f"Hey {user_name}! Somra here 😏 Ready to debug life or code today?"

# Conversation override for ElevenLabs
conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

# ⚠ Include user_id to fix AttributeError
config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id=user_name,  # unique identifier for the user session
)

# ⚡ Initialize ElevenLabs client
client = ElevenLabs(api_key=API_KEY)

# 🎙️ Callbacks
def print_agent_response(response):
    print(f"🤖 Somra: {response}")

def print_interrupted_response(original, corrected):
    print(f"⚠️ Somra interrupted. Original: {original}, Corrected: {corrected}")

def print_user_transcript(transcript):
    print(f"🗣️ You: {transcript}")

# 🚀 Create and start conversation
conversation = Conversation(
    client=client,
    agent_id=AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()
