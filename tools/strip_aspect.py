#!/usr/bin/env python3
"""Remove aspect ratio from prompt files; rename the reference ratio in profiles."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, ".claude", "skills", "film-creation", "references")

PROMPT_DIRS = [os.path.join(REF, "prompts"), os.path.join(REF, "prompts-cinematographers")]
PROFILE_DIRS = [os.path.join(REF, "directors"), os.path.join(REF, "cinematographers")]

RATIO = re.compile(r"\b\d+(?:\.\d+)?:\d+(?:\.\d+)?\b")
AR = re.compile(r"\s*--ar\s+\S+")
DRAW = re.compile(r"^- 画幅：.*$", re.M)


def clean_prompt(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("- 画幅："):
            continue
        line = AR.sub("", line)
        line = RATIO.sub("", line)
        line = re.sub(r"\s*,\s*,+", ", ", line)
        line = re.sub(r",\s*;", ";", line)
        line = re.sub(r",\s*\.", ".", line)
        line = re.sub(r"\.\s*,", ". ", line)
        line = re.sub(r"`\s+", "`", line)
        line = re.sub(r"\s{2,}", " ", line)
        line = line.rstrip()
        lines.append(line)
    return "\n".join(lines) + "\n"


def main() -> None:
    prompts = 0
    for d in PROMPT_DIRS:
        for path in glob.glob(os.path.join(d, "*.md")):
            text = open(path, encoding="utf-8").read()
            new = clean_prompt(text)
            if new != text:
                open(path, "w", encoding="utf-8").write(new)
                prompts += 1

    profiles = 0
    for d in PROFILE_DIRS:
        for path in glob.glob(os.path.join(d, "*.md")):
            text = open(path, encoding="utf-8").read()
            new = re.sub(r"^- (?:画幅|参考画幅（不写入提示）)：", "- 参考画幅：", text, flags=re.M)
            if new != text:
                open(path, "w", encoding="utf-8").write(new)
                profiles += 1

    print(f"Cleaned {prompts} prompt files; renamed ratio label in {profiles} profiles.")


if __name__ == "__main__":
    main()
