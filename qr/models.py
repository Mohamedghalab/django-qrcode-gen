from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

class QrCodeGen(models.Model):
    product = models.CharField(max_length=64)
    price   = models.DecimalField(decimal_places=2, max_digits=5)
    img     = models.ImageField(upload_to='code', blank=True)

    def __str__(self):
        return self.product

    
    
    def save(self, *args, **kwargs):
        img = qrcode.make(f'{self.product} {self.price}')
        canvas = Image.new('RGB',(400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        fname=f'qrcode-{self.product[:4]}.png'
        buffer=BytesIO()
        canvas.save(buffer, "PNG")
        self.img.save(fname, File(buffer), save=False)
        canvas.close()
        img = Image.open(self.img.path) # Open image using self
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.img.path)
        super().save(*args, **kwargs)