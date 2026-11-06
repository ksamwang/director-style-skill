---
name: aki-kaurismaki
title: 阿基·考里斯马基 Aki Kaurismäki
style_file: ../directors/aki-kaurismaki.md
---

## 风格锚点
Deadpan cinematic film still, frontal eye-level static camera, full body held in frame against a single flat-colored wall, blocks of deep green, brick red and mustard yellow, hard practical light from a hanging bulb or window with no fill, old wood, chipped enamel and cigarette ash, 35–50mm lens, 1.85:1, matte muted texture, quietly dignified, no camera movement.

## 图像提示
- 主体 / 场景：a factory worker standing at a bar counter; a cleaner facing the camera in a cheap apartment; two unemployed men sharing a cigarette outside a neon-lit kiosk; a small shopkeeper behind his till.
- 景别 / 构图：medium or medium-full shot, whole body intact and never fragmented, centered or slightly off-center, one flat-colored wall directly behind; frontal eye-level; one wider shot only when the place itself must carry the emotion.
- 镜头 / 焦段：35–50mm, full-body distance, no telephoto compression, no wide-angle distortion.
- 光线：hard, single practical source — hanging bulb, window, neon sign; flat even light at the emotional peak instead of darkening it; no soft fill.
- 色彩：three flat color blocks — deep green, brick red, mustard yellow; no soft gradients, no mixed pastel palette.
- 材质：old wood, chipped enamel, synthetic fabric, cigarette ash; worn but never dirty or squalid.
- 画幅：1.85:1.

## 视频提示
- 镜头运动（只选一种）：static lock-off — the camera never moves and never secretly pushes in; emotion is carried by the pause, not by focal length.
- 主体运动：small gestures only — lighting a cigarette, raising a glass, standing still, a slow turn of the head; no big emotional display, no tears, no embrace.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, no slow motion, minimal motion blur.

## 负面提示
no close-up tears, no emotional close-up, no hidden push-in, no non-diegetic strings, no voice-over explanation, no squalor spectacle, no dirty-poverty close-ups, no warm nostalgic sunlight, no sepia, no handheld camera, no shallow-focus glamour, no cool Nordic desaturation filter, no end-title epilogue, no characters explaining their feelings.

## 一致性锚点
- 色彩：deep green / brick red / mustard yellow, flat blocks, high separation, no soft transitions.
- 镜头：35–50mm, full body, 1.85:1.
- 光线：one hard practical source, flat and even at the peak, no fill.
- 构图：frontal eye-level, subject centered or slightly off against a flat wall, camera static.
- 材质：old wood, enamel, synthetic fabric, ash; worn, not dirty.
- 禁止漂移：no handheld drift, no warm sepia, no cool Nordic desaturation filter, no modern LED, no glass towers, no digital skin, no teary close-up.

## 平台备注
- Midjourney：`--ar 185:100 --style raw --stylize 100`；用一张正面平光的电影静帧做 `--sref`，把色块和静止感一起锁住。
- SDXL / ComfyUI：风格锚点做成固定 prompt 块，加轻微胶片颗粒 LoRA；用 ControlNet depth/pose 锁全身正面站位；negative 里务必写 `cinematic lighting, dramatic shadow, shallow depth of field`。
- Runway / Kling / Sora / Veo：从首帧静帧开始，运镜选 `static`，只让演员做小动作；4–6 秒，24fps，不加慢镜和运动模糊。
