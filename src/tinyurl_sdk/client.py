from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import httpx

from .exceptions import TinyURLClientError, TinyURLHTTPError, TinyURLResponseError

@dataclass
class TinyURLClient:
    api_key: str
    timeout: float = 10.0
    api_base_url: str = "https://api.tinyurl.com"
    user_agent: str = "tinyurl-sdk/0.0.0"

    def shorten(
        self,
        url: str,
        domain: Optional[str] = None,
        alias: Optional[str] = None,
        tags: Optional[str] = None,
        expires_at: Optional[str] = None,
        description: Optional[str] = None,
    ) -> str:
        """Create a TinyURL short link for the provided long URL."""
        if not url:
            raise ValueError("url is required")

        return self._shorten_token(
            url,
            domain=domain,
            alias=alias,
            tags=tags,
            expires_at=expires_at,
            description=description,
        )

    def _shorten_token(
        self,
        url: str,
        domain: Optional[str] = None,
        alias: Optional[str] = None,
        tags: Optional[str] = None,
        expires_at: Optional[str] = None,
        description: Optional[str] = None,
    ) -> str:
        if not self.api_key:
            raise TinyURLClientError("api_key is required for token API usage")

        payload = {"url": url}
        if domain:
            payload["domain"] = domain
        if alias:
            payload["alias"] = alias
        if tags:
            payload["tags"] = tags
        if expires_at:
            payload["expires_at"] = expires_at
        if description:
            payload["description"] = description

        url = f"{self.api_base_url.rstrip('/')}/create"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            with httpx.Client(
                timeout=self.timeout,
                headers={"User-Agent": self.user_agent},
            ) as client:
                response = client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPStatusError as exc:
            raise TinyURLHTTPError(
                f"HTTP error {exc.response.status_code}: {exc.response.reason_phrase}"
            ) from exc
        except httpx.RequestError as exc:
            raise TinyURLHTTPError(f"Network error: {exc}") from exc
        except ValueError as exc:
            raise TinyURLResponseError("Token API did not return valid JSON") from exc

        tiny_url = data.get("data", {}).get("tiny_url")
        if not tiny_url:
            raise TinyURLResponseError("Token API response missing tiny_url")

        return tiny_url
