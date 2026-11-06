---
name: stanley-kubrick
title: 斯坦利·库布里克 Stanley Kubrick
style_file: ../directors/stanley-kubrick.md
---

## 风格锚点
Cinematic film still, one-point perspective, figure pinned on the central axis, 18–25mm wide angle, symmetrical corridor or room, ceiling and floor both visible, flat even practical light, controlled contrast, red white and blue blocks in the dream-logic films, carpet, mirror, geometric furniture, 1.85:1, cold, measured, institutional.

## 图像提示
- 主体 / 场景：a writer standing alone at the end of a hotel corridor; a soldier under a tiled barracks ceiling; an astronaut in a white cylindrical module. The room is measurable and the person is an object inside it.
- 景别 / 构图：wide and frontal medium; strict one-point perspective, subject on the axis, symmetrical walls, ceiling and floor both in frame; asymmetry appears only when the order is already broken.
- 镜头 / 焦段：18–25mm wide angle, frontal, no long-lens compression; occasional high angle turning the room into a floor plan.
- 光线：flat even practical light or clean natural light, controlled ratio; no dramatic backlight, no warm glow.
- 色彩：blocks of red, white and blue in the dream-logic films; elsewhere neutral, never a warm filter.
- 材质：patterned carpet, mirror, polished metal, geometric furniture, corridor walls; nothing organic or hand-soft.
- 画幅：1.85:1 (2.20:1 for the space film, 1.66:1 for the period film).

## 视频提示
- 镜头运动（只选一种）：constant-speed straight dolly forward along the axis — one direction, one velocity, no acceleration or easing.
- 主体运动：the figure walks or stands without deviation from the centre line; extras move in formation; the body stays rigid while tension rises.
- 时长 / 帧率 / 运动模糊：12–20 seconds, 24fps, zero motion blur, perfectly steady; the move must feel mechanical.

## 负面提示
no handheld, no whip pan, no improvised zoom, no asymmetrical composition to signal madness, no warm nostalgic filter, no psychological flashback, no redemption ending, no fast cutting to hide space, no gothic horror shadow, no fisheye, no naturalistic messy framing, no Dutch angle, no lens flare, no organic hand-made texture.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：red white blue blocks or neutral, 18–25mm frontal at 1.85:1, flat even practical light, one-point perspective with the subject on axis, carpet and geometric furniture.
- 禁止漂移：no teal-orange grade, no handheld shake, no drone, no asymmetric art framing, no retro grain, no soft bokeh, no modern minimal white interior.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 100 --no handheld, bokeh, warm`；对称构图靠 `symmetrical`、`one-point perspective`、`on the central axis` 三个词，不靠 `--tile`。
- SDXL / ComfyUI：ControlNet canny 或 mlsd 锁走廊的消失线；固定 seed 保证同一空间的多镜头一致；negative 里必须出现 `asymmetry` 与 `film grain`。
- Runway / Kling / Sora / Veo：首帧是正面中轴；只写 `constant-speed dolly forward`，明确 `no easing, no acceleration`；时长 12 秒以上，让机械感成立。
