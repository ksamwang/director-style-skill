---
name: christopher-nolan
title: 克里斯托弗·诺兰 Christopher Nolan
style_file: ../directors/christopher-nolan.md
---

## 风格锚点
Cinematic 65mm IMAX film still, a lone figure centered on the axis of a vast concrete chamber, steel-blue and charcoal palette with a single warm amber practical, hard directional overcast light, deep focus, fine 65mm grain, symmetrical composition, oppressive negative space above, monumental scale, cold and restrained, no digital gloss.

## 图像提示
- 主体 / 场景：a man in a charcoal suit alone in a vast concrete test chamber; a soldier crossing an empty beach under an overcast sky; a rotating corridor with one figure at its center.
- 景别 / 构图：extreme wide establishing scale, then close-up on eyes or hands; centered symmetry, figure on the central axis, large negative space above; no casual rule-of-thirds.
- 镜头 / 焦段：65mm IMAX; 24–40mm wide for space, 75–100mm for faces and hands; deep focus, no wide-angle face distortion.
- 光线：single hard directional source — overcast sky, window, practical; deep shadows retained; no fill light, no even studio lighting.
- 色彩：steel blue, charcoal, black; one warm amber exception for fire, home or memory; no teal-and-orange grade.
- 材质：concrete, glass, water, snow, wool suiting, real smoke and dust; fine 65mm grain, no digital gloss.
- 画幅：1.43:1 for spectacle, 2.39:1 for dialogue.

## 视频提示
- 镜头运动：slow dolly in, one direction only; no handheld, no whip pan.
- 主体运动：minimal — a man walks, stops, turns his head; no broad gesture.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, minimal motion blur; hold the last frame.

## 负面提示
no handheld camera shake, no dutch angle, no warm nostalgia filter, no teal-and-orange grade, no soft dreamy focus, no clean CGI gloss, no neon, no slow-motion cliché, no casual rule-of-thirds, no bright even lighting.

## 一致性锚点
- 色彩：steel blue / charcoal / black, one amber accent, low saturation, high contrast.
- 镜头：65mm IMAX look, 24–40mm wide, 1.43:1 or 2.39:1.
- 光线：single hard directional source, deep retained shadows.
- 构图：centered symmetry, figure on axis, negative space above.
- 材质：concrete, glass, water, wool, fine 65mm grain.
- 禁止漂移：no modern LED white, no clean glass towers, no digital skin, no drone-shot gloss.

## 平台备注
- Midjourney：`--ar 1.43:1 --style raw --stylize 150`；用真实 IMAX 静帧做 `--sref`，避免模型自动加暖色。
- SDXL / ComfyUI：固定 prompt 块；用 ControlNet depth 锁中轴对称与人物轴线；negative 里保留 no fill light。
- Runway / Kling / Sora / Veo：从首帧图开始，只给 slow dolly in，4–6 秒，24fps；不要同时写推轨和手持。
