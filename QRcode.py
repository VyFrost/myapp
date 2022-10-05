import qrcode 
# link="https://youtu.be/mQJPRaTlmIY"
img_link="https://mylogin22.herokuapp.com/msg"
# link="Asis Dash, Python Developer"
# from datetime import datetime
# now_time=datetime.now().strftime("%d-%m-%Y")
# combined_date=f"Domain Name {link}, date is {now_time}"

qr_data=qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
    )

qr_data.add_data(img_link)
qr_data.make(fit=True)
qr_gen = qr_data.make_image(fill_color="black", back_color="white")
qr_gen.save("secQrcode.png")