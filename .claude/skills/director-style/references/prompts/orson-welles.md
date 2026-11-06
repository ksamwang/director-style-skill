---
name: orson-welles
title: 奥逊·威尔斯 Orson Welles
style_file: ../directors/orson-welles.md
---

## 风格锚点
Cinematic film still, black-and-white hard light, 18–25mm wide angle in deep focus, low camera looking up, ceiling in frame, figures pushed to the edge of the composition, foreground midground and background all occupied, venetian-blind shadows across a face, dark detail retained, baroque, theatrical, a performance staged for empty seats.

## 图像提示
- 主体 / 场景：a newspaper tycoon addressing a half-empty hall; a sheriff and a suspect across a border motel room; a judge in a cavernous office. Space has real depth and a visible ceiling.
- 景别 / 构图：wide and deep-focus medium; figures pressed to the frame edge, large negative space beside them; three planes active at once — a foreground back, a midground speaker, a background reaction.
- 镜头 / 焦段：18–25mm wide angle, deep focus (small aperture, foreground and background both sharp); no shallow bokeh except to isolate one abandoned figure.
- 光线：hard key from one side, venetian-blind or railing shadows cutting across faces, practical lamps, dark areas hold detail; no flat fill.
- 色彩：black and white hard tone; colour work desaturated.
- 材质：ceiling beams, columns, mirrors, stage curtains, polished wood floors; reflections used as another plane.

## 视频提示
- 镜头运动（只选一种）：low-angle crane that rises and travels across the room, moving from one seat of power to another, then stops dead.
- 主体运动：overlapping staging — a foreground figure turns his back and speaks, a midground figure answers, a background figure contradicts with a single gesture.
- 时长 / 帧率 / 运动模糊：8–14 seconds, 24fps, crisp edges, no motion blur; the stop at the end must be abrupt, not eased.

## 负面提示
no flat frontal lighting, no even fill light, no hidden ceiling, no shallow depth of field, no symmetrical centered framing, no single reliable narrator, no polite turn-taking staging, no modern handheld realism, no naturalistic underplaying, no cropped-head close-up, no digital sharpness, no clean white walls.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：black-and-white hard tone, 18–25mm deep focus at , hard side key with blind shadows and detailed darks, low angle with ceiling and edge-pushed figures, beams and mirrors.
- 禁止漂移：no anamorphic flare, no color grade, no soft bokeh, no handheld, no centered hero, no modern glass office.

## 平台备注
- Midjourney：`--style raw --stylize 180 --no bokeh, flat lighting, color`；`--sref`用《公民凯恩》静帧；提示词里必须出现 “deep focus” 与 “ceiling”。
- SDXL / ComfyUI：ControlNet depth 是关键，用来强制前中后三层与低机位；不要用 pose，会把群像压成单人。negative 里单独写 `shallow depth of field`。
- Runway / Kling / Sora / Veo：首帧锁定低角度；只写一种运动 `low-angle crane rising across the room`；结尾加 “camera stops abruptly”，禁止模型自动缓停。
