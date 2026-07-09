# Daily Workflow Guide

## Quy trình tạo 1 video

1. Viết script trong `scripts/projects/<ten-du-an>/script.md` (dùng template trong `scripts/templates/`)
2. Gắn tag nhân vật (`CHAR_001`, `CHAR_002`, ...) cho từng cảnh — xem `characters/`
3. Tạo/xác nhận ảnh tham chiếu nhân vật trong `characters/reference_images/`
4. Chạy pipeline:
   ```bash
   python tools/pipeline/video_pipeline.py --project <ten-du-an>
   ```
5. Kiểm tra output trong `generated/videos/`
6. Review và lặp lại nếu cần

## Git branching

### Quy ước đặt tên nhánh

```
main                              # bản production-ready
├── person-1/script-constantinople
├── person-2/characters-design
├── person-1/prompts-ottoman
└── person-2/pipeline-audio
```

### Quy trình

**Buổi sáng: lấy code mới nhất**
```bash
git pull origin main
```

**Bắt đầu tính năng mới**
```bash
git checkout -b [ten-cua-ban]/[ten-tinh-nang]
# Vi du: git checkout -b person-1/script-constantinople
```

**Làm việc và commit**
```bash
git status
git add <file-da-sua>
git commit -m "Mo ta ro rang thay doi"
git push origin [ten-nhanh]
```

**Khi xong tính năng**
- Vào GitHub → "Compare & pull request"
- Mô tả thay đổi
- Người còn lại review → approve → merge
- Xóa nhánh sau khi merge

**Lấy code của người kia**
```bash
git checkout main
git pull origin main
```

## Xử lý sự cố thường gặp

Xem [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).
