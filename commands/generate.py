from PIL import Image, ImageDraw, ImageFont, ImageSequence
from env import FONT, TRAVIS_GIF
from io import BytesIO
from discord.ext import commands
import discord
import textwrap

def setup(bot):
    bot.add_cog(Generate(bot))

class Generate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[''])
    async def generate(self, ctx, *, arg):
        await ctx.trigger_typing()

        gif = Image.open(TRAVIS_GIF)

        W, H = gif.size

        img = Image.new(
            'RGBA',
            (W, H),
            (255, 0, 0, 0)
        )

        font = ImageFont.truetype(FONT, 40)
        image_layer = ImageDraw.Draw(img)

        caption = arg
        caption_size = font.getsize(caption)

        def wrap(text):
            lines = []
            line = []

            for i in caption.split(" "):
                line.append(i)
                w, h = font.getsize(" ".join(line))
                if w > W:
                    line.pop()
                    lines.append(" ".join(line))
                    line = [i]

            if len(line) > 0:
                lines.append(" ".join(line))

            return lines

        current_y = 50  # all alignment values are hardcoded because i'm not good with maths

        for i in wrap(caption):    
            image_layer.text(((W / 2), current_y), i, font=font, fill="white", anchor="mb")
            current_y += 45

        if current_y > 340:
            await ctx.send("too many words vro")
            return
        
        else:
            frames = []
            for frame in ImageSequence.Iterator(gif):
                frame = frame.copy().convert('RGBA')
                frame.paste(img, mask=img)
                frames.append(frame)

        with BytesIO() as output:
            frames[0].save(output, "GIF", save_all=True, optimize=True, append_images=frames[1:])
            output.seek(0)
            await ctx.send(file=discord.File(fp=output, filename="output.gif"))