---
name: iwai-shunji
title: 岩井俊二 Shunji Iwai
style_file: ../directors/iwai-shunji.md
---

## 风格锚点
Cinematic film still, a snowfield at dusk, a girl in a dark coat standing far off, backlit by a low overexposed sky with one specific pale sun, 35mm wide, vast negative space, cream-white and faded pink memory palette, blown highlights, a lace curtain in the near foreground, 1.66:1, soft film grain, a letter read to someone absent, tenderness already turning into recollection.

## 图像提示
- 主体 / 场景：a girl standing alone in a snowfield or wheat field; a hand holding an envelope near a window; a classroom lit by green fluorescent tubes; a figure cycling past a corridor window; a CRT monitor or miniDV camera on a desk.
- 景别 / 构图：extreme wide landscape or extreme close-up of a hand, ear, envelope; no stable medium two-shot; composition either leaves vast empty space or pushes the object to the frame edge.
- 镜头 / 焦段：24–35mm for snowfield and wheat field; 85–135mm for hands, ears, envelopes; long lens isolates the media object.
- 光线：backlight first; window, snowfield, sea, corridor window as a specific source; highlights may blow out, but never without a source.
- 色彩：memory set — cream white, pale green, faded pink; present set — cold cyan, fluorescent green, screen blue; do not blend the two in one shot.
- 材质：lace curtain, plastic raincoat, CRT monitor, miniDV tape, school desk, snow.
- 画幅：1.85:1; memory passages may be 1.66:1.

## 视频提示
- 镜头运动（只选一种）：slow lateral tracking at walking pace alongside the subject; no push-in, no handheld unless the shot is explicitly DV.
- 主体运动：a girl walks through snow, breath visible, holding a letter; a hand turns an envelope; a figure cycles away from camera; no running in slow motion.
- 时长 / 帧率 / 运动模糊：6–8 seconds, 24fps, gentle natural blur, no slow motion, no speed ramp.

## 负面提示
no backlight with cherry blossoms, white dress and piano all at once, no overexposure without a specific light source, no face-to-face confession spoken to completion, no push-in on a reunion, no piano while a character cries, no lyrical score over violence, no clean bright classroom, no slow-motion running or falling sakura, no sweet unrequited love without misrecognition or cost, no adult explaining youth.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：cream white, pale green, faded pink, or cold cyan and screen blue / 24–35mm wide, 85–135mm detail, 1.85:1 or 1.66:1 / backlight with a named source, blown highlights allowed / vast negative space or extreme close-up, no medium two-shot / lace, plastic raincoat, CRT, miniDV.
- 禁止漂移：no modern smartphone, no crisp 4K digital skin, no drone snowscape, no warm golden filter, no music-video gloss.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 200`；用真实雪景或胶片扫描做 `--sref`；负面压 `cherry blossom, white dress, piano, soft focus`，避免四件套同时出现。
- SDXL / ComfyUI：固定逆光 prompt 块 + 轻颗粒 LoRA；ControlNet 锁大远景留白或手部特写；不要加日系美颜 LoRA。
- Runway / Kling / Sora / Veo：首帧为雪原或窗边手部特写，只给 slow lateral tracking；6–8 秒，24fps；重逢用固定全景，不要推近。
