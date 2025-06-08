from PIL import Image

img = Image.open("icon.png")
img = img.convert("RGBA")  # 確保含透明度
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
img.save("icon.ico", format="ICO", sizes=sizes)
