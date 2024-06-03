import qrcode
from PIL import Image

# Créer un objet QRCode avec une taille plus grande et une correction d'erreur plus élevée
qr = qrcode.QRCode(
    version=3,
    box_size=20,
    border=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Définir les données à encoder dans le code QR
data = "https://924efbbcd97a93a4.chmeetings.com/forms/60AADCBDF3EEAAAE"

# Ajouter les données à l'objet QRCode
qr.add_data(data)

# Créer le code QR
qr.make(fit=True)

# Créer une image à partir du code QR avec une couleur de remplissage noire et un fond blanc
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarder l'image du code QR
img.save("Inscription_member_ICC_Gonesse.png")

print("QR code généré et sauvegardé sous le nom 'qr_code.png'")
