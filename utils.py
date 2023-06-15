from prefect import get_client, get_cloud_client
from prefect.utilities.asyncutils import sync_compatible


@sync_compatible
async def get(route):
    """GET any route with the orchestration client"""
    async with get_client() as client:
        response = await client._client.get(url=route)
    return response.json()


@sync_compatible
async def post(route, payload=None):
    """POST any route with the orchestration client"""
    async with get_client() as client:
        response = await client._client.post(url=route, json=payload)
    return response.json()


@sync_compatible
async def put(route, payload=None):
    """PUT any route with the orchestration client"""
    async with get_client() as client:
        response = await client._client.put(url=route, json=payload)
    return response


@sync_compatible
async def get_cloud(route):
    """GET any route with the cloud client"""
    # Note: automatically returns JSON
    async with get_cloud_client() as client:
        response = await client.get(route=route)
    return response
