#!/usr/bin/env python3
"""Build an instructional PDF: 6-pose pencil jaw routine for men."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent.parent
FRAMES = ROOT / "frames"
OUT = ROOT / "out"
OUT.mkdir(parents=True, exist_ok=True)
FRAMES.mkdir(parents=True, exist_ok=True)

print("See repo docs/protocolo-lapiz.md")
print("Full generator lives with the published PDF in the conversation artifacts.")
print("Run locally after copying the complete build_pdf.py if you need frames.")
