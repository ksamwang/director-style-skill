---
name: johnnie-to
title: 杜琪峰 Johnnie To
style_file: ../directors/johnnie-to.md
---

## 风格锚点
Cinematic crime film still, cold blue Hong Kong parking garage or warehouse, wide-angle deep-focus full shot, five figures distributed evenly like chess pieces, hard practical light with large dark areas, columns and exits dividing the frame, black-white-grey clothing, 2.39:1, precise geometry, stillness before violence, no atmosphere for its own sake.

## 图像提示
- 主体 / 场景：five bodyguards spread across a mall atrium or car park; a negotiation around a table in a warehouse; a lone cop at the mouth of a stairwell; each figure holds a readable position.
- 景别 / 构图：full shot and medium, wide-angle, deep focus; columns, doors, cars and mirrors split the space; every exit visible before the gunshot.
- 镜头 / 焦段：wide-angle, deep depth of field, static.
- 光线：hard practical light, large dark areas; neon only as accent.
- 色彩：one temperature per space — cold blue, warm brown or warm gold; never mixed within a scene.
- 材质：concrete car park, warehouse steel, cha chaan teng tile, neon, rain-slick asphalt.
- 画幅：2.39:1.

## 视频提示
- 镜头运动（只选一种）：locked-off wide shot holding all positions, one sudden push-in when someone is about to draw; no handheld.
- 主体运动：minimal — a shift of stance, a glance, a nod; gunfire erupts for two seconds, then everyone stops and the space is left uncleared.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, no slow motion.

## 负面提示
no handheld gunfight, no psychological flashback, no long motive speeches, no warm nostalgia filter, no slow-motion showmanship in action, no background-only extras, no score cueing tension, no coincidence rescue, no mixed color temperatures within a scene, no shallow depth of field hiding positions.

## 一致性锚点
- 色彩：one temperature per location — cold blue, warm brown, warm gold; neon accent only.
- 镜头：wide-angle, deep focus, 2.39:1.
- 光线：hard practical light, large dark areas, minimal fill.
- 构图：chessboard group framing, columns and exits dividing the space, all positions legible.
- 材质：concrete, steel, tile, neon, wet asphalt.
- 禁止漂移：no handheld camera, no shallow-focus blur, no warm filter, no extra characters without a position.

## 平台备注
- Midjourney：`--ar 2.39:1 --style raw --stylize 150`；用一张停车场或仓库的广角实景做 `--sref`，强调站位而非气氛。
- SDXL / ComfyUI：用 ControlNet depth 锁柱列与出口；negative 排除 handheld、shallow focus、warm filter。
- Runway / Kling / Sora / Veo：首帧用全景群像，只给固定机位；爆发靠人物动作与剪辑，6–10 秒，24fps，不用慢镜。
