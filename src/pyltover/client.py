from pyltover import servers
from pyltover.apis import v1, v4
from pyltover.base import BasePyltover
from pyltover.servers import RegionalRoutingValues, PlatformRoutingValues, esports_server


class Pyltover(BasePyltover):
    def __init__(self, riot_token: str):
        super().__init__(riot_token)
        self.riot_token = riot_token

        self._esport = None

        self._europe = None
        self._americas = None
        self._asia = None
        self._sea = None

        self._br = None
        self._eune = None
        self._euw = None
        self._jp = None
        self._kr = None
        self._la1 = None
        self._la2 = None
        self._na = None
        self._oc = None
        self._tr = None
        self._ru = None
        self._ph = None
        self._sg = None
        self._th = None
        self._tw = None
        self._vn = None

    @property
    def esport(self):
        if self._esport is None:
            self._esport = PyltoverServerSpecific(esports_server, self.riot_token)
        return self._esport

    # Regional

    @property
    def americas(self):
        if self._americas is None:
            self._americas = PyltoverServerSpecific(RegionalRoutingValues.AMERICAS.value, self.riot_token)
        return self._americas

    @property
    def asia(self):
        if self._asia is None:
            self._asia = PyltoverServerSpecific(RegionalRoutingValues.ASIA.value, self.riot_token)
        return self._asia

    @property
    def sea(self):
        if self._sea is None:
            self._sea = PyltoverServerSpecific(RegionalRoutingValues.SEA.value, self.riot_token)
        return self._sea

    @property
    def europe(self):
        if self._europe is None:
            self._europe = PyltoverServerSpecific(RegionalRoutingValues.EUROPE.value, self.riot_token)
        return self._europe

    # Platforms

    @property
    def br(self):
        if self._br is None:
            self._br = PyltoverServerSpecific(PlatformRoutingValues.BR1.value, self.riot_token)
        return self._br

    @property
    def eune(self):
        if self._eune is None:
            self._eune = PyltoverServerSpecific(PlatformRoutingValues.EUN1.value, self.riot_token)
        return self._eune

    @property
    def euw(self):
        if self._euw is None:
            self._euw = PyltoverServerSpecific(PlatformRoutingValues.EUW1.value, self.riot_token)
        return self._euw

    @property
    def jp(self):
        if self._jp is None:
            self._jp = PyltoverServerSpecific(PlatformRoutingValues.JP1.value, self.riot_token)
        return self._jp

    @property
    def kr(self):
        if self._kr is None:
            self._kr = PyltoverServerSpecific(PlatformRoutingValues.KR.value, self.riot_token)
        return self._kr

    @property
    def la1(self):
        if self._la1 is None:
            self._la1 = PyltoverServerSpecific(PlatformRoutingValues.LA1.value, self.riot_token)
        return self._la1

    @property
    def la2(self):
        if self._la2 is None:
            self._la2 = PyltoverServerSpecific(PlatformRoutingValues.LA2.value, self.riot_token)
        return self._la2

    @property
    def na(self):
        if self._na is None:
            self._na = PyltoverServerSpecific(PlatformRoutingValues.NA1.value, self.riot_token)
        return self._na

    @property
    def oc(self):
        if self._oc is None:
            self._oc = PyltoverServerSpecific(PlatformRoutingValues.OC1.value, self.riot_token)
        return self._oc

    @property
    def tr(self):
        if self._tr is None:
            self._tr = PyltoverServerSpecific(PlatformRoutingValues.TR1.value, self.riot_token)
        return self._tr

    @property
    def ru(self):
        if self._ru is None:
            self._ru = PyltoverServerSpecific(PlatformRoutingValues.RU.value, self.riot_token)
        return self._ru

    @property
    def ph(self):
        if self._ph is None:
            self._ph = PyltoverServerSpecific(PlatformRoutingValues.PH2.value, self.riot_token)
        return self._ph

    @property
    def sg(self):
        if self._sg is None:
            self._sg = PyltoverServerSpecific(PlatformRoutingValues.SG2.value, self.riot_token)
        return self._sg

    @property
    def th(self):
        if self._th is None:
            self._th = PyltoverServerSpecific(PlatformRoutingValues.TH2.value, self.riot_token)
        return self._th

    @property
    def tw(self):
        if self._tw is None:
            self._tw = PyltoverServerSpecific(PlatformRoutingValues.TW2.value, self.riot_token)
        return self._tw

    @property
    def vn(self):
        if self._vn is None:
            self._vn = PyltoverServerSpecific(PlatformRoutingValues.VN2.value, self.riot_token)
        return self._vn


class PyltoverServerSpecific(BasePyltover):
    def __init__(self, server_addr: servers.ServerAddress, riot_token: str):
        self.server_addr = server_addr

        self.v1 = v1.Pyltover(self.server_addr, riot_token)
        # self.v2 = v2.Pyltover(self.server_addr, self.riot_token)
        # self.v3 = v3.Pyltover(self.server_addr, self.riot_token)
        self.v4 = v4.Pyltover(self.server_addr, riot_token)
        # self.v5 = v5.Pyltover(self.server_addr, self.riot_token)
