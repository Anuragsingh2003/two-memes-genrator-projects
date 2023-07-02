import uuid
from django.shortcuts import render
from django.http import HttpResponse
from .models import CaptionImage
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import os
from django.http import HttpResponse, FileResponse
from django.conf import settings


def index(request):
    if request.method == 'POST':
        caption1 = request.POST.get('caption1')
        caption2 = request.POST.get('caption2')
        caption3 = request.POST.get('caption3')
        caption1_fg_color = request.POST.get('caption1_fg_color')
        caption1_bg_color = request.POST.get('caption1_bg_color')
        caption2_fg_color = request.POST.get('caption2_fg_color')
        caption2_bg_color = request.POST.get('caption2_bg_color')
        caption3_fg_color = request.POST.get('caption3_fg_color')
        caption3_bg_color = request.POST.get('caption3_bg_color')
        caption1_position = request.POST.get('caption1_position')
        caption2_position = request.POST.get('caption2_position')
        caption3_position = request.POST.get('caption3_position')
        image = request.FILES.get('image')

        # Save the user's inputs and uploaded image
        caption_image = CaptionImage(
            caption1=caption1,
            caption2=caption2,
            caption3=caption3,
            caption_color1=caption1_fg_color,
            caption_background_color1=caption1_bg_color,
            caption_color2=caption2_fg_color,
            caption_background_color2=caption2_bg_color,
            caption_color3=caption3_fg_color,
            caption_background_color3=caption3_bg_color,
            position1=caption1_position,
            position2=caption2_position,
            position3=caption3_position,
            image=image
        )
        caption_image.save()

        # Generate new image with captions
        new_image = generate_captioned_image(caption_image)

        # Render the meme_detail.html template with the new image
        return render(request, 'meme_detail.html', {'new_image': new_image})

    return render(request, 'meme_form.html')


def hex_to_rgb(hex_color):
    hex_color = hex_color.strip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_captioned_image(caption_image):
    image = Image.open(caption_image.image)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 24)

    # Write captions on the image
    caption_x = 10
    caption_y = 50  # Starting y position

    for i, caption_field in enumerate(['caption1', 'caption2', 'caption3']):
        caption = getattr(caption_image, caption_field)
        caption_color_field = 'caption_color' + str(i+1)
        caption_background_color_field = 'caption_background_color' + str(i+1)
        position_field = 'position' + str(i+1)

        # Set caption color, background color, and position
        caption_color = hex_to_rgb(getattr(caption_image, caption_color_field))
        caption_background_color = hex_to_rgb(
            getattr(caption_image, caption_background_color_field))
        caption_position = getattr(caption_image, position_field)

        # Draw the background rectangle
        caption_text_width, caption_text_height = draw.textsize(
            caption, font=font)
        caption_box_width = caption_text_width + 10
        caption_box_height = caption_text_height + 10

        if caption_position == 'top':
            caption_y = 10
        elif caption_position == 'bottom':
            caption_y = image.height - caption_box_height - 10
        else:  # 'center'
            caption_y = (image.height - caption_box_height) // 2

        draw.rectangle(
            (caption_x, caption_y, caption_x +
             caption_box_width, caption_y + caption_box_height),
            fill=caption_background_color
        )

        # Write the caption text
        draw.text((caption_x + 5, caption_y + 5),
                  caption, font=font, fill=caption_color)

        # Update the y position for the next caption
        caption_y += caption_box_height + 10

    # Save the new image to disk
    new_image_path = f"media/uploads/{uuid.uuid4()}.jpg"
    image.save(new_image_path, format='JPEG')

    return new_image_path
