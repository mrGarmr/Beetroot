# SuperFastPython.com
# Example of a chat client using asyncio streams
import sys
import asyncio


# Send messages to server
async def write_messages(writer):
    while True:
        message = await asyncio.to_thread(sys.stdin.readline)
        msg_bytes = message.encode()
        writer.write(msg_bytes)
        await writer.drain()

        if message.strip().lower() == "quit":
            break

    print("Quitting...")


# Read messages from the server
async def read_messages(reader, writer):
    while True:
        try:
            result_bytes = await reader.readline()
            response = result_bytes.decode().strip()

            if not response:
                break  # Connection closed

            print(response)

            # If the server kicks the client, shut down the client
            if response.lower() == "you have been kicked from the server.":
                print("You were kicked. Exiting...")
                writer.close()
                await writer.wait_closed()
                break
                # sys.exit(0)  # Exit the script immediately

        except asyncio.CancelledError:
            break


# Client main function
async def main():
    server_address, server_port = "127.0.0.1", 8888
    print(f"Connecting to {server_address}:{server_port}...")

    reader, writer = await asyncio.open_connection(server_address, server_port)
    print("Connected.")

    read_task = asyncio.create_task(read_messages(reader, writer))
    await write_messages(writer)

    read_task.cancel()
    print("Disconnecting from server...")
    writer.close()
    await writer.wait_closed()
    print("Done.")


# Run the client
asyncio.run(main())
