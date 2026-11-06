---
name: lynne-ramsay
title: 琳恩·拉姆塞 Lynne Ramsay
style_file: ../directors/lynne-ramsay.md
---

## 风格锚点
Sensory film still, camera at a child's height, 50–85mm pressed close to skin, shallow focus melting the background into color blocks, asymmetric frame with half the body cut off and the center left empty, overexposed summer white against dark interior corners, wet green, one piercing red, natural window light with no fill, water, sweat, oil, fogged glass, 1.85:1, tactile, uneasy, memory arriving unannounced.

## 图像提示
- 主体 / 场景：a child at the edge of a canal; a mother's neck and hands at a sink; a figure half-hidden behind a doorframe; an insect on a windowsill; bodies are shown in fragments, never fully staged.
- 景别 / 构图：start on skin, hair, water or an insect before any wide shot; subject pushed to the frame edge, the center left empty — a sink, a door gap, the end of a corridor; half the face cut off by the frame.
- 镜头 / 焦段：50–85mm close to the skin with shallow depth; wide angle only under pressure, never to establish geography.
- 光线：natural light, windows blown out, interiors unlit; the face may sink into shadow; no fill.
- 色彩：overexposed white, wet green, one piercing red used once as a trauma anchor; the red is never spread across the frame.
- 材质：water, sweat, oil, condensation on glass; touch before meaning.
- 画幅：1.85:1；童年段落可用 4:3。

## 视频提示
- 镜头运动（只选一种）：slight handheld drift that freezes without warning — the camera follows breath, then stops dead while the sound continues.
- 主体运动：a repeated daily action — washing, wiping, counting, drying a plate; no crying, no collapse, no hug.
- 时长 / 帧率 / 运动模糊：2–4 seconds, 24fps, slight step-printed motion blur on the moving hand or body.

## 负面提示
no full flashback explaining the trauma, no therapy dialogue ("when I was young…"), no sound cue naming the emotion, no wide shot of an assault, no hug or reconciliation ending, no establishing wide shot of the geography, no children acting cute or innocent, no camera rising to adult eye level, no red filter over the whole image, no dirty-water aesthetic, no symmetrical clean composition.

## 一致性锚点
- 色彩：overexposed white / wet green / a single piercing red.
- 镜头：50–85mm close to skin, shallow focus, 1.85:1 or 4:3.
- 光线：natural window light, blown highlights, dark interior corners, no fill.
- 构图：child height, asymmetric, half the body cut off, empty center.
- 材质：water, sweat, oil, fogged glass.
- 禁止漂移：no adult eye-level camera, no clean symmetrical framing, no red wash, no digital sharpness, no full-body staging, no modern interior.

## 平台备注
- Midjourney：`--ar 185:100 --style raw --stylize 150`（童年段落改 `--ar 4:3`）；用一张皮肤、水或雾面玻璃的微距静帧做 `--sref`。
- SDXL / ComfyUI：用 ControlNet depth 锁“主体偏边、中心留空”的构图；IP-Adapter 只喂色板，不喂完整场景；negative 务必写 `symmetrical, centered, full body, clean background`。
- Runway / Kling / Sora / Veo：首帧给局部特写，运镜只写 `slight handheld drift, then freeze`，2–4 秒，24fps；声音设计先于画面，不要生成完整动作过程。
