# API Setup

Hướng dẫn lấy API key cho từng dịch vụ dùng trong pipeline.

## Midjourney
Dùng qua Discord bot — cần Discord token của server chạy Midjourney.
Docs: https://docs.midjourney.com

## Ideogram
Đăng ký tại ideogram.ai, lấy API key trong phần Settings → API.

## Kling
Đăng ký tại https://klingai.com/api, lấy API key.

## Veo 3
Cần Google Cloud API key có bật Veo/Gemini API.

## ElevenLabs
Đăng ký ElevenLabs Pro, lấy API key và chọn `voice_id` giọng tiếng Việt phù hợp.
Docs: https://elevenlabs.io/docs

## OpenAI (Whisper)
Lấy API key tại platform.openai.com, dùng cho sinh phụ đề tự động.

## YouTube Upload
Tạo OAuth client (client_id + client_secret) trong Google Cloud Console, bật YouTube Data API v3.

Sau khi có đủ key, điền vào `config/api_keys.json` (copy từ `config/api_keys.example.json`, không commit file này).
