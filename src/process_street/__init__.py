import dataclasses

import httpx


@dataclasses.dataclass
class ProcessStreetClient:
    api_key: str
    base_url: str = "https://public-api.process.st/api/v1.1"

    def call(self, url: str, method: str = "GET"):
        headers = {"X-API-Key": self.api_key}
        with httpx.Client(base_url=self.base_url, headers=headers) as client:
            r = client.request(method, url)
            r.raise_for_status()
            return r.json()

    @property
    def data_sets(self) -> list["DataSet"]:
        return [DataSet(d) for d in self.get_data_sets().get("dataSets")]

    def get_data_sets(self):
        return self.call("/data-sets")

    def get_test_auth(self):
        return self.call("/testAuth")


class DataSet:
    def __init__(self, data: dict):
        self.data = data

    @property
    def fields(self) -> list["DataSetField"]:
        return [DataSetField(f) for f in self.data.get("fields")]

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def organization_id(self) -> str:
        return self.data.get("organizationId")

    @property
    def name(self) -> str:
        return self.data.get("name")


class DataSetField:
    def __init__(self, data: dict):
        self.data = data

    @property
    def field_type(self) -> str:
        return self.data.get("fieldType")

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def name(self) -> str:
        return self.data.get("name")
