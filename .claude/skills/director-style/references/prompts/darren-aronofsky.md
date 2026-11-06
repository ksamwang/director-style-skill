---
name: darren-aronofsky
title: 达伦·阿罗诺夫斯基 Darren Aronofsky
style_file: ../directors/darren-aronofsky.md
---

## 风格锚点
American psychological body film, bleached high-contrast image, 1.85:1, hip-height handheld camera pressed close to skin, 24mm wide-angle distortion, overhead fluorescent light, blown highlights and crushed blacks, sweat, pores, glass, concrete, one accent color of red or pink, coarse 16mm grain, obsessive, airless, subjective.

## 图像提示
- 主体 / 场景：a dancer's bare shoulder and ribcage in a backstage mirror; a wrestler's taped hands; a face half-lit in a bathroom; no full room.
- 景别 / 构图：extreme close-up on skin, pores, sweat, a needle or a wound; face pushed to the frame edge; mirror doubling the body; no negative space.
- 镜头 / 焦段：18–28mm wide-angle close to the face, 50–85mm for extreme detail; visible distortion at the edges.
- 光线：hard overhead fluorescent or a single bare bulb; blown highlights; blacks crushed with no fill.
- 色彩：bleached, desaturated base plus one accent — blood red, ballet pink, or ochre; no warm nostalgia.
- 材质：sweat, skin, hair, glass, needles, feathers, blood, cracked concrete.
- 画幅：1.85:1；《黑天鹅》《母亲！》2.39:1.

## 视频提示
- 镜头运动：handheld follow at hip height, breathing shake, no stabilization; the camera stays inside the character's space.
- 主体运动：repetitive training or scratching; the body moves faster than the camera can settle; one small flinch at the end.
- 时长 / 帧率 / 运动模糊：4–6 seconds, 24fps, slight shutter smear on fast movement.

## 负面提示
no soft beauty lighting, no clean skin, no objective wide shot explaining the location, no slow-motion lyricism, no moralizing caption, no healthy resolution, no gimbal smoothness, no warm filter, no symmetrical composition, no digital plastic texture.

## 一致性锚点
- 色彩：bleached high contrast, one accent color, crushed blacks.
- 镜头：18–28mm wide-angle close, 50–85mm detail, 1.85:1.
- 光线：hard overhead source, blown highlights, no fill.
- 构图：centered pressure, face at frame edge, mirror doubling.
- 材质：sweat, skin, glass, needle, blood, concrete.
- 禁止漂移：no softbox glow, no clean digital skin, no drone shot, no warm sunset, no symmetrical beauty frame.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 100`；用皮肤/后台特写做 `--sref`；避免“cinematic”“beautiful”这类词。
- SDXL / ComfyUI：正面锁“extreme close-up, sweat, pores, hard overhead light”；负面提示加重 no soft lighting / no clean skin；用 ControlNet depth 锁贴脸距离。
- Runway / Kling / Sora / Veo：首帧给极特写，只写一种“handheld follow”，4–6 秒，24fps；把“呼吸式抖动”写成 camera shake amplitude，不写“紧张”。
