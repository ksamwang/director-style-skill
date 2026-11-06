---
name: giuseppe-tornatore
title: 朱塞佩·托纳多雷 Giuseppe Tornatore
style_file: ../directors/giuseppe-tornatore.md
---

## 风格锚点
Cinematic film still, Sicilian memory piece, warm amber and honey light from a projector beam, dust visible in the beam, a crowded village square at dusk, symmetrical frontal composition framed by a cinema doorway, old velvet seats, film reels and plaster walls, 35–50mm, shallow focus, 1.85:1, 35mm grain, tender, nostalgic, elegiac.

## 图像提示
- 主体 / 场景：a boy in a projection booth, an old projectionist threading film, a crowd watching a screen in a village square, a man returning to an empty cinema; the device must be in frame.
- 景别 / 构图：medium-wide to establish the square or cinema as a stage, then close-up on the device — projector lens, reel, photograph, beam; symmetrical frontal composition, frame-within-frame through a doorway, window or screen; no shaky intimate close-up.
- 镜头 / 焦段：35–50mm for the square and crowd; 85–135mm for faces and the device; shallow focus so the background becomes memory.
- 光线：visible projector beam, sunset, bare bulb, candle; dust in the air; warm light must have a source; night scenes deep blue with warm practicals.
- 色彩：amber, honey, burnt orange, olive green, cream; golden but not sepia; no source-less warm filter.
- 材质：film reels, dust, old posters, velvet seats, plaster walls, sea salt, linen, brass fittings.
- 画幅：1.85:1 or 2.35:1.

## 视频提示
- 镜头运动（只选一种）：slow dolly in toward the projector beam and the screen, then hold.
- 主体运动：a hand threading film; dust drifting in the beam; a crowd turning its faces up to the screen; the projectionist standing still at the window.
- 时长 / 帧率 / 运动模糊：6–10 seconds, 24fps, gentle motion blur; hold the last two seconds so the light can settle.

## 负面提示
no source-less golden glow, no sepia-only grade, no modern digital sharpness, no handheld camera, no fast cutting, no cute-child cliché, no complete reconciliation, no postcard Italy, no voice-over explaining every feeling, no empty square without an audience, no clean new cinema.

## 一致性锚点
- 色彩：amber, honey, burnt orange, olive, cream; deep blue at night, always with a warm source.
- 镜头：35–50mm wide, 85–135mm for face and device; 1.85:1.
- 光线：projector beam, sunset, bare bulb; dust visible, source visible.
- 构图：symmetrical, frontal, frame-within-frame; device in the foreground.
- 材质：film reels, dust, velvet, plaster, old posters, linen.
- 禁止漂移：no modern multiplex, no LED white, no digital skin, no drone shot, no CGI crowd, no clean empty frame.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 250`；用《天堂电影院》放映室或广场静帧做 `--sref`；`--no sepia, modern cinema, handheld`。
- SDXL / ComfyUI：用 ControlNet canny 锁门框/放映窗口的画中画；positive 里写明 `projector beam visible, dust in beam`，否则模型会给无源暖光。
- Runway / Kling / Sora / Veo：首帧给放映机与光束，只写 `slow dolly in`；最后两秒写 `hold`，不要让它自动切到人群或拉远。
