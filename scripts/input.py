import cv2
import os

# Inicializa a captura da webcam
cap = cv2.VideoCapture(0)

# Captura um quadro da webcam
ret, frame = cap.read()

# Verifica se a captura foi bem sucedida
if not ret:
    print('Não foi possível capturar o quadro')

# Define o caminho para a pasta onde você deseja salvar a imagem
folder_path = '../imagens'

# Cria a pasta se ela não existir
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define o nome do arquivo de imagem e o caminho completo
file_name = 'painel_solar.jpg'
file_path = os.path.join(folder_path, file_name)

# Salva a imagem no caminho especificado
cv2.imwrite(file_path, frame)

# Libera a captura da webcam e fecha a janela de visualização
cap.release()
cv2.destroyAllWindows()