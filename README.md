# tinyurl-sdk

A lightweight Python SDK for simplifying TinyURL link creation and management.

## Installation

```bash
pip install tinyurl-sdk
```

## Usage

```python
from tinyurl_sdk.client import TinyURLClient

client = TinyURLClient(api_key="YOUR_API_KEY")
short_url = client.shorten(
    url="https://www.example.com/my-really-long-link-that-I-need-to-shorten/84378949",
    domain="tinyurl.com",
    alias="myexamplelink",
    tags="example,link",
    expires_at="2024-10-25 10:11:12",
    description="string",
)
print(short_url)
```

### Parameters

Constructor:

| Name | Required | Type | Notes |
| --- | --- | --- | --- |
| `api_key` | Yes | `str` | TinyURL API key. |
| `timeout` | No | `float` | Request timeout in seconds. Default: `10.0`. |
| `api_base_url` | No | `str` | Base API URL. Default: `https://api.tinyurl.com`. |
| `user_agent` | No | `str` | User agent header. Default: `tinyurl-sdk/0.0.0`. |

`shorten`:

| Name | Required | Type | Notes |
| --- | --- | --- | --- |
| `url` | Yes | `str` | Long URL to shorten. |
| `domain` | No | `str` | TinyURL domain. |
| `alias` | No | `str` | Must be at least 5 characters if provided. |
| `tags` | No | `str` | Comma-separated tags. |
| `expires_at` | No | `str` | Expiration timestamp (API format). |
| `description` | No | `str` | Link description. |

## Development

```bash
pip install -e .
```

## License

MIT
