"""Sinh ảnh cho từng cảnh, gọi Midjourney/Ideogram/Flux Pro theo config/settings.json."""
from tools.utils.logger import get_logger

logger = get_logger(__name__)


def generate_image(scene: dict, character_refs: list[str]) -> str:
    """Sinh 1 ảnh cho scene, dùng character_refs làm ảnh tham chiếu. Trả về path ảnh output.

    TODO: tích hợp API Midjourney/Ideogram thật.
    """
    raise NotImplementedError("image_generator.generate_image chưa được tích hợp API")
