"""Chuyển ảnh thành video 4 giây, gọi Kling/Veo3 theo config/settings.json."""
from tools.utils.logger import get_logger

logger = get_logger(__name__)


def convert_to_video(image_path: str, motion_prompt: str, duration_seconds: int = 4) -> str:
    """Chuyển 1 ảnh thành video ngắn có chuyển động. Trả về path video output.

    TODO: tích hợp API Kling/Veo3 thật.
    """
    raise NotImplementedError("video_converter.convert_to_video chưa được tích hợp API")
