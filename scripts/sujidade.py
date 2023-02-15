import cv2
import numpy as np

# Carrega a imagem do painel solar
img = cv2.imread('../imagens/painel_solar.jpg')

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica um filtro de suavização para remover o ruído da imagem
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplica uma transformação morfológica para realçar as bordas dos elementos na imagem
kernel = np.ones((5,5), np.uint8)
morph = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)

# Define um limite de intensidade de pixel para segmentar a imagem em áreas sujas e limpas
thresh_value = 100
_, thresh = cv2.threshold(morph, thresh_value, 255, cv2.THRESH_BINARY)

# Calcula a porcentagem de pixels brancos na imagem segmentada
dirty_percentage = (cv2.countNonZero(thresh) / (thresh.shape[0] * thresh.shape[1])) * 100

# Exibe a imagem segmentada e o percentual de sujeira na tela
cv2.imshow('Imagem segmentada', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'Percentual de sujeira: {dirty_percentage:.2f}%')