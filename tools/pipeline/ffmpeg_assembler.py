"""Ghép các video cảnh + audio + phụ đề thành video hoàn chỉnh bằng FFmpeg."""
from tools.utils.logger import get_logger

logger = get_logger(__name__)


def assemble_final_video(scene_video_paths: list[str], audio_path: str, subtitle_path: str, output_path: str) -> str:
    """Ghép danh sách video cảnh theo thứ tự, đồng bộ với audio, gắn phụ đề, xuất MP4 cuối cùng.

    TODO: dựng lệnh ffmpeg thật (concat + audio mux + subtitle burn-in/soft sub).
    """
    raise NotImplementedError("ffmpeg_assembler.assemble_final_video chưa được implement")
