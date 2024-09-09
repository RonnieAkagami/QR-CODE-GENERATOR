import qrcode
from PIL import Image
from qrcode.console_scripts import error_correction

qr = qrcode.QRCode(version =1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 20)

qr.add_data(#paste your link here which you want to convert to qr code)

qr.make(fit=True)
img = qr.make_image(fill_color='Black',back_color='white')
img.save(#paste the name with which you want to save your qr image followed by '.png')