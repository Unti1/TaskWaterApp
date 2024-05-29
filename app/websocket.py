from settings import *
from .models import Store

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict = {}

    async def connect(self, websocket: WebSocket, store_id: str):
        await websocket.accept()
        if store_id not in self.active_connections:
            self.active_connections[store_id] = []
        self.active_connections[store_id].append(websocket)

    def disconnect(self, websocket: WebSocket, store_id: str):
        self.active_connections[store_id].remove(websocket)
        if not self.active_connections[store_id]:
            del self.active_connections[store_id]

    async def send_personal_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: dict, store_id: str):
        if store_id in self.active_connections:
            for connection in self.active_connections[store_id]:
                await connection.send_json(message)

manager = ConnectionManager()

@router.websocket("/ws/{store_id}")
async def websocket_endpoint(websocket: WebSocket, store_id: str):
    await manager.connect(websocket, store_id)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket, store_id)
