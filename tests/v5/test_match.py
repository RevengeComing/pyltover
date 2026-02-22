from pyltover.apis.v5 import Pyltover as V5Pyltover


class _FakeResponse:
    def __init__(self, payload):
        self.status_code = 200
        self._payload = payload

    def json(self):
        return self._payload


class _FakeAsyncClient:
    def __init__(self):
        self.last_url = None
        self.last_params = None

    async def get(self, url, params=None):
        self.last_url = url
        self.last_params = params
        return _FakeResponse(["NA1_123"])


async def test_get_list_of_match_ids_by_puuid_uses_default_query_params():
    client = _FakeAsyncClient()
    api = V5Pyltover("europe.api.riotgames.com", "token")
    V5Pyltover.async_client = client

    response = await api.get_list_of_match_ids_by_puuid("some-puuid")

    assert response == ["NA1_123"]
    assert client.last_params == {"start": 0, "count": 20}


async def test_get_list_of_match_ids_by_puuid_uses_all_supported_query_params():
    client = _FakeAsyncClient()
    api = V5Pyltover("europe.api.riotgames.com", "token")
    V5Pyltover.async_client = client

    response = await api.get_list_of_match_ids_by_puuid(
        "some-puuid",
        startTime=1700000000,
        endTime=1700009999,
        queue=420,
        type="ranked",
        start=10,
        count=50,
    )

    assert response == ["NA1_123"]
    assert client.last_params == {
        "startTime": 1700000000,
        "endTime": 1700009999,
        "queue": 420,
        "type": "ranked",
        "start": 10,
        "count": 50,
    }
