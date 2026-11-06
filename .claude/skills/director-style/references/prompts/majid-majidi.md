---
name: majid-majidi
title: 马基德·马基迪 Majid Majidi
style_file: ../directors/majid-majidi.md
---

## 风格锚点
Cinematic film still, rural Iran, a child at eye level, golden natural backlight, dust and wheat, warm ochre and saturated green, medium close-up of a face, shallow depth of field, 85mm lens, handheld follow from behind, 1.85:1, 35mm grain, tender, dignified, luminous, no glamour.

## 图像提示
- 主体 / 场景：a boy carrying worn shoes through a dusty alley; a blind child reaching toward wind and sound; a girl in a blue headscarf at a courtyard well.
- 景别 / 构图：medium close-up of the child's face, low horizon, child centered or slightly off-center, foreground wheat or grass; wide only to make the child small in landscape.
- 镜头 / 焦段：50–85mm shallow focus for faces; 35mm for running and following.
- 光线：natural sun, backlight, golden hour, dust or rain diffusing the light; no studio fill.
- 色彩：warm ochre, wheat gold, saturated green, sky blue; natural saturation, no sepia.
- 材质：dust, mud brick, wool, water, worn shoes, wheat, coarse cloth.
- 画幅：1.85:1.

## 视频提示
- 镜头运动：one handheld follow at the child's eye level, tracking from behind, then stopping when the child stops.
- 主体运动：walking, running, looking back, small hand movements; adults move past the frame edge.
- 时长 / 帧率 / 运动模糊：6–12 seconds, 24fps, natural motion blur, no slow motion.

## 负面提示
no ironic distance, no adult voice-over, no shaky handheld realism, no grey-blue art-house grade, no sepia nostalgia, no crying close-up as a shortcut, no villain adults, no city glamour, no slow-motion climax, no studio lighting.

## 一致性锚点
- 色彩：warm ochre / wheat gold / saturated green / sky blue, natural saturation.
- 镜头：50–85mm for faces, 35mm for following, 1.85:1.
- 光线：natural sun, backlight, golden hour, dust diffusion.
- 构图：child's eye level, low horizon, centered child, foreground grass or wheat.
- 材质：dust, mud brick, wool, water, worn shoes, film grain.
- 禁止漂移：no teal-orange grade, no modern city, no digital skin, no drone shots, no studio softbox.

## 平台备注
- Midjourney：`--ar 1.85:1 --style raw --stylize 200`；用自然光儿童纪实照片做 `--sref`，不要用广告式暖调。
- SDXL / ComfyUI：固定 prompt 块 + 细颗粒 LoRA；用 ControlNet depth 锁低机位与前景麦草，色彩用土黄绿色板。
- Runway / Kling / Sora / Veo：首帧图起手，只给低机位手持跟拍一种运镜，6–12 秒，24fps；不要叠加推近和环绕。
