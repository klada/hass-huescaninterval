# hass-huescaninterval

This custom component allows you to modify the `scan_interval` of Home Assistant's official Hue integration. This enables you to use devices such as buttons and motion sensors with a much smaller delay.

The code is based on the approach of [Hue-remotes-HASS](https://github.com/robmarkcole/Hue-remotes-HASS). Special thanks to [@robmarkcole](https://github.com/robmarkcole).

## :warning: Warning

This component lowers the `scan_interval` of your Hue bridge to 0.5 seconds. Depending on your environment your Hue Bridge may become unstable! There is a reason why the HASS core developers will not lower the scan interval by default!

This component does not add any device support. All it does is adjusting the scan interval. Everything else you need for processing Hue events is included in recent versions of Home Assistant.

## Installation

1. Place the `huescaninterval` folder into your `custom_components` directory.
2. Add this to your `configuration.yaml`:
```yaml
huescaninterval:
```

## Reacting to button events in automations

This is a sample automation which reacts to the large Hue Tap button:

```yaml
- alias: Tap Automation Demo
  trigger:
    - platform: event
      event_type: hue_event
      event_data:
        id: hue_tap_1
        event: 34
  condition: []
  action:
    - service: light.toggle
      entity_id: light.demo_light
```

## Inspecting button events

You can use Home Assistant's event listener to get the events of your Hue sensors and buttons:

1. Open the Developer Tools in Home Assistant
2. Click on Events
3. Start listening for `hue_event` events and use the ids and events from the inspector in your automations :grin:


