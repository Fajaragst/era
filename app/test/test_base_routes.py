import pytest
from app.test.test_app import TestApp


class BaseTestRoutes(TestApp):

    def _request(self, client, url, params=None):

        return client(
            url,
            json=params
        )

    def add(self, params, url):

        return self._request(
            client=self._client.post,
            params=params,
            url=url)

    def show(self, url):

        return self._request(
            client=self._client.get,
            url=url)