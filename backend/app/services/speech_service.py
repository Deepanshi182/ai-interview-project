# from faster_whisper import WhisperModel
import tempfile
import os

# model = WhisperModel("base", device="cpu", compute_type="int8")
whisper_model = None

def get_whisper():
    global whisper_model

    if whisper_model is None:
        from faster_whisper import WhisperModel
        whisper_model = WhisperModel("base", device="cpu", compute_type="int8")

    return whisper_model

def speech_to_text(audio_bytes):
    model = get_whisper()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    segments, info = model.transcribe(temp_audio_path, beam_size=5)
    
    transcript = " ".join([segment.text for segment in segments])

    os.remove(temp_audio_path)

    return transcript