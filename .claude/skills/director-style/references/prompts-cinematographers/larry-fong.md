---
name: larry-fong
title: 拉瑞·方 Larry Fong
style_file: ../cinematographers/larry-fong.md
---

## 风格锚点
Cinematic film still, 2.39:1 anamorphic, 35mm grain, a single hard top-light raking across the body, deep black background, no fill except negative fill, figure centered against empty sky or smoke, amber and steel-blue palette, crushed blacks, desaturated midtones, dust and rain in the air, hard rim on shoulders, poster-like graphic composition, retro 1970s genre film, monumental, still.

## 图像提示
- 主体 / 场景：a lone warrior, detective or soldier standing in smoke, rain or dust; a vast empty landscape or a black soundstage void behind them.
- 景别 / 构图：wide or medium-wide, dead center or low angle, strong verticals, figure small against a large negative space; horizon very low or very high.
- 镜头 / 焦段：27mm Primo or 35–50mm anamorphic; long lens for compressed landscapes.
- 光线：one hard source from top or behind, 8:1–16:1, black background, rim on shoulders, a small eye light inside the silhouette.
- 色彩：amber, steel blue, blood red; crushed blacks, desaturated midtones, no pastel.
- 材质：dust, ash, rain, smoke, metal, leather, wet skin, anamorphic flare.
- 画幅：2.39:1 or 2.40:1.

## 视频提示
- 镜头运动（只选一种）：slow vertical crane rise, revealing the figure against sky or smoke, then a hard stop.
- 主体运动：a figure stands still while cape, coat or smoke moves in the wind.
- 时长 / 帧率 / 运动模糊：4–8 seconds, 24fps base with a 50–100fps speed ramp, crisp edges, no handheld.

## 负面提示
no soft frontal fill, no even skin tones, no handheld shake, no grey-blue desaturated wash, no naturalistic window logic, no wide-angle distortion, no rescued shadows, no pastel palette, no documentary realism, no modern LED white, no clean digital skin.

## 一致性锚点
- 色彩 / 镜头 / 光线 / 构图 / 材质：amber, steel blue and blood red; 27mm or 35–50mm anamorphic; one hard top/back source at 8:1–16:1; centered graphic frame; dust, smoke and wet metal.
- 禁止漂移：no soft key, no handheld, no teal-orange LUT, no daylight naturalism, no clean plastic surfaces.

## 平台备注
- Midjourney：`--ar 2.39:1 --style raw --stylize 250`；加 `--no soft light, handheld`；用高对比电影静帧做 `--sref`。
- SDXL / ComfyUI：negative 里固定 `soft lighting, flat grey, pastel`；ControlNet canny 锁剪影轮廓，depth 只做两层。
- Runway / Kling / Sora / Veo：从一张已打光的首帧开始，只写一种摇臂垂直上升，4–8 秒，24fps 加一次变速，不要叠加推近和手持。
