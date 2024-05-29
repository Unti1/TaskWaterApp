import asyncio
import pytest
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_websocket():
    async with client.websocket_connect("/ws/test_store") as websocket:
        await websocket.send_json({"message": "test"})
        data = await websocket.receive_json()
        assert data == {"message": "test"}
