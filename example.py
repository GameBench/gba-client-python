import gba

client_factory = gba.ClientFactory()
client = client_factory.create()

devices = client.list_devices()

try:
    client.get_device("foo")
except gba.DeviceNotFoundError:
    print("Device not found")

try:
    client.list_device_apps("foo")
except gba.DeviceNotFoundError:
    print("Device not found")

try:
    session = client.start_session("foo", "bar")
    print(session)
except gba.ServerError:
    print("Failed to start session")
except gba.InvalidAuthCredentialsError:
    print("Invalid auth credentials")

# sleep(10)

try:
    client.stop_session("baz")
except gba.SessionNotFoundError:
    print("Session not found")

client.sync()

for device in devices:
    print("*", device["name"], device["id"])
    apps = client.list_device_apps(device["id"])

    for app in apps:
        print("", "*", app["identifier"])
