def capabilityRegistryStopProvider(container, provider, capability=None):

    if capability:
        print('container: ', container)
        print('provider: ', provider)
    else:
        print('capability not specified')


capabilityRegistryStopProvider('testcontainer', 'testprovider', 'capability')

