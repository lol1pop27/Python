import tellopy
import cv2
import numpy as np
import time

def main():
    drone = tellopy.Tello()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)
        print("Подключение установлено.")

        drone.start_video()
        container = drone.get_video_stream()

        print("Управление:")
        print("W/S: вперед/назад, A/D: влево/вправо")
        print("Arrow Up/Down: вверх/вниз, Arrow Left/Right: поворот")
        print("T: взлет, L: посадка, Q: выход")

        for frame in container:
            image = cv2.cvtColor(np.array(frame.to_image()), cv2.COLOR_RGB2BGR)
            cv2.imshow('Tello Video', image)

            key = cv2.waitKey(1) & 0xFF

            # Движение
            if key == ord('w'):
                drone.forward(50)
            elif key == ord('s'):
                drone.backward(50)
            else:
                drone.forward(0)
                drone.backward(0)

            if key == ord('a'):
                drone.left(50)
            elif key == ord('d'):
                drone.right(50)
            else:
                drone.left(0)
                drone.right(0)

            # Вверх/вниз
            if key == 82:  # стрелка вверх
                drone.up(50)
            elif key == 84:  # стрелка вниз
                drone.down(50)
            else:
                drone.up(0)
                drone.down(0)

            # Повороты
            if key == 81:  # стрелка влево
                drone.counter_clockwise(50)
            elif key == 83:  # стрелка вправо
                drone.clockwise(50)
            else:
                drone.clockwise(0)
                drone.counter_clockwise(0)

            # Взлет и посадка
            if key == ord('t'):
                drone.takeoff()
            elif key == ord('l'):
                drone.land()

            # Выход
            if key == ord('q'):
                break

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        print("Завершение работы...")
        drone.quit()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
