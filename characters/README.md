# Characters

Hệ thống character tagging đảm bảo một nhân vật luôn trông giống nhau xuyên suốt video, dù xuất hiện ở cảnh 10, 30 hay 150.

## Quy tắc

1. Mỗi nhân vật có một mã duy nhất: `CHAR_001`, `CHAR_002`, ...
2. Mỗi mã có đúng 3 ảnh tham chiếu trong `reference_images/`, đặt tên: `CHAR_001_<ten>_ref1.png`, `ref2`, `ref3`.
3. File thiết kế nhân vật nằm trong `designs/CHAR_001_<ten>.json`:

```json
{
  "CHAR_001": {
    "name": "Mehmed II",
    "era": "ottoman_1453",
    "reference_images": [
      "CHAR_001_mehmed_ref1.png",
      "CHAR_001_mehmed_ref2.png",
      "CHAR_001_mehmed_ref3.png"
    ]
  }
}
```

4. Trong script, gắn tag nhân vật ở phần `**Characters:**` của mỗi cảnh — pipeline sẽ tự động lấy đúng 3 ảnh tham chiếu này khi sinh ảnh cho cảnh đó.
