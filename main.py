from fastapi import FastAPI
import qrcode


app = FastAPI()



qr = qrcode.QRCode()




@app.post("/qrcode/")
async def generate(url: str):
    file_path = "qrcode.png"
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)

    return {"message":f"QrCode Generate for: {url}"}


