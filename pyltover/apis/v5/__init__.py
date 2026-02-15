from pyltover.base import BasePyltover
from pyltover.apis.v5 import schema
from pyltover.apis.v5 import urls


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr

    async def get_list_of_match_ids_by_puuid(self, puuid: str) -> list[str]:
        url = urls.get_list_of_match_ids_by_puuid.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            return self._response_json(resp, "v5.get_list_of_match_ids_by_puuid")
        else:
            self._raise_riot_api_error(resp, "v5.get_list_of_match_ids_by_puuid")

    async def get_match_by_id(self, match_id: str) -> schema.Match:
        url = urls.get_match_by_id.format(server_addr=self.server_addr, match_id=match_id)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            return self._model_validate_json(schema.Match, resp.text, "v5.get_match_by_id", resp)
        else:
            self._raise_riot_api_error(resp, "v5.get_match_by_id")

    async def get_match_timeline_by_id(self, puuid: str) -> schema.MatchTimeline:
        url = urls.get_match_timeline_by_id.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            return schema.MatchTimeline()
        else:
            self._raise_riot_api_error(resp, "v5.get_match_timeline_by_id")
