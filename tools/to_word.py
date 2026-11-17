"""Convert a Markdown file from this repo into a Word document.

Usage (from the repo folder):
    python3 tools/to_word.py draft/ch4-fixes-and-limits.md
    python3 tools/to_word.py thesis-outline.md Thesis-Outline.docx

The .docx goes to ~/Documents unless the second argument is a full path.
Links to repo files become plain text; tables get light gray borders.
Needs pandoc.
"""
import os
import re
import subprocess
import sys
import tempfile
import zipfile

BORDERS = "<w:tblBorders>" + "".join(
    f'<w:{e} w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/>'
    for e in ["top", "left", "bottom", "right", "insideH", "insideV"]
) + "</w:tblBorders>"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    if len(sys.argv) > 2:
        out = sys.argv[2]
    else:
        out = os.path.splitext(os.path.basename(src))[0] + ".docx"
    if not os.path.isabs(out):
        out = os.path.join(os.path.expanduser("~/Documents"), out)

    text = open(src, encoding="utf-8").read()
    text = re.sub(r"\[([^\]]+)\]\((?!http)[^)]+\)", r"\1", text)  # local links -> text
    text = re.sub(r"\n---\n", "\n", text)  # horizontal rules -> nothing

    with tempfile.TemporaryDirectory() as tmp:
        md = os.path.join(tmp, "in.md")
        raw = os.path.join(tmp, "raw.docx")
        open(md, "w", encoding="utf-8").write(text)
        subprocess.run(["pandoc", md, "-f", "gfm", "-o", raw], check=True)

        zin = zipfile.ZipFile(raw)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename.endswith("/"):
                    continue
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    xml = data.decode("utf-8")
                    xml = re.sub(
                        r'<w:tblW w:type="pct" w:w="[^"]*" />',
                        '<w:tblW w:type="auto" w:w="0" />' + BORDERS,
                        xml,
                    )
                    data = xml.encode("utf-8")
                zout.writestr(item, data)
    print("Saved", out)


if __name__ == "__main__":
    main()
