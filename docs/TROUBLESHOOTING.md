# Troubleshooting

## Merge Conflicts
```bash
git pull origin main
# Sửa conflict trong VS Code (chọn their/your/both)
git add .
git commit -m "Resolve conflict"
git push
```

## Lỡ commit API key
```bash
git rm --cached config/api_keys.json
git commit --amend --no-edit
git push --force-with-lease
```
Sau đó **thu hồi (revoke) key đó ngay** trên dashboard của dịch vụ, vì nó đã từng lên GitHub.

## Không push được (người khác push trước)
```bash
git pull origin [branch]
git push origin [branch]
```

## Muốn undo commit cuối (giữ lại thay đổi)
```bash
git reset --soft HEAD~1
```

## ffmpeg not found
Kiểm tra đã cài và thêm vào PATH: `ffmpeg -version`. Xem [SETUP.md](../SETUP.md).
