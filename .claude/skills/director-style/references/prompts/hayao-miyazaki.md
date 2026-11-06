---
name: hayao-miyazaki
title: 宫崎骏 Hayao Miyazaki
style_file: ../directors/hayao-miyazaki.md
---

## 风格锚点
Cinematic animation still, hand-drawn cel animation over watercolor backgrounds with visible paper grain, saturated layered greens and blues each with its own color temperature, deep receding space, wind bending grass hair cloth and smoke in one direction, soft natural daylight with cloud shadows moving across the land, an inhabitable cluttered interior of wood iron and steam, hard clean foreground lines, 1.85:1, curious, warm, alive.

## 图像提示
- 主体 / 场景：a girl on a rooftop above a sprawling hand-painted town; a boiler room packed with pipes, coal and steam; a small aircraft over a green valley; a forest spirit at the edge of tall grass.
- 景别 / 构图：extreme wide establishing first, then medium; deep space with foreground, midground and background readable; wind unifies every element; interiors cluttered and lived-in.
- 镜头 / 焦段：24–35mm equivalent wide, no wide-angle distortion on faces; tighter lens only for a face.
- 光线：natural daylight, cloud shadows drifting across the ground, no flat uniform light.
- 色彩：saturated but layered, separate color temperature for sky and grass; watercolor washes, no even digital gradient.
- 材质：watercolor paper grain, wood, iron, steam, cloth, hand-painted foliage.
- 画幅：1.85:1.

## 视频提示
- 镜头运动（只选一种）：one long lateral move that reveals the landscape instead of cutting; or a low glide over grass and rooftops; no shaky handheld.
- 主体运动：wind moves hair, grass, smoke and flags together; flight with weight and inertia, clumsy takeoff and landing; running with clear direction.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps, slight smear on fast flight.

## 负面提示
no 3D-rendered smoothness replacing hand-drawn lines, no uniform gradient skies, no photoreal foliage, no villain monologue justifying himself, no rapid-cut flight montage, no voice-over explaining the world, no protagonist awakening to one-shot the enemy, no postcard nature, no ending that solves everything, no character stating the theme, no lens flare, no shallow depth-of-field bokeh, no vector-clean edges.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：跨镜头锁定以下五项。
  - 色彩：saturated layered greens and blues, one temperature per plane.
  - 镜头：24–35mm equivalent wide, 1.85:1.
  - 光线：natural daylight with moving cloud shadow.
  - 构图：deep space, wide establishing first, a single wind direction across all elements.
  - 材质：watercolor paper, hand-drawn line, wood, iron, steam.
- 禁止漂移：no 3D or CGI sheen, no uniform gradient, no vector-clean edges, no photoreal texture, no modern city, no flat anime filter.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 250`；写 `hand-painted watercolor background, cel animation, visible paper grain`；避免 `3D render, octane, unreal engine`；角色与背景分别用 `--sref`。
- SDXL / ComfyUI：背景与角色分开生成再合成，或用经授权的风格 LoRA；ControlNet depth 锁纵深布局；negative 写 `3d, photoreal, gradient sky, lens flare`。
- Runway / Kling / Sora / Veo：先给完成度高的首帧插画，只给一次横移或贴地滑行，4–8 秒；只让风与人物动，不要要求模型中途重绘建筑。
