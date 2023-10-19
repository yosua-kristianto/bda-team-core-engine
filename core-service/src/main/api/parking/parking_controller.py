"""
1. Get parking price data from plate number (POST)

Header:
Content-Type: application/json

Request:

```
{
    "plate": "B1100FF"
}

Response

```
{
    "in": "2023-10-19 14:00:00",
    "out": "2023-10-19 15:00:00", // Get from current date
    "price": 10000
}
```

"""

"""
2. Mock parking payment (POST)

This API intended to simulate payment process.

Header:
Content-Type: application/json

Request:

```
{
    "plate": "B1100FF"
}

Response

```
null
```

"""