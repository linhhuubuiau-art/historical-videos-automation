# Setup Instructions

## 1. Clone repo

```bash
git clone https://github.com/linhhuubuiau-art/historical-videos-automation.git
cd historical-videos-automation
```

## 2. Cấu hình Git (mỗi người làm 1 lần)

```bash
git config user.name "Tên của bạn"
git config user.email "email@cua-ban.com"
```

## 3. Cài Python environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

## 4. Tạo API keys

Copy file mẫu và điền key thật (file này **không** được commit):

```bash
cp config/api_keys.example.json config/api_keys.json
```

Điền key cho các dịch vụ:
- Midjourney (Discord token)
- Ideogram
- Kling
- Veo (Google API key)
- ElevenLabs
- OpenAI (Whisper)
- YouTube (upload)

## 5. Cài FFmpeg

- Windows: tải từ https://ffmpeg.org và thêm vào PATH
- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

## 6. Kiểm tra cài đặt

```bash
python tools/pipeline/video_pipeline.py --check
```

Xem [WORKFLOW.md](WORKFLOW.md) để bắt đầu làm việc hàng ngày.
