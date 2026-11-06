#!/usr/bin/env python3
"""Structural + visual checks for cinematographer profiles."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, ".claude", "skills", "director-style", "references", "cinematographers")

REQUIRED_FM = ["name", "title", "region", "era", "family", "signature_layers",
               "collaborators", "anchors", "keywords", "film_grab"]
REQUIRED_SECTIONS = [
    "一句话签名", "核心命题（视觉观）", "人物关系（与导演/演员/空间）",
    "视觉规则", "镜头语法", "光线与色彩", "时间与运动", "制作条件",
    "反向约束", "误读警告", "可复用做法", "混搭接口", "同族差异",
    "视觉配方", "视觉参考",
]
VIS_DIMS = ["景别", "构图", "空间", "色彩", "光线", "材质"]
CAM_DIMS = ["机位", "焦段", "运动", "静止", "靠近", "远离", "权力"]
SPEC_FIELDS = ["参考画幅", "镜头/焦段", "机位与运动", "色彩", "光线", "材质/美术", "构图"]
CJK = re.compile(r"[一-鿿]")


def section(text: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    return text[start:start + nxt.start()] if nxt else text[start:]


def body_of(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def fm_keys(text: str) -> set:
    if not text.startswith("---"):
        return set()
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else ""
    return set(re.findall(r"^([A-Za-z_]+):", block, re.M))


def main() -> None:
    files = sorted(glob.glob(os.path.join(DIR, "*.md")))
    print(f"Cinematographer files: {len(files)}\n")
    issues = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        name = os.path.basename(f).replace(".md", "")
        body = body_of(text)
        chars = len(CJK.findall(body))
        keys = fm_keys(text)
        missing_fm = [k for k in REQUIRED_FM if k not in keys]
        missing_sec = [s for s in REQUIRED_SECTIONS if f"## {s}" not in text]

        vis = section(text, "视觉规则")
        cam = section(text, "镜头语法")
        light = section(text, "光线与色彩")
        spec = section(text, "视觉配方")
        vis_hits = [d for d in VIS_DIMS if d in vis]
        cam_hits = [d for d in CAM_DIMS if d in cam]
        spec_lines = re.findall(r"^- ([^：:]+)[：:]", spec, re.M)
        missing_spec = [x for x in SPEC_FIELDS if x not in spec_lines]

        probs = []
        if chars < 1200:
            probs.append(f"太短({chars})")
        elif chars > 1800:
            probs.append(f"太长({chars})")
        if missing_fm:
            probs.append("缺字段:" + ",".join(missing_fm))
        if missing_sec:
            probs.append("缺章节:" + ",".join(missing_sec))
        if len(CJK.findall(vis)) < 180:
            probs.append(f"视觉规则短({len(CJK.findall(vis))})")
        if len(CJK.findall(cam)) < 160:
            probs.append(f"镜头语法短({len(CJK.findall(cam))})")
        if len(CJK.findall(light)) < 150:
            probs.append(f"光线色彩短({len(CJK.findall(light))})")
        if len(vis_hits) < 4:
            probs.append(f"视觉维度{len(vis_hits)}/6")
        if len(cam_hits) < 3:
            probs.append(f"镜头维度{len(cam_hits)}/7")
        if missing_spec:
            probs.append("配方缺:" + ",".join(missing_spec))

        if probs:
            issues += 1
            print(f"[!] {name}: {' | '.join(probs)}")
        else:
            print(f"[ok] {name}: {chars} 字 | 视觉{len(vis_hits)}/6 镜头{len(cam_hits)}/7")

    print(f"\nChecked {len(files)} files, {issues} with issues.")
    if len(files) != 29:
        print(f"WARNING: expected 29, got {len(files)}")


if __name__ == "__main__":
    main()
