from gtts import gTTS
import tempfile
from llm_mod import expressed_text

def text_to_speech(text, filename="audiobook.mp3"):
    tts = gTTS(text, lang="en", slow=True)
    tts.save(filename)
    return filename
# tts_engine.py


def generate_audio(texts, expression):
    if expression == "Normal":
        modified_text=texts

    else:
        # Modify text based on expression
        modified_text =expressed_text(texts, expression)
        special="~!@#$%^&*()_+=-:<>?';,./'""`*/"
        for text in modified_text:
            if text  in special:
                pass





    tts = gTTS(text=modified_text, lang="en")


    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name