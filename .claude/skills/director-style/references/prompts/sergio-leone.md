---
name: sergio-leone
title: 塞尔吉奥·莱昂内 Sergio Leone
style_file: ../directors/sergio-leone.md
---

## 风格锚点
Cinematic film still, 2.35:1 anamorphic western, extreme wide landscape with the horizon pressed into the upper third, a tiny figure walking in from far away, then an extreme close-up of sweat and narrowed eyes, low camera near boot height, hard noon sunlight carving wrinkles, dust ochre rust red and faded blue, weathered wood leather and grit, deep focus, no middle distance, 35mm grain, waiting, indebted, still.

## 图像提示
- 主体 / 场景：a lone gunslinger, a bounty hunter, a railroad tycoon, a woman in a dusty town; a desert, a wooden station, a water tower, a windmill turning in dead air.
- 景别 / 构图：only two extremes — extreme wide where the body is a dot on the plain, or extreme close-up where a face fills the scope; no medium-shot dialogue framing. Horizon in the upper third, lateral composition.
- 镜头 / 焦段：25–35mm for the vast landscape, 85–150mm for the face; middle focal lengths almost never. Camera very low, near boot height, looking up so the figure stands against the sky.
- 光线：hard noon sun that carves wrinkles and shadow into the face; interiors lit only by a shaft of window light cutting across the eyes.
- 色彩：dust ochre, rust red, faded blue denim; desaturated and sun-bleached, never vivid primaries.
- 材质：dust, cracked leather, sweat, weathered wood, iron rails, horsehair, flaking paint.
- 画幅：2.35:1 anamorphic.

## 视频提示
- 镜头运动（只选一种）：static extreme wide that holds far too long, then a very slow push in to the eyes and stop.
- 主体运动：a figure walking in from the horizon for a long time; a hand hovering over a holster; a hat brim turning; almost nothing else.
- 时长 / 帧率 / 运动模糊：8–12 seconds, 24fps, minimal motion blur, no slow-motion effect — duration comes from cutting and stillness.

## 负面提示
no fast cutting, no handheld shaky action, no slow-motion duel effects, no clean vivid digital grade, no saturated primary colors, no medium-shot dialogue coverage, no explanatory dialogue, no wall-to-wall score, no modern western pastiche, no trench-coat-cigar-whistle advertising imagery, no moral lesson on revenge, no aerial drone sweep.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：ochre, rust red, faded blue; 25–35mm wide and 85–150mm close-up, nothing between; hard noon key; horizon upper third, low camera; dust, leather, sweat, wood.
- 禁止漂移：no green or teal grade, no clean new props, no modern firearms, no shirtless glamour, no soft portrait lighting, no medium two-shot, no fast zoom.

## 平台备注
- Midjourney：`--ar 2.35:1 --style raw --stylize 200`；用 1960 年代意大利西部片 2.35:1 静帧做 `--sref`，锁住褪色土色。
- SDXL / ComfyUI：positive 里明确 `extreme wide` 或 `extreme close-up` 二选一，不要留给模型折中；用 ControlNet canny 锁地平线高度。
- Runway / Kling / Sora / Veo：首帧用大远景，运动只写 `static hold` 或 `very slow push in`；不要在同一段里要求推近和横摇。
