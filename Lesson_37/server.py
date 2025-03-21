# SuperFastPython.com
# example of a chat server using streams
import asyncio

ADMIN_NAME = "user123"

# Store all connected users
ALL_USERS = {}


# Write a message to a stream writer
async def write_message(writer, msg_bytes):
    writer.write(msg_bytes)
    await writer.drain()


# Send a message to all connected users
async def broadcast_message(message):
    print(f"Broadcast: {message.strip()}")  # Log broadcast
    msg_bytes = message.encode()
    tasks = [
        asyncio.create_task(write_message(w, msg_bytes))
        for _, (_, w) in ALL_USERS.items()
    ]
    await asyncio.wait(tasks)


# Connect a user
async def connect_user(reader, writer):
    writer.write("Asyncio Chat Server\n".encode())
    writer.write("Enter your name:\n".encode())
    await writer.drain()

    name_bytes = await reader.readline()
    name = name_bytes.decode().strip()

    if name in ALL_USERS:
        writer.write("Name already taken. Try another name.\n".encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return None  # Return None if name is already taken

    ALL_USERS[name] = (reader, writer)
    await broadcast_message(f"{name} has connected\n")

    writer.write(f"Welcome {name}. Send QUIT to disconnect.\n".encode())
    await writer.drain()

    return name


# Disconnect a user
async def disconnect_user(name):
    if name in ALL_USERS:
        _, writer = ALL_USERS.pop(name)
        writer.write("You have been kicked from the server.\n".encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        await broadcast_message(f"{name} has been kicked from the server.\n")


# Send a private message
async def send_message(name, user, message):
    if user not in ALL_USERS:
        print("This user does not exist!")
        return

    msg_bytes = (name + ": " + message + "\n").encode()
    writer = ALL_USERS[user][1]
    await write_message(writer, msg_bytes)


# Handle a chat client
async def handle_chat_client(reader, writer):
    print("Client connecting...")
    name = await connect_user(reader, writer)

    if name is None:
        return  # Exit if connection failed

    try:
        while True:
            line_bytes = await reader.readline()
            if not line_bytes:
                break  # Exit if connection is closed

            message = line_bytes.decode().strip()

            if message.lower() == "quit":
                break  # User wants to leave

            elif message.lower().startswith("pm:"):
                _, username, msg = message.split(":", 2)
                await send_message(name, username, msg)

            elif message.lower().startswith("kick:") and name == ADMIN_NAME:
                _, user = message.split(":", 1)
                if user in ALL_USERS:
                    await disconnect_user(user)

                else:
                    writer.write(f"User {user} not found.\n".encode())
                    await writer.drain()

            else:
                await broadcast_message(f"{name}: {message}\n")
    finally:
        if name in ALL_USERS:
            del ALL_USERS[name]
        writer.close()
        await writer.wait_closed()
        await broadcast_message(f"{name} has disconnected\n")


# Chat server entry point
async def main():
    host_address, host_port = "127.0.0.1", 8888
    server = await asyncio.start_server(handle_chat_client, host_address, host_port)

    async with server:
        print("Chat Server Running\nWaiting for chat clients...")
        await server.serve_forever()


# Run the event loop
asyncio.run(main())
