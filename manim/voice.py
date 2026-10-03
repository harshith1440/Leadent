from elevenlabs.client import ElevenLabs
from elevenlabs import save

# 🔑 Paste your API key here
client = ElevenLabs(api_key="b37ddf27b71d41b6c89efcfe99843df5e35f1072063a156180b369dd87620389")

text = """
Computers cannot understand human language directly.
They understand instructions written in programming languages.

One of the most important programming languages is C.
C is used to communicate with computers.

Now let us look at a simple C program.
"""

audio = client.text_to_speech.convert(
    text=text,
    voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice
    model_id="eleven_multilingual_v2"
)

save(audio, "voice.mp3")