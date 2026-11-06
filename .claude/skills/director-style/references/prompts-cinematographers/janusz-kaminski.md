---
name: janusz-kaminski
title: 扬努什·卡明斯基 Janusz Kamiński
style_file: ../cinematographers/janusz-kaminski.md
---

## 风格锚点
Backlit 35mm film still, a violent overexposed window behind the subject, face falling into silhouette, visible smoke shafts, rim light on hair and shoulders, desaturated grey-green with warm blown highlights, slight handheld imperfection and lens flare, wide 28mm lens, 2.39:1, bleach-bypass texture, grainy, remembered, unstable, subjective.

## 图像提示
- 主体 / 场景：a soldier, a child or a public man standing in front of a blazing window or doorway, smoke drifting through the room.
- 景别 / 构图：medium shot, subject centered and backlit, window or door directly behind the head, edges cropped by frames or smoke.
- 镜头 / 焦段：21–35mm wide-angle, close to the body, slight distortion, shallow atmospheric space.
- 光线：strong backlight 4–6 stops above the face, windows and sky blown out, almost no frontal fill.
- 色彩：desaturated grey-green, earth brown, iron grey, warm clipped highlights.
- 材质：smoke, dust, rain, wet glass, bleach-bypass grain, lens flare.
- 画幅：2.39:1 or 1.85:1.

## 视频提示
- 镜头运动（只选一种）：handheld follow, shoulder height, slight breathing drift.
- 主体运动：a figure walks toward the camera out of the light, then stops; smoke crosses the frame.
- 时长 / 帧率 / 运动模糊：5–12 seconds, 24fps, 45-degree shutter for combat, crisp staccato motion blur.

## 负面提示
no frontal soft light, no correctly exposed windows, no clean smoke-free air, no saturated primary colors, no gimbal-smoothed war, no fill on every face, no slow-motion hero shot, no modern LED flat white, no symmetrical clean composition, no digital-clean skin.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：grey-green desaturation, 21–35mm, backlight with blown window, centered silhouette, smoke and bleach grain.
- 禁止漂移：no front fill, no clean air, no warm teal-orange LUT, no stabilized drone shot, no sharp digital texture.

## 平台备注
- Midjourney：`--ar 2.39:1 --style raw --stylize 120`；用逆光烟雾静帧做 `--sref`，加 `--no soft light`。
- SDXL / ComfyUI：negative 锁 no fill light / no clean air；可用烟雾 ControlNet 或 depth 图层；加 bleach-bypass LoRA。
- Runway / Kling / Sora / Veo：首帧给逆光剪影，只写一种手持跟拍，5–12 秒，24fps，不叠加推轨。
