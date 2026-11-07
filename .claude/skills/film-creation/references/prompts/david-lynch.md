---
name: david-lynch
title: 大卫·林奇 David Lynch
style_file: ../directors/david-lynch.md
---

## 风格锚点
Cinematic film still, 35–50mm, static camera at a doorway or window, subject half-hidden by a curtain or doorframe, practical lamp and television light, deep textured black, velvet, plastic, wood, a single deep red bleeding from the back of the frame, suburban interior that is slightly wrong, dreamlike, watched, uneasy.

## 图像提示
- 主体 / 场景：a woman standing in a suburban living room lit only by a lamp and a television; a man at a doorway looking into a dark hallway; a nightclub stage. The room is normal except for one detail.
- 景别 / 构图：medium and close-up; heavy occlusion — doorframe, curtain, lamp shade cuts the face in half; the camera sits outside the room as a watcher; no clean symmetrical wide.
- 镜头 / 焦段：35–50mm; medium-long lens for the voyeur angle; focus on the plane behind the doorframe.
- 光线：practical sources only — table lamp, neon, car headlight, television glow; darks are very deep but textured; no fill, no key.
- 色彩：deep red and deep blue in dream passages, near-natural elsewhere; red is an alarm from the back of the frame, not decoration; no global filter.
- 材质：velvet, curtain, plastic, varnished wood, blood, cheap carpet, wallpaper.

## 视频提示
- 镜头运动（只选一种）：imperceptibly slow push-in from the doorway — almost static; the frame closes in without announcing itself.
- 主体运动：the figure stands still, then turns the head slightly; someone in the background stops moving; no chase, no sudden gesture.
- 时长 / 帧率 / 运动模糊：15–25 seconds, 24fps, no motion blur; the move should be slower than the viewer expects.

## 负面提示
no explanation of the dream, no jump scare, no flat black without texture, no psychological dialogue, no fully normal lighting in a normal scene, no wall-to-wall score, no grotesque as comedy, no resolved causality, no clean symmetrical sitcom framing, no bright neutral daylight, no neon-everywhere cliché, no red-blue filter over the whole image.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：deep red and blue in dreams, near-natural elsewhere, 35–50mm at , practical lamp and TV light with textured black, doorframe occlusion with half a face, velvet and plastic.
- 禁止漂移：no full-frame colour filter, no jump-cut horror grammar, no daylight flatness, no symmetrical family-sitcom composition, no digital clean skin, no explained ending.

## 平台备注
- Midjourney：`--style raw --stylize 200 --no symmetry, daylight, explained`；`--sref`用《蓝丝绒》室内静帧；提示词保留 `doorframe`、`curtain`、`practical lamp`。
- SDXL / ComfyUI：ControlNet depth 锁门框遮挡，不要用 canny（半张脸会被描成硬边）；negative 单列，`neon`一词要慎用，否则模型会铺满全画面。
- Runway / Kling / Sora / Veo：首帧就是门口视角；只写 `imperceptibly slow push-in`；时长拉到 15 秒以上；不要让它自动产生惊吓节拍。
