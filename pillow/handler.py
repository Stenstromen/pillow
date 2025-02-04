from PIL import Image
import io

def handle(req):
    buf = io.BytesIO()
    with Image.open(io.BytesIO(req)) as im:
        im_grayscale = im.convert("L")
        try:
            im_grayscale.save(buf, format='JPEG')
        except OSError:
            return "cannot process input file", 500, {"Content-type": "text/plain"}

        byte_im = buf.getvalue()
        return byte_im, 200, {"Content-type": "application/octet-stream"}