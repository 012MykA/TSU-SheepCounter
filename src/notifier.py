from abc import ABC, abstractmethod
import requests
import cv2


class BaseNotifier(ABC):
    @abstractmethod
    def notify(self, count: int, frame=None) -> None:
        pass


class TelegramNotifier(BaseNotifier):
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def notify(self, count: int, frame=None) -> None:
        message = f"Found sheep count: {count}"
        try:
            requests.post(
                self.api_url + "sendMessage",
                data={"chat_id": self.chat_id, "text": message},
                timeout=10,
            )

            if frame is not None:
                _, img_encoded = cv2.imencode(".jpg", frame)
                requests.post(
                    self.api_url + "sendPhoto",
                    data={"chat_id": self.chat_id},
                    files={"photo": img_encoded.tobytes()},
                    timeout=10,
                )
        except Exception as e:
            print(f"Notificator error: {e}")


class ConsoleNotifier(BaseNotifier):
    def notify(self, count: int, frame=None) -> None:
        print(f"[LOG] Sheep count: {count}")
