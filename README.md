Please note this will only work with GBA version v1.5.0 or greater.

### Create a client

```
client_factory = gba_client.ClientFactory()
client = client_factory.create()
```

You can optionally pass a dictionary when creating the client

```
config = {
    baseUrl: '',
    username: '',
    password: '',
}
client = client_factory.create(config)
```

### List devices

```
client.list_devices()
```
