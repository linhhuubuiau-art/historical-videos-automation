# Prompts

- `eras/` — bộ từ khóa phong cách (style keywords) theo từng thời kỳ lịch sử, dùng làm nền cho prompt sinh ảnh/video của mọi cảnh trong thời kỳ đó.
- `scene_templates.json` — khung prompt chung cho từng loại cảnh (chân dung, toàn cảnh, chiến trận, đối thoại...).

Mỗi file era có cấu trúc:
```json
{
  "era_id": "ottoman_1453",
  "style_keywords": ["...", "..."],
  "negative_keywords": ["...", "..."]
}
```
