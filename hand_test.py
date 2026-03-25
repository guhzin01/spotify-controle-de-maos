from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import mediapipe as mp


# caminho do modelo
model_path = "models/hand_landmarker.task"

# configurações básicas de modelo predefenido
base_options = python.BaseOptions(model_asset_path=model_path)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

# cria o detector
detector = vision.HandLandmarker.create_from_options(options)

print("Detector criado com sucesso 🚀")

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not captura.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

while True:
    success, frame = captura.read()

    if not success:
        print("Erro ao acessar a câmera")
        break

    # DETECÇÃO
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
    resultado = detector.detect(mp_image)
    if resultado.hand_landmarks:
        print(len(resultado.hand_landmarks[0]))
    altura, largura, _ = frame.shape


    if resultado.hand_landmarks:
        for hand in resultado.hand_landmarks:
            for landmark in hand:
                x_pixel = int(landmark.x * largura)
                y_pixel = int(landmark.y * altura)

                cv2.circle(frame, (x_pixel, y_pixel), 8, (0, 255, 0), -1)
    
    if resultado.hand_landmarks:
        print("Mão detectada")

    # MOSTRAR IMAGEM
    cv2.imshow("Camera", frame)

    # 🔥 ESSA LINHA É IMPORTANTE
    key = cv2.waitKey(1)

    # ESC
    if key == 27:
        print("Saindo...")
        break

    # se fechar no X
    if cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1:
        print("Janela fechada")
        break

captura.release()
cv2.destroyAllWindows()
