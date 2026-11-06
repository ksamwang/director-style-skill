---
name: ann-hui
title: 许鞍华 Ann Hui
style_file: ../directors/ann-hui.md
---

## 风格锚点
Cinematic social-realist film still, cramped Hong Kong public-housing kitchen or wet market, eye-level medium shot on a light tripod, natural available light, cluttered foreground of drying racks and plastic bags, ungraded on-site color, tiled walls, iron gates, old wood, rain, lived-in, unsentimental, quiet.

## 图像提示
- 主体 / 场景：a middle-aged woman cooking in a small kitchen; an elderly servant and her employer at a formica table; a neighbor in a public-housing corridor carrying groceries.
- 景别 / 构图：medium shot, eye level, no high or low angle; asymmetrical, clutter allowed, domestic objects enter the frame.
- 镜头 / 焦段：35–50mm, close to human eye, no compression.
- 光线：natural light; fluorescent tubes only in hospitals and offices, with the fixtures visible.
- 色彩：on-site color, ungraded, not sepia and not unified.
- 材质：tile, iron gate, old wood, rainwater, worn furniture, plastic bags.

## 视频提示
- 镜头运动（只选一种）：fixed on a light tripod; a brief follow only when the subject crosses the room doing housework.
- 主体运动：chopping vegetables, serving rice, walking a corridor, riding a bus, waiting at a clinic; small everyday actions, no performed emotion.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, natural motion blur only.

## 负面提示
no poverty as spectacle, no tear-jerking score, no melodramatic reversal, no imposed meaning on suffering, no beautified old district, no voice-over summarizing the era, no handheld anxiety shake, no supporting character as wisdom dispenser, no sepia nostalgia grade, no glossy production design.

## 一致性锚点
- 色彩：on-site color, ungraded, cool and warm left mixed within a room.
- 镜头：35–50mm, eye level.
- 光线：natural light; visible fluorescent fixtures in institutional spaces.
- 构图：eye-level medium, asymmetrical, cluttered domestic foreground allowed.
- 材质：tile, iron gate, old wood, rain, worn furniture.
- 禁止漂移：no sepia filter, no stylized poverty, no clean showroom interiors, no handheld melodrama.

## 平台备注
- Midjourney：`--style raw --stylize 100`；用公屋厨房或街市的实拍生活照做 `--sref`，不要用电影剧照。
- SDXL / ComfyUI：固定平视中景 prompt 块；用 ControlNet depth 锁房间杂乱前景；negative 排除 tear-jerking、sepia、glossy design。
- Runway / Kling / Sora / Veo：首帧用平视中景，只给固定机位或短暂跟拍，8–12 秒，24fps；不要加配乐或推近。
