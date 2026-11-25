import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PUNCHLINE = "I opened 100x leverage so my liquidation price and my entry price could finally meet. They did. In four minutes."


def resolve_entry_path():
    target = os.environ.get("ENTRY_OUT")
    if target:
        if target.endswith(".txt"):
            return target
        return os.path.join(target, "entry.txt")
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        return os.path.join(folder, "entry.txt")
    return "/output/entry.txt"


def emit_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


def main():
    emit_entry(resolve_entry_path(), PUNCHLINE)


if __name__ == "__main__":
    main()
