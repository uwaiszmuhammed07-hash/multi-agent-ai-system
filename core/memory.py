class SharedMemory:
    def __init__(self):
        self._store = {}
        self._history = []

    def write(self, key: str, value: str):
        self._store[key] = value
        self._history.append({"key": key, "value": value})

    def read(self, key: str) -> str:
        return self._store.get(key, "")

    def get_all(self) -> dict:
        return self._store

    def get_history(self) -> list:
        return self._history