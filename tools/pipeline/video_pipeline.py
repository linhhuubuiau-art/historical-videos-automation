"""Orchestrator chính: script.md -> scenes.json -> ảnh -> video -> audio -> phụ đề -> video cuối cùng.

Usage:
    python tools/pipeline/video_pipeline.py --project <ten-du-an>
    python tools/pipeline/video_pipeline.py --check
"""
import argparse

from tools.utils.logger import get_logger

logger = get_logger(__name__)


def check_environment() -> None:
    """Kiểm tra nhanh: ffmpeg có trong PATH, config/api_keys.json tồn tại, v.v."""
    import shutil
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[2]
    api_keys_path = project_root / "config" / "api_keys.json"

    logger.info("ffmpeg found: %s", bool(shutil.which("ffmpeg")))
    logger.info("config/api_keys.json exists: %s", api_keys_path.exists())


def run_pipeline(project_name: str) -> None:
    """Chạy toàn bộ pipeline cho 1 project trong scripts/projects/<project_name>/.

    TODO: parse script.md -> scenes.json, sau đó gọi image_generator, video_converter,
    audio_processor, ffmpeg_assembler theo thứ tự.
    """
    raise NotImplementedError(f"Pipeline cho project '{project_name}' chưa được implement")


def main() -> None:
    parser = argparse.ArgumentParser(description="Historical video automation pipeline")
    parser.add_argument("--project", help="Ten thu muc trong scripts/projects/")
    parser.add_argument("--check", action="store_true", help="Kiem tra moi truong cai dat")
    args = parser.parse_args()

    if args.check:
        check_environment()
    elif args.project:
        run_pipeline(args.project)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
