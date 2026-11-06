---
name: apichatpong-weerasethakul
title: 阿彼察邦·韦拉斯哈古 Apichatpong Weerasethakul
style_file: ../directors/apichatpong-weerasethakul.md
---

## 风格锚点
Cinematic film still, tropical Thailand, humid moss-green jungle near black, pale fluorescent hospital green, single practical light at night, no fill on faces, medium-long shot, figure at one side of frame, foreground tree leaves or fan blade, empty sky or ceiling above, head cropped, static camera at seated height, 35–50mm, mosquito net and wet tile, half the face lost in darkness.

## 图像提示
- 主体 / 场景：a middle-aged man lying awake in a hospital bed; a woman on a plastic chair at the edge of a jungle clearing; a family eating at a folding table with one empty chair.
- 景别 / 构图：medium-long shot, figure pushed to one side or deep in frame, foreground leaves, curtain or fan blade, empty sky or ceiling filling the top, head often cropped.
- 镜头 / 焦段：35–50mm prime, minimal compression; wide angle only for a jungle wide.
- 光线：available light — overcast daylight, fluorescent tube, one lamp at night; expose for the room, no side fill, half the face may disappear.
- 色彩：humid moss green, near-black jungle, pale fluorescent hospital green, night black; no teal-orange, no saturated peacock green.
- 材质：mosquito net, old wood, plastic chair, moisture, tile, hospital curtain.

## 视频提示
- 镜头运动（只选一种）：static tripod at seated or bed height, no follow.
- 主体运动：people enter and leave the frame, sit, sleep, wait; the camera does not chase them.
- 时长 / 帧率 / 运动模糊：20–40 seconds, 24fps, no motion blur, no speed ramp.

## 负面提示
no postcard tropical filter, no saturated peacock green, no teal-and-orange grade, no mystical glow, no shot-reverse-shot, no push-in on emotion, no fast-cut dream montage, no exoticized jungle, no symbolic hospital set, no character explaining a dream or a past life.

## 一致性锚点
- 色彩：humid moss green / near-black jungle / pale fluorescent hospital green, low saturation.
- 镜头：35–50mm.
- 光线：available light, no side fill, one practical source at night.
- 构图：medium-long, figure off to one side, foreground obstruction, empty sky or ceiling, head cropped.
- 材质：mosquito net, wet tile, old wood, plastic chair.
- 禁止漂移：no drone aerial, no LED white, no clean digital skin, no travel-brochure saturation, no symmetrical centered hero shot.

## 平台备注
- Midjourney：`--style raw --stylize 150`；用一张实景静帧做 `--sref`，不要加 “cinematic lighting” 之类美化词。
- SDXL / ComfyUI：固定 prompt 块打头；用 ControlNet depth 锁前景树叶/风扇遮挡；不要套 HDR 或高对比 LoRA。
- Runway / Kling / Sora / Veo：先给首帧图，只写 static camera，20–40 秒或平台上限，24fps，不加运动模糊与变速。
