---
name: andrei-tarkovsky
title: 安德烈·塔可夫斯基 Andrei Tarkovsky
style_file: ../directors/andrei-tarkovsky.md
---

## 风格锚点
Contemplative film still, low horizon with a small figure pushed to the frame corner and the sky taking most of the image, slightly low stable camera, 35mm or 50mm, desaturated brown-green present-day palette, natural and practical light with layered shadows, peeling walls, mossy timber, standing water, ruins, faint rain and fire, no clean modern surfaces, patient, sacred, time visible inside the frame.

## 图像提示
- 主体 / 场景：a walker — guide, monk, painter, poet or child — crossing a zone and carrying a promise; a mother or wife as a doorway into memory; a room where water has entered.
- 景别 / 构图：either extreme wide with the figure reduced to a dot, or extreme close-up on wall, earth or water; medium shots are rare because they organize relationships for the viewer; low horizon, figure off in a corner, sky and earth occupying most of the frame; the center belongs to time, not to the person.
- 镜头 / 焦段：35mm and 50mm, no long-lens separation of figure from landscape.
- 光线：natural and practical light, shadow detail retained, no fill, no theatrical hard light.
- 色彩：desaturated brown-green for the present; memory segments switch to sudden color or monochrome with a hard boundary and no transition cue.
- 材质：water, fire, wet walls, mossy wood, ruins; the environment changes before the person does.

## 视频提示
- 镜头运动（只选一种）：very slow lateral or crane movement, barely perceptible, able to drift from the figure to the landscape and back within one unbroken take; no handheld.
- 主体运动：waiting, standing, walking slowly; water rises, fire moves, wind crosses the room — the environment acts first.
- 时长 / 帧率 / 运动模糊：20–60 seconds in one take, 24fps, no motion blur, no speed ramp.

## 负面提示
no montage metaphor, no symbolic explanation dialogue, no music filling every gap, no long take without time pressure or waiting, no clean designer modern space, no color-filter flashback, no whip pan, no running follow shot, no subjective showiness, no clear redemption ending, no fast cutting, no symmetrical centered portrait.

## 一致性锚点
- 色彩：desaturated brown-green present / sudden color or monochrome memory, hard boundary.
- 镜头：35mm or 50mm, or by segment.
- 光线：natural and practical, layered darks, no fill.
- 构图：low horizon, small figure in a corner, sky and earth dominant.
- 材质：water, fire, wet walls, mossy wood, ruins.
- 禁止漂移：no teal-orange grade, no clean modern surfaces, no drone shot, no fast handheld, no digital skin, no centered hero composition.

## 平台备注
- Midjourney：``raw --stylize 200`；用一张低地平线、人物很小的风景静帧做 `--sref`，不要用奇幻概念图。
- SDXL / ComfyUI：现实段与记忆段分成两个固定 prompt 块和两套色板；ControlNet depth 锁低地平线和人物角落位置；negative 写 `clean, modern, glossy, centered, fast`。
- Runway / Kling / Sora / Veo：首帧给低地平线全景，运镜只写 `very slow lateral drift`，单镜 20–60 秒，24fps；让水、火、风先动，人物后动。
