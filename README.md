# Historical Videos Automation

Hệ thống tự động tạo video lịch sử dài (5-15 phút) bằng AI, dựa theo quy trình của creator "nông dân yêu AI".

## Ý tưởng cốt lõi

Thay vì dựng video thủ công từng khung hình:
1. Viết **một** kịch bản (script)
2. Tạo ảnh tham chiếu nhân vật (3 ảnh/nhân vật)
3. Gắn tag nhân vật xuất hiện trong từng cảnh
4. Hệ thống tự động:
   - Sinh ảnh cho từng cảnh
   - Chuyển ảnh thành video 4 giây
   - Tạo giọng đọc (voiceover)
   - Sinh phụ đề
   - Đồng bộ hình + tiếng
   - Xuất video hoàn chỉnh

## Tech stack

| Việc | Công cụ |
|------|---------|
| Sinh ảnh | Midjourney, Ideogram, Flux Pro |
| Ảnh → Video | Kling 2.6, Veo 3 |
| Text-to-Speech | ElevenLabs Pro |
| Phụ đề | Whisper API |
| Ghép video | FFmpeg + Python |
| Automation | n8n / Make |

## Bắt đầu

Xem [SETUP.md](SETUP.md) để cài đặt và [WORKFLOW.md](WORKFLOW.md) để biết quy trình làm việc hàng ngày.

## Cấu trúc dự án

```
scripts/      # Kịch bản video (theo project)
prompts/      # Thư viện prompt theo thời kỳ lịch sử
characters/   # Thiết kế & ảnh tham chiếu nhân vật
tools/        # Pipeline Python xử lý tự động
generated/    # Output sinh ra (không commit)
config/       # Cấu hình & API keys (không commit key thật)
docs/         # Tài liệu chi tiết
```

## Team

2 người cộng tác qua GitHub. Xem [docs/WORKFLOW.md](docs/WORKFLOW.md) cho quy trình branching.
