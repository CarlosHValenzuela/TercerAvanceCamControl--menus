import cv2
import pytesseract
import re
from core.models import Auto

# Configuración de Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\carlo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Configurar la captura de video
camera = cv2.VideoCapture(0)

# Función para validar y formatear la patente detectada
def format_plate(text):
    text = re.sub(r'\W+', '', text).upper()
    match = re.match(r'^([A-Z]{2}\d{4}|[A-Z]{4}\d{2})$', text)
    if match:
        return text
    return None

def generate_frames():
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        edged = cv2.Canny(gray, 30, 200)

        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        plate = None

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

            if len(approx) == 4:
                plate = approx
                break

        if plate is not None:
            cv2.drawContours(frame, [plate], -1, (0, 255, 0), 3)
            x, y, w, h = cv2.boundingRect(plate)
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (400, 200))

            raw_text = pytesseract.image_to_string(roi, config='--psm 8').strip()
            plate_text = format_plate(raw_text)

            if plate_text:
                # Consultar la base de datos para verificar si la patente está registrada
                try:
                    vehicle = Auto.objects.get(placa=plate_text)
                    persona_nombre = vehicle.persona.nombre 
                    cv2.putText(frame, f'Patente registrada', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                except Auto.DoesNotExist:
                    cv2.putText(frame, 'Patente no registrada', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            else:
                cv2.putText(frame, 'Formato de patente no reconocido', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        else:
            cv2.putText(frame, 'No se detecto patente', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')