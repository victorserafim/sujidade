import cv2
import numpy as np

# Carregar a imagem da placa solar
img = cv2.imread('../imagens/painel_solar.jpg')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Definir limite para inverter cores na imagem binarizada
threshold = 125

# Binarizar a imagem com o limite definido e inverter cores
binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)[1]

# Definir a máscara que cobre a placa solar
mask = np.zeros_like(binary)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        cv2.drawContours(mask, [cnt], 0, 255, -1)

# Aplicar a máscara à imagem binarizada
binary_masked = cv2.bitwise_and(binary, mask)

# Inverter as cores do resultado final da máscara
binary_masked = cv2.bitwise_not(binary_masked)

# Contar o número de pixels brancos na região suja da placa solar
# Aqui, utilizamos a função cv2.countNonZero() 
# para contar o número de pixels brancos na imagem binarizada que estão dentro da região definida pela máscara
dirty_pixels = cv2.countNonZero(binary_masked)

# Contar o número total de pixels na região da máscara
total_pixels = cv2.countNonZero(mask)

# Calcular o percentual de sujidade da placa solar
dirty_percentage = dirty_pixels / total_pixels * 100

# Exibe a imagem segmentada e o percentual de sujeira na tela
cv2.imshow('Imagem segmentada', binary_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir o resultado
print(f'Percentual de sujidade: {dirty_percentage:.2f}%')
cv2.imwrite('imagem_processada.png', binary_masked)