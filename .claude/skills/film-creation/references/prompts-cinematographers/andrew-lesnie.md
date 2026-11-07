---
name: andrew-lesnie
title: 安德鲁·莱斯涅 Andrew Lesnie
style_file: ../cinematographers/andrew-lesnie.md
---

## 风格锚点
Cinematic fantasy epic still, extreme wide deep-space composition, tiny figures and horses as scale reference, low horizon beneath towering mountains, 18–24mm wide lens, crane and aerial scale, low-angle natural sunlight, god rays through cloud gaps, green-gold moss and honey light against cool grey stone shadows, volumetric mist, forced-perspective depth, 35mm grain, mythic, immense, lived-in.

## 图像提示
- 主体 / 场景：a small company of travelers crossing a vast valley beneath mountains; a lone rider on a ridge; the terrain is the subject and the people are its measure.
- 景别 / 构图：extreme wide and wide, low horizon, tiny figures placed against a readable landmark, foreground rock or branch, layered ridges into mist; aerial or low-angle.
- 镜头 / 焦段：18–24mm wide to establish, 75–200mm to compress mountains; deep focus, forced-perspective scale.
- 光线：low natural sun, side-backlight, volumetric shafts through cloud gaps, morning mist, warm highlights and cool green shadows.
- 色彩：moss green, fern green, honey gold, mist grey, rock grey; regional palettes, no unified LUT.
- 材质：wet moss, mud, coarse wool, stone, timber, miniature-set texture.

## 视频提示
- 镜头运动（只选一种）：slow crane rise and lateral move, revealing the full geography.
- 主体运动：the company walks or rides along a ridge; mist drifts through the valley.
- 时长 / 帧率 / 运动模糊：12–25 seconds, 24fps, natural motion blur, no fast aerial dive.

## 负面提示
no figure filling the frame without scale reference, no telephoto blur erasing the mountain, no flat even daylight, no fast drone fly-through, no fluorescent green grade, no low-angle hero shot for everyone, no CG background without aerial perspective, no rapid cutting, no clean digital fantasy sheen.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：moss and honey palette with cool shadows; 18–24mm establishing lens; low sun and god rays; low horizon with tiny figures; wet moss and stone.
- 禁止漂移：no studio lighting, no teal-orange LUT, no modern architecture, no close-up portrait default, no video-game rendering.

## 平台备注
- Midjourney：`--style raw --stylize 150`；用真实山谷航拍做构图参考，避免模型生成游戏概念图。
- SDXL / ComfyUI：depth ControlNet 锁前景—中景—远景三层；negative 排除 fast drone 与 fluorescent green。
- Runway / Kling / Sora / Veo：首帧给大全景，只写一种 crane 上升横移；12–25 秒，24fps，不叠加俯冲或甩镜。
