import socket
import cv2
import numpy as np
import evaluate

def receive_image(sock):
    length = int.from_bytes(sock.recv(4), byteorder='big')
    data = b''

    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            return None
        data += packet

    image = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def send_image(sock, image):
    _, buffer = cv2.imencode('.jpg', image)
    data = buffer.tobytes()
    sock.send(len(data).to_bytes(4, byteorder='big'))
    sock.send(data)

def main():
    foggy_model = evaluate.YoloTest()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8001))
    server_socket.listen(1)
    print('Server listening on port 8001')

    while True:
        conn, addr = server_socket.accept()
        print(f'Connected by {addr}')

        # Receive image from client
        image = receive_image(conn)
        if image is not None:
            foggy_image_filtered = foggy_model.evaluate(image)
            send_image(conn, foggy_image_filtered)

        conn.close()

if __name__ == '__main__':
    main()