from PIL import Image, ImageDraw, ImageFont
import os

def main():
    res_dir = r"d:\编程文件\好玩的\JiYuTrainer-1.7.6\JiYuTrainerUI\res"
    os.chdir(res_dir)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    for fname in os.listdir('.'):
        if fname.lower().endswith('.png'):
            img = Image.new('RGB', (128,128), color=(200,200,200))
            d = ImageDraw.Draw(img)
            text = 'C++' if 'logo' in fname.lower() or 'icon' in fname.lower() else ''
            if text:
                bbox = d.textbbox((0,0), text, font=font)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                d.text(((128-w)/2,(128-h)/2), text, fill=(0,0,0), font=font)
            img.save(fname)
        if fname.lower().endswith('.ico'):
            img = Image.new('RGB', (64,64), color=(150,150,150))
            d = ImageDraw.Draw(img)
            text='C++'
            bbox = d.textbbox((0,0), text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            d.text(((64-w)/2,(64-h)/2),text,fill=(0,0,0),font=font)
            img.save(fname)
    print('replaced images')

if __name__ == '__main__':
    main()
