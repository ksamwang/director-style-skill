#!/usr/bin/env python3
"""Detect near-duplicate prose across director entries (8-char shingles)."""

import re
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / ".claude" / "skills" / "film-creation" / "references" / "directors"

CJK = re.compile(r"[一-鿿]")
SENT_SPLIT = re.compile(r"[。！？；\n]+")


def body_of(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def normalize(text: str) -> str:
    return "".join(CJK.findall(body_of(text)))


def shingles(s: str, n: int = 8) -> set:
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    docs = {}
    for path in sorted(DIR.glob("*.md")):
        docs[path.stem] = normalize(path.read_text(encoding="utf-8"))

    print(f"Documents: {len(docs)}\n")

    print("== Top shingle overlaps ==")
    pairs = []
    for (na, a), (nb, b) in combinations(docs.items(), 2):
        pairs.append((jaccard(shingles(a), shingles(b)), na, nb))
    for score, na, nb in sorted(pairs, reverse=True)[:25]:
        if score >= 0.12:
            print(f"{score:.3f}  {na}  ×  {nb}")

    print("\n== Repeated full sentences (>= 18 chars) ==")
    sentences = Counter()
    owners = {}
    for name, text in docs.items():
        for sent in SENT_SPLIT.split(body_of((DIR / f"{name}.md").read_text(encoding="utf-8"))):
            sent = "".join(CJK.findall(sent))
            if len(sent) >= 18:
                sentences[sent] += 1
                owners.setdefault(sent, []).append(name)
    dupes = [(s, c) for s, c in sentences.items() if c > 1]
    if not dupes:
        print("none")
    for sent, count in sorted(dupes, key=lambda x: -x[1])[:30]:
        print(f"{count}x  {sent[:60]}  <- {', '.join(sorted(set(owners[sent]))[:6])}")


if __name__ == "__main__":
    main()
