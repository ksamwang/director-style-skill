#!/usr/bin/env python3
"""Structural + length + banned-phrase checks for director entries."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / ".claude" / "skills" / "film-creation" / "references" / "directors"

REQUIRED_FM = ["name", "title", "region", "era", "family", "signature_layers", "anchors", "keywords", "film_grab"]
REQUIRED_SECTIONS = [
    "一句话签名", "核心命题", "人物关系", "视觉规则", "镜头语法",
    "表演与对白", "时间与剪辑", "声音规则", "反向约束", "误读警告",
    "可复用做法", "混搭接口", "同族差异", "视觉配方", "视觉参考",
]

BANNED = [
    (r"出生于|生于\d", "生平信息"),
    (r"获得.{0,8}奖|奥斯卡|金棕榈|金狮|金熊|戛纳.{0,6}奖|威尼斯.{0,6}奖", "奖项信息"),
    (r"被誉为|影史地位|大师地位|影响了无数", "影史评价"),
    (r"票房", "票房信息"),
]

CJK = re.compile(r"[一-鿿]")


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
    files = sorted(DIR.glob("*.md"))
    print(f"Files: {len(files)}\n")
    problems = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        body = body_of(text)
        chars = len(CJK.findall(body))
        keys = fm_keys(text)
        missing_fm = [k for k in REQUIRED_FM if k not in keys]
        missing_sec = [s for s in REQUIRED_SECTIONS if f"## {s}" not in text]
        warns = [label for pat, label in BANNED if re.search(pat, body)]

        issues = []
        if chars < 1200:
            issues.append(f"太短({chars})")
        elif chars > 1800:
            issues.append(f"太长({chars})")
        if missing_fm:
            issues.append("缺字段:" + ",".join(missing_fm))
        if missing_sec:
            issues.append("缺章节:" + ",".join(missing_sec))
        if warns:
            issues.append("禁用:" + ",".join(sorted(set(warns))))

        if issues:
            problems += 1
            print(f"[!] {path.stem}: {' | '.join(issues)}")
        else:
            print(f"[ok] {path.stem}: {chars} 字")

    print(f"\nChecked {len(files)} files, {problems} with issues.")
    if len(files) != 125:
        print(f"WARNING: expected 125 files, got {len(files)}")


if __name__ == "__main__":
    main()
