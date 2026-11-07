#!/usr/bin/env python3
"""Check AI prompt files under references/prompts/."""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBDIR = sys.argv[1] if len(sys.argv) > 1 else "prompts"
EXPECTED = int(sys.argv[2]) if len(sys.argv) > 2 else 125
DIR = os.path.join(ROOT, ".claude", "skills", "film-creation", "references", SUBDIR)

SECTIONS = ["风格锚点", "图像提示", "视频提示", "负面提示", "一致性锚点", "平台备注"]
IMAGE_FIELDS = ["主体 / 场景", "景别 / 构图", "镜头 / 焦段", "光线", "色彩", "材质"]
VIDEO_FIELDS = ["镜头运动", "主体运动", "时长 / 帧率 / 运动模糊"]


def section(text: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    return text[start:start + nxt.start()] if nxt else text[start:]


def english_words(s: str) -> int:
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))


def main() -> None:
    files = sorted(glob.glob(os.path.join(DIR, "*.md")))
    print(f"Prompt files: {len(files)}\n")
    issues = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        name = os.path.basename(f)
        probs = []
        for sec in SECTIONS:
            if f"## {sec}" not in text:
                probs.append(f"缺:{sec}")
        anchor = section(text, "风格锚点")
        words = english_words(anchor)
        if words < 30:
            probs.append(f"锚点英文词太少({words})")
        elif words > 110:
            probs.append(f"锚点英文词太多({words})")
        img = section(text, "图像提示")
        for field in IMAGE_FIELDS:
            if field not in img:
                probs.append(f"图像缺:{field}")
        vid = section(text, "视频提示")
        for field in VIDEO_FIELDS:
            if field not in vid:
                probs.append(f"视频缺:{field}")
        neg = section(text, "负面提示")
        if english_words(neg) < 8:
            probs.append("负面提示过短")
        if re.search(r"--ar\s", text):
            probs.append("含--ar")
        if re.search(r"\b\d+(?:\.\d+)?:\d+\b", text):
            probs.append("含画幅比例")
        if "style_file:" not in text:
            probs.append("缺 style_file")

        if probs:
            issues += 1
            print(f"[!] {name}: {' | '.join(probs)}")
        else:
            print(f"[ok] {name}: anchor {words} words")

    print(f"\nChecked {len(files)} files, {issues} with issues.")
    if len(files) != EXPECTED:
        print(f"WARNING: expected {EXPECTED} prompt files, got {len(files)}")


if __name__ == "__main__":
    main()
