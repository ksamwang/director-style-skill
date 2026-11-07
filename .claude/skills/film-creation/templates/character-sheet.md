# 人物角色表提示词规范

> 一张 3:2 三面板角色表：左无头正面、中背面、右 3/4 特写。全表只有一张脸。

## 固定规范

- **画幅**：3:2 横向，三个等宽、等高面板。
- **背景**：统一纯色 `#D9D9D9`；均匀、无阴影的棚拍光。
- **左面板**：正面全身，无头。
  - 颈根以上（脸、耳、头发、头饰）全部替换为 `#D9D9D9`，与背景无缝；无轮廓、无阴影、无纹理、无渐变、无遮罩边。
  - 颈根到鞋底完整可见；自然站立，肩放松，手臂下垂，手空。
  - 保持全身构图；头顶留空；不裁切脖子、不放大身体、不上移。
  - 头饰或衣领若延伸到颈根以下，保留颈根及以下部分。
  - 这是干净的图形遮罩效果；不得出现颈断面、伤口、损伤。
- **中面板**：背面全身，头可见，无脸。
  - 与左面板同身体比例、姿态、机位高度、距离、透视；同一地面基线。
  - 不得独立缩放或重新居中。
- **右面板**：3/4 头肩特写，从胸口以上。
  - 身体和脸转向观众左侧（角色右侧），目光直视镜头。
  - 与左/中同身份、同服装、同头饰。
  - 全表只有这一张脸。
- **对齐**：
  - 颈根、肩线、肘、腰、胯、膝、踝、鞋底在相同垂直坐标。
  - 躯干长度、四肢长度、肩宽、站距、整体比例一致；同一地面基线；各自在面板垂直中轴。
  - 左肩以上空白 = 中面板头部所占区域；不得拉伸、压缩、位移、缩放。

## Trait card（先填）

```text
age | build | face | hair | outfit | palette (hex) | props | headwear
```

## 提示词模板

```text
CHARACTER SHEET — 3:2 horizontal, three equal panels, solid #D9D9D9 background, even shadowless studio lighting.

IDENTITY (all panels): {{age}} | {{build}} | {{outfit}} | {{palette hex}} | {{props}}
HEAD (middle + right only): {{face}} | {{hair}} | {{headwear}}

LEFT PANEL: front full-body, headless. Everything above the neck base is exactly #D9D9D9, seamless with the background; no silhouette, outline, shadow, texture, gradient, or mask edge. Body from neck base to shoe soles visible; arms hanging; hands empty; same framing and scale as the middle panel. If headwear or clothing extends below the neck base, keep the part at and below the neck base. Clean graphic mask; no neck cross-section, wound, or injury.

MIDDLE PANEL: full back view, head visible, no face. Same outfit, proportions, camera height, distance, body scale; shared ground baseline.

RIGHT PANEL: three-quarter head-and-shoulders close-up; body and face turned to viewer's left; gaze into lens. Same identity and outfit. This is the only face in the sheet.

ALIGNMENT: neck base, shoulder line, elbows, waist, hips, knees, ankles, shoe soles at identical vertical coordinates; same torso length, limb lengths, shoulder width, stance width; no stretch, compress, shift, or rescale.
```

## 负面

```text
wound | cut | neck cross-section | injury | outline | shadow | gradient | mask edge | cropped body | extra face | duplicate head | inconsistent outfit | different body scale | misaligned panels | text | watermark
```
