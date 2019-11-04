import gba_client

client_factory = gba_client.ClientFactory()
client = client_factory.create()

devices = client.list_devices()

try:
    client.get_device("foo")
except gba_client.DeviceNotFoundError:
    print("Device not found")

try:
    client.list_device_apps("foo")
except gba_client.DeviceNotFoundError:
    print("Device not found")

try:
    session = client.start_session("foo", "bar")
    print(session)
except gba_client.ServerError:
    print("Failed to start session")
except gba_client.InvalidAuthCredentialsError:
    print("Invalid auth credentials")

# sleep(10)

try:
    client.stop_session("baz")
except gba_client.SessionNotFoundError:
    print("Session not found")

client.sync()

for device in devices:
    print("*", device["name"], device["id"])
    apps = client.list_device_apps(device["id"])

    for app in apps:
        print("", "*", app["identifier"])
