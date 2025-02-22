import cv2

import cv2

def read_video(video_path):
    frames = []
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()

# 1. read_video(video_path)
# Questa funzione legge un video da un file e lo converte in una lista di frame (immagini).

# Cosa fa:

# Apre il video specificato da video_path utilizzando cv2.VideoCapture.

# Legge ogni frame del video uno per uno in un ciclo while.

# Se il frame viene letto correttamente (ret è True), lo aggiunge alla lista frames.

# Quando non ci sono più frame da leggere (ret è False), il ciclo si interrompe.

# Rilascia la risorsa del video con cap.release().

# Restituisce la lista di frame.

# A cosa serve:

# Questa funzione è utile per estrarre tutti i frame da un video e lavorarli individualmente (ad esempio, per analisi, elaborazione, modifica, ecc.).

# 2. save_video(output_video_frames, output_video_path)
# Questa funzione salva una lista di frame come un nuovo video.

# Cosa fa:

# Crea un oggetto cv2.VideoWriter per scrivere un nuovo video.

# fourcc = cv2.VideoWriter_fourcc(*'MJPG'): Specifica il codec da utilizzare per il video (in questo caso, MJPG).

# out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height)): Crea un oggetto per scrivere il video. I parametri sono:

# output_video_path: Il percorso del file di output.

# fourcc: Il codec utilizzato.

# 24: Il frame rate (FPS) del video.

# (width, height): Le dimensioni del video (prese dal primo frame della lista output_video_frames).

# Scrive ogni frame nella lista output_video_frames nel file video.

# Rilascia la risorsa con out.release().

# A cosa serve:

# Questa funzione è utile per salvare una sequenza di frame come un nuovo video. Ad esempio, dopo aver elaborato i frame (applicando filtri, ridimensionando, ecc.), puoi salvarli in un nuovo file video.