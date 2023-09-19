from collections import defaultdict

from .event_listener import EventListener


class EventManager:
    def __init__(self) -> None:
        self.__listeners: dict[list[EventListener]] = defaultdict(list)

    @property
    def listeners(self) -> list[EventListener]:
        return self.__listeners

    def subscribe(self, event: str, listener: EventListener) -> None:
        self.__listeners[event].append(listener)

    def unsubscribe(self, event: str, listener: EventListener) -> None:
        self.__listeners[event].remove(listener)

    def notify(self, event: str, *args, **kwargs) -> None:
        for listener in self.__listeners[event]:
            listener.notify(event, *args, **kwargs)
