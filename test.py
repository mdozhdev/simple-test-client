import asyncio
import websockets
import time
import os


WS_URL = os.environ.get("WS_URL", "ws://0.0.0.0:8000")
CHUNK_SIZE = 4096  # bytes
AUDIO_FILE = "sample.wav"  # MUST be WAV


# Determine if authentication is required
ID_TOKEN = os.environ.get("ID_TOKEN", None)


async def test_transcription():
    headers = {}
    if ID_TOKEN:
        headers["Authorization"] = f"Bearer {ID_TOKEN}"

    async with websockets.connect(
        WS_URL,
        max_size=None,
        additional_headers=headers,
    ) as ws:
        print("Connected to server")

        with open(AUDIO_FILE, "rb") as f:
            chunk_count = 0
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break

                await ws.send(chunk)
                chunk_count += 1
                print(f"Sent chunk {chunk_count}")

                # Simulate realtime streaming
                await asyncio.sleep(0.05)

                # Receive server messages (non-blocking)
                try:
                    response = await asyncio.wait_for(ws.recv(), timeout=0.01)
                    print("Server:", response)
                except asyncio.TimeoutError:
                    pass

        print("Finished sending audio")

        # Keep listening for final messages
        while True:
            try:
                response = await asyncio.wait_for(ws.recv(), timeout=2)
                print("Server:", response)
            except asyncio.TimeoutError:
                break


asyncio.run(test_transcription())
