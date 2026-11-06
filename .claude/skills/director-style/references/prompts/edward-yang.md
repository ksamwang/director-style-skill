---
name: edward-yang
title: 杨德昌 Edward Yang
style_file: ../directors/edward-yang.md
---

## 风格锚点
Cinematic urban film still, 1990s Taipei office or apartment, fixed wide-angle deep-focus shot, figures separated by glass partitions and window frames, cool grey-blue fluorescent light, flat overhead illumination, architectural lines cutting across faces, symmetrical framing, 1.85:1, analytic, precise, no handheld, city as grid.

## 图像提示
- 主体 / 场景：a family at a dinner table in a glass-walled apartment; office workers divided by partitions; a teenager in a school corridor; two people in the same frame but unable to reach each other.
- 景别 / 构图：medium-wide and full shot, symmetrical, framed, deep focus; architectural lines slice across the face; person and space carry equal weight.
- 镜头 / 焦段：wide-angle, deep depth of field, static.
- 光线：flat fluorescent overhead; domestic warmth flattened by daylight tubes; no soft warm key.
- 色彩：cool grey-blue for offices, hospitals and night; warm only at home but held flat; no unified midtone.
- 材质：glass, curtain wall, corridor tile, neon, office partitions.
- 画幅：1.85:1.

## 视频提示
- 镜头运动（只选一种）：fixed camera, one slow lateral pan to re-frame the group; never a push-in or handheld.
- 主体运动：people talking, arguing, moving between rooms, sitting in separate compartments; restrained gestures, no big emotional display.
- 时长 / 帧率 / 运动模糊：8–15 seconds, 24fps, no stylized motion blur.

## 负面提示
no handheld shake, no warm nostalgia filter, no postcard city skyline, no score judging the characters, no sentimental close-up, no content-free poetic dialogue, no coincidence resolving threads, no violence as spectacle, no shallow focus, no soft warm fill.

## 一致性锚点
- 色彩：cool grey-blue, fluorescent-flat; warm domestic light held down.
- 镜头：wide-angle, deep focus, 1.85:1.
- 光线：flat overhead fluorescent, visible fixtures, minimal fill.
- 构图：symmetrical, glass and frame divisions, lines crossing the face, person and space equal.
- 材质：glass, curtain wall, corridor tile, neon.
- 禁止漂移：no handheld, no shallow depth, no warm grade, no glass-tower glamour, no emotional close-up.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 100`；用玻璃隔断办公室的实拍参考做 `--sref`，不要用城市夜景明信片。
- SDXL / ComfyUI：用 ControlNet depth/canny 锁玻璃隔断与建筑线条；negative 排除 handheld、warm filter、shallow focus。
- Runway / Kling / Sora / Veo：首帧用固定广角群像，只给固定机位或一次缓慢横移，8–15 秒，24fps；不要推近。
