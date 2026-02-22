# Changelog

## v2.1.0

- 🔀 **Repository renamed** to `homeassistant-aldes-cmv-easyhome-connect` to better reflect the CMV focus
- 📝 **README rewritten** — clarified CMV-only scope, added T.One heat pump redirect to [tiagfernandes fork](https://github.com/tiagfernandes/homeassistant-aldes)
- 🔄 **Reconfigure flow** — update your Aldes credentials without reinstalling
- 🏷️ **Cleaner entity names** — entities use `has_entity_name` so HA composes `<Device> <Sensor>` names properly
- 🔗 Updated all internal links to new repo URL

## v2.0.5

- 🏷️ **Cleaner entity names** — entities now use `has_entity_name` so HA composes names as `<Device> <Sensor>` instead of duplicating the device name. You may need to delete old entities with duplicate names.

## v2.0.4

- 🔄 **Reconfigure flow** — update your Aldes credentials from Settings → Integrations → Aldes → Reconfigure, without deleting and recreating the integration
- 🔗 Fixed documentation links to point to this fork
- 📝 Added `strings.json` for proper HA translation support
- 🌍 Updated translations (en, fr, nb)

## v2.0.3

- ⚡ Fixed "Current Mode Power" sensor showing Unknown (reverted API field path)

## v2.0.2

- 🐛 Fixed multi-device support (multiple units on the same account)
- 🔗 Fixed sensors not being linked to their device in Home Assistant
- 🔄 Fixed sensor value reading (loop exiting after first product)
- 🎚️ Fixed select entity mode detection
- ⏳ Fixed missing `await` on API auth retry
- 📦 Moved `device_info` to base entity class for proper device grouping
- ✨ Modernized code (`asyncio.timeout`, enum device classes, removed deprecated APIs)
