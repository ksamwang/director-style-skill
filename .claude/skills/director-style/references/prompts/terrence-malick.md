---
name: terrence-malick
title: 泰伦斯·马力克 Terrence Malick
style_file: ../directors/terrence-malick.md
---

## 风格锚点
Cinematic film still, backlit natural light, sun through leaves, low horizon with sky and tree canopy filling the upper two thirds, human figure small in the lower third, 25–40mm wide angle, low camera close to grass height, drifting handheld frame, wheat gold, muddy river green, faded military olive, dust and leaf texture, 2.39:1, reverent, weight of scale.

## 图像提示
- 主体 / 场景：a lone figure crossing a wheat field or riverbank; a child half-hidden behind tall grass; soldiers walking a ridge; a room with one window and an empty chair.
- 景别 / 构图：medium wide to extreme wide; no reverse-shot close-up; human in the lower third, low horizon, environment established before the person enters; no centered hero.
- 镜头 / 焦段：25–40mm wide angle, foreground grass enlarged and people made small; long lens only when a figure is isolated.
- 光线：natural daylight and window light only; backlight preferred so the contour arrives before the face; no fill, overcast stays overcast.
- 色彩：wheat gold, muddy green, faded uniform olive, earth brown; weather decides saturation, no warm grade added.
- 材质：grass, dust, water, sweat, leaves, skin, weathered wood; no clean walls or polished props.
- 画幅：2.39:1.

## 视频提示
- 镜头运动（只选一种）：low handheld drift, slightly weightless, turning toward what the subject is about to look at before they look.
- 主体运动：walking, digging, washing, waiting; low-intensity, unperformed; no big emotional display.
- 时长 / 帧率 / 运动模糊：5–8 seconds, 24fps, soft handheld motion blur; the decisive action stays offscreen and the camera keeps drifting after the person stops.

## 负面提示
no symmetrical composition, no even studio lighting, no clean seamless background, no full-face close-up at the emotional peak, no explanatory flashback, no landscape-postcard wallpaper, no voice-over restating what is on screen, no slow-motion violence as spectacle, no warm nostalgia grade, no centered hero framing.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：以下五项为全片锁定值，逐镜不重设。
- 色彩：wheat gold, muddy green, faded olive, earth brown, low saturation by weather.
- 镜头：25–40mm, wide, deep space, 2.39:1.
- 光线：natural sun or window light, backlit, unmodified contrast.
- 构图：low camera near ground, low horizon, human small in lower third.
- 材质：grass, dust, water, sweat, skin, film grain.
- 禁止漂移：no drone aerial, no golden-hour postcard filter, no clean digital sharpness, no modern architecture, no centered symmetrical portrait.

## 平台备注
- Midjourney：`--ar 2.39:1 --style raw --stylize 150`；用一张自然光广角静帧做 `--sref`，避免默认补光和暖色滤镜。
- SDXL / ComfyUI：固定风格块 + 胶片颗粒 LoRA；ControlNet depth 锁低地平线与人物下三分之一位置。
- Runway / Kling / Sora / Veo：先给首帧，只写一种 handheld drift，5–8 秒、24fps；不要同时写推近和环绕。
