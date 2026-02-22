# Changelog

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
