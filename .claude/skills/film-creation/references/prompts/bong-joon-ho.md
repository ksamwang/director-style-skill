---
name: bong-joon-ho
title: 奉俊昊 Bong Joon-ho
style_file: ../directors/bong-joon-ho.md
---

## 风格锚点
Cinematic film still, vertical social geography, 24–35mm wide-angle stacking basement, stairwell and rooftop in one frame, subject pushed to the edge while space dominates, foreground diners and background watchers in layered depth, overcast or sourceless practical light, damp concrete and rain, deadpan dread.

## 图像提示
- 主体 / 场景：a family half-hidden behind a semi-basement window at street level; a man descending wet concrete stairs; a long table where one person eats in the foreground while another watches from the next room.
- 景别 / 构图：medium to wide; vertical stacking inside one frame, figure pressed to the frame edge, foreground obstruction, depth planes that each hold a different class; symmetry avoided.
- 镜头 / 焦段：24–35mm wide for the vertical geography, 50–85mm only at the moment of revelation.
- 光线：sourced practical light with type-appropriate contrast — fluorescent basement yellow, cold white in the big house; no decorative glow.
- 色彩：distributed by level — warm yellow and mold green below, cold white, steel and lawn green above; the palette is a map, not a mood.
- 材质：damp concrete, plastic sheeting, rainwater, stainless steel, clipped lawn, cheap tile.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking scan at eye level, sliding across a room to reveal who is standing on which level.
- 主体运动：ordinary and slightly late — a half-beat pause, a slow turn, a look that arrives after the line; then one abrupt movement when the genre turns.
- 时长 / 帧率 / 运动模糊：5–7 seconds, 24fps, minimal blur, no handheld except during the disaster passage.

## 负面提示
no vertical space as pure composition game, no poor-only-virtuous characters, no rich-only-villain, no clever hero who controls the system, no score telling us to be afraid, no grey miserabilism that erases the comedy timing, no solvable ending, no clean basement-plus-rain formula, no symmetrical hero framing, no aerial drone establishing shot, no HDR gloss.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：warm yellow and mold green below, cold white and lawn green above; 24–35mm wide; sourced practical light with class-coded contrast; figure at edge, foreground obstruction, vertical layers; wet concrete, plastic sheet, steel, lawn.
- 禁止漂移：no uniform teal-orange grade, no glossy modern apartment with no grime, no drone aerials, no symmetrical centered framing, no digital skin, no LED white replacing practical sources.

## 平台备注
- Midjourney：`--style raw --stylize 150`；`--sref`用《寄生虫》半地下或豪宅静帧，但不要同时锁两种色调；纵向分层靠构图词 + 参考图。
- SDXL / ComfyUI：ControlNet depth 锁楼梯与楼层关系最有效；色彩按空间分块写进 positive，不要整体调色；negative 单独保留上列。
- Runway / Kling / Sora / Veo：首帧先给"人在下、空间在上"的构图，只写一种横移扫描；5–7 秒、24fps；灾难段再单独生成手持素材，不要在同一段里混两种运动。
