import qrcode
from PIL import Image

def gen_qr(text, link, fname):
    """
    str text
    str link
    str fname, without file ending
    """

    img = qrcode.make(text)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    img.save(str(fname) + ".png")

if __name__ == '__main__':
    gen_qr('BitcoinPricingKernelsNFT', 'https://testnet.algoexplorer.io/tx/CKZWKFMBUWI7P2VFDQ4JUEPGQLQPND52MC7FGGBMMGNCOR7OKNFQ', 'BitcoinPricingKernelsNFT')
    gen_qr('BitcoinPricingKernels', 'https://github.com/QuantLet/BitcoinPricingKernels/tree/master/BitcoinPricingKernels', 'BitcoinPricingKernelsQR')
