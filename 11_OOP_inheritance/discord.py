from abc import ABC, abstractmethod

class DiscordConnector:
    def wrzuc_kanal(self, channel):
        channel.send('message')

# -----------------

class Channel(ABC):
    @abstractmethod
    def send(self, msg: str):
        pass


# -----------------

class PythonChannel(Channel):
    def send(self, msg):
        print('wrzuć cieakawy news', msg)

# -----------------


class SQLChannel(Channel):
    name = 'SQLChannel'

    def send(self, msg):
        print('wrzuć cieakawy news', msg)


pykanal = PythonChannel()
d = DiscordConnector()
d.wrzuc_kanal()