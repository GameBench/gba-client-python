import gba

client_factory = gba.ClientFactory()
client = client_factory.create()

devices = client.list_devices()

client.get_device("foo")

client.list_device_apps("foo")

session = client.start_session("foo", "bar")
print(session)

# sleep(10)

client.stop_session("baz")

client.sync()

for device in devices:
    print("*", device["name"], device["id"])
    apps = client.list_device_apps(device["id"])

    for app in apps:
        print("", "*", app["identifier"])
