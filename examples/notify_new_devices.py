import logging

from bluezero import tools
from bluezero import adapter
from bluezero import device

logging.getLogger('bluezero.adapter').setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)

dongle = adapter.Adapter(adapter.list_adapters()[0])
print(dongle.name)
dongle.powered = True


def dev_add(device_found, device_prop_keys):
    print('Added device name: {}'.format(device_found.alias))
    for prop in device_prop_keys:
        print('\t{} = {}'.format(prop, getattr(device_found, prop)))


def dev_changed(device_changed, device_prop_changed):
    print('Changed device name: {}'.format(device_changed.alias))
    for prop in device_prop_changed:
        print('\t{} = {}'.format(prop, getattr(device_changed, prop)))


def dev_removed(device_id):
    print('Removed device ID: {}'.format(device_id))

adapter.Adapter.on_device_added = dev_add
adapter.Adapter.on_device_prop_changed = dev_changed
adapter.Adapter.on_device_removed = dev_removed

dongle.nearby_discovery(15)

for device_obj in device.Device._instances:

    print('We have the following: {} {}'.format(
        device_obj.alias,
        device_obj.address))

tools.start_mainloop()
