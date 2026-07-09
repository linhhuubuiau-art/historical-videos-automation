"""Sinh giọng đọc (TTS qua ElevenLabs) và phụ đề (Whisper)."""
from tools.utils.logger import get_logger

logger = get_logger(__name__)


def generate_voiceover(script_text: str, voice_id: str) -> str:
    """Sinh file audio giọng đọc từ text. Trả về path file audio.

    TODO: tích hợp API ElevenLabs thật.
    """
    raise NotImplementedError("audio_processor.generate_voiceover chưa được tích hợp API")


def generate_subtitles(audio_path: str) -> str:
    """Sinh file phụ đề .srt từ audio bằng Whisper. Trả về path file srt.

    TODO: tích hợp API Whisper thật.
    """
    raise NotImplementedError("audio_processor.generate_subtitles chưa được tích hợp API")
