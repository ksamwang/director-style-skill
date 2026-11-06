---
name: kleber-mendonca-filho
title: 小克莱伯·门东萨 Kleber Mendonça Filho
style_file: ../directors/kleber-mendonca-filho.md
---

## 风格锚点
Cinematic film still, contemporary Recife, a middle-class living room seen from a corner, white walls and blue tile, mango-green louvered shutters, old wood, hard noon light cutting through the blinds, one figure held at the edge of the frame, the rest left to an empty corridor, doorframe within doorframe, 35mm lens, static camera, faint grain, ordinary surfaces under inspection, threat kept off-screen.

## 图像提示
- 主体 / 场景：a retired nurse standing in her own apartment doorway; a residential street with mango trees, low walls, a dog, an intercom panel; a removal van parked outside, never framed as spectacle.
- 景别 / 构图：medium-wide to medium; eye level; frame-within-frame through door or window; figure pushed to one side, the other side left empty for corridor or street; no centered hero.
- 镜头 / 焦段：28–50mm; 35mm for interiors; avoid long telephoto; deep enough focus to read the room.
- 光线：natural window light plus practical sources; hard noon light allowed and not softened; no fill that flattens the room.
- 色彩：white walls, tile blue, mango green, old wood; ungraded, no filter, mid saturation.
- 材质：terrazzo floor, louvered shutters, plastic chairs, cassette tapes, old records, worn paper documents.

## 视频提示
- 镜头运动（只选一种）：static tripod camera held in a room corner; no handheld.
- 主体运动：people walk out of frame and back in; someone pauses, listens to an off-screen sound, continues a household task; a dog crosses the background.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, minimal motion blur, no speed ramps.

## 负面提示
no voice-over explaining history, no villain arriving with a motive, no musical sting before violence, no handheld shake for tension, no saturated postcard Recife, no folkloric score, no title cards for time and place, no jump-scare sound design, no drone establishing shot, no clean digital showroom interiors, no hero winning a face-to-face confrontation.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：white, tile blue, mango green, old wood / 35mm, / natural plus practical, hard noon allowed / eye-level static, door or window frame, figure at one edge / terrazzo, louvers, plastic, magnetic tape.
- 禁止漂移：no modern glass towers, no LED white, no clean digital skin, no drone aerials, no warm nostalgia sepia.

## 平台备注
- Midjourney：`--style raw --stylize 150`；用一张真实公寓或街道照片做 `--sref`，不要用电影海报。
- SDXL / ComfyUI：固定 prompt 块 + 轻颗粒 LoRA；ControlNet depth 锁门框/窗框套框；negative 里保留 sound-design 类词，防止模型加惊悚光效。
- Runway / Kling / Sora / Veo：首帧为静止室内全景，只给 static camera；6–8 秒，24fps；威胁用画外声提示，不要生成入室镜头。
