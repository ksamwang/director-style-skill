---
name: sergei-eisenstein
title: 谢尔盖·爱森斯坦 Sergei Eisenstein
style_file: ../directors/sergei-eisenstein.md
---

## 风格锚点
Revolutionary silent-film still, hard black-and-white blocks with no soft midtones, low angle raising an officer into a monument, overhead flattening a crowd into a pattern, strong diagonal lines and repeated rows of backs and raised fists, high-contrast hard light with clear silhouettes, stone steps, iron armor, flags, boots, wide lens and long lens cut against each other, 1.33:1, collective, graphic, argumentative.

## 图像提示
- 主体 / 场景：a crowd of sailors, workers, peasants or insurgents; an officer, priest or bureaucrat as a legible social type; an individual shown only as a representative of a class.
- 景别 / 构图：hard cut between extreme wide (rows of bodies) and extreme close-up (a boot, a monocle, a nape); no medium-shot transition; diagonals, low angle or repeated backs; space segmented into steps, deck, bridge, factory gate, with who is above and who is below instantly readable.
- 镜头 / 焦段：wide angle turns the crowd into a pattern; long lens flattens a face into a type; the focal-length change itself is an edit, so do not unify it.
- 光线：high-contrast hard light, clear silhouettes, the face often reduced to an outline.
- 色彩：black and white; white and black are the camps, no soft middle tone.
- 材质：stone steps, iron armor, flags, boots, wheels — hard, heavy, trampled.
- 画幅：1.33:1。

## 视频提示
- 镜头运动（只选一种）：mechanical lateral tracking, like a military review — or a locked-off frame that lets the action complete inside it; no handheld, no improvisation.
- 主体运动：masses moving in formation, repeated crowd choreography, a hand or boot entering the frame as a graphic event.
- 时长 / 帧率 / 运动模糊：1–4 seconds per shot, cutting faster as the sequence builds; 24fps, no motion blur, no smoothing.

## 负面提示
no continuity editing hiding the cuts, no psychological close-up, no voice-over inner monologue, no neutral camera position, no undifferentiated crowd background, no music-video fast cutting without a third meaning, no soft midtones, no individual emotion resolving history, no evenly timed shots, no handheld realism, no color, no naturalistic daylight.

## 一致性锚点
- 色彩：black and white, hard blocks, no soft midtone.
- 镜头：wide and long lenses hard-cut, no unified focal length, 1.33:1.
- 光线：high-contrast hard light, silhouette readable.
- 构图：diagonal, low angle or overhead, repeated rows, local close-up replacing the wide.
- 材质：stone, iron, flags, boots, wheels.
- 禁止漂移：no color, no soft focus, no handheld, no centered individual portrait, no modern crowd, no digital gloss, no even lighting.

## 平台备注
- Midjourney：`--ar 133:100 --style raw --stylize 50`；用一张高对比黑白群众构图做 `--sref`；单张图无法生成“碰撞”，要成对生成再并置。
- SDXL / ComfyUI：高对比黑白 LoRA + ControlNet canny 锁对角线、队列和阶梯；分别生成“全景队列”和“局部特写”两组固定 seed 图，剪辑时再碰撞。
- Runway / Kling / Sora / Veo：每个镜头单独生成，运镜只写 `locked-off` 或 `mechanical lateral track`，1–4 秒，24fps；碰撞意义在剪辑台完成，不要指望单条视频生成蒙太奇。
