from pyltover.base import BasePyltover


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr
