import os

import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont


def generate_modern_logo(text="LOGO", size=(300, 300)):
    """
    Generates a modern minimalist logo with gradient background, abstract shapes, and text.

    Parameters:
        text (str): The text to display on the logo.
        size (tuple): The size of the logo (width, height).

    Returns:
        None
    """

    save_path = os.path.abspath("./processed_data/logos/" + text+".png")
    # Create a gradient background
    img = Image.new("RGB", size, (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i in range(size[1]):  # Vertical gradient
        color = (
            int(50 + (200 - 50) * (i / size[1])),  # R
            int(100 + (255 - 100) * (i / size[1])),  # G
            int(150 + (255 - 150) * (i / size[1]))  # B
        )
        draw.line([(0, i), (size[0], i)], fill=color)

    # Draw random semi-transparent shapes
    for _ in range(random.randint(2, 5)):
        shape_type = random.choice(["circle", "rectangle"])
        color = tuple(np.random.randint(50, 200, 3)) + (random.randint(100, 180),)  # RGBA for transparency

        x1, x2 = sorted([random.randint(20, size[0] - 20) for _ in range(2)])
        y1, y2 = sorted([random.randint(20, size[1] - 20) for _ in range(2)])

        if shape_type == "circle":
            draw.ellipse([x1, y1, x2, y2], fill=color)
        else:
            draw.rectangle([x1, y1, x2, y2], fill=color)

    # Load a modern font
    font_path = "arial.ttf"  # Replace with a modern font if available
    font_size = min(size) // 5

    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate centered position
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2

    # Add shadow effect for text
    shadow_offset = 3
    draw.text((text_x + shadow_offset, text_y + shadow_offset), text, fill=(50, 50, 50), font=font)  # Shadow
    draw.text((text_x, text_y), text, fill="white", font=font)  # Main text

    # Save the logo
    os.makedirs(os.path.abspath("./processed_data/logos/"), exist_ok=True)
    img.save(save_path)
    return save_path
