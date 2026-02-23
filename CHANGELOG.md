# Changelog

## v2.2.3

- Increased delay before cloud refresh after mode change from 5s to 15s (Aldes cloud is slow to propagate)

## v2.2.2

- Fixed mode change showing stale state — HA now updates optimistically and waits before refreshing from Aldes cloud

## v2.2.1

- Renamed `PwmQai` sensor to "Internal Sensor Setpoint" (was "Fan Speed") — motor speed setpoint from built-in air quality algorithm
- Renamed `In0_10V` sensor to "External Sensor Setpoint" (was "0-10V Input") — motor speed setpoint from external 0-10V input
- Both sensors now display raw values (0–1000) without unit

## v2.2.0

- **3 new diagnostic sensors**: 0-10V Input (voltage setpoint), Kitchen Timer (TimCu), Effective Ventilation Mode (ConVe)
- Added "cov" (VOC) to the dominant pollutant mapping
- Translations for new sensors in all 13 languages

## v2.1.5

- 🏷️ **Renamed integration** to "Aldes EasyHome" (was just "Aldes")

## v2.1.4

- 🐛 **Fixed entity translations** — entity names now properly display in the user's language (French, German, etc.) instead of always English
- 🏷️ Removed hardcoded `name=` from sensor descriptions so `translation_key` takes effect

## v2.1.3

- 🌍 **Translations in 13 languages** — entity names translated in en, fr, de, es, it, nb, pt-BR, pl, ru, zh-Hans, ja, ko, sv
- 🏷️ **Fixed English sensor names** — "Polluant Dominant" → "Dominant Pollutant", "Carbon dioxyde" → "Carbon Dioxide"

## v2.1.2

- 🌀 **New Fan Speed sensor** — exposes the fan speed in RPM (`PwmQai`)

## v2.1.1

- 🔢 **Rounded sensor values** — humidity sensors now display as integers (no more 15-digit decimals), temperatures rounded to 0.1°C
- 🗑️ **Removed fake "Current Mode Power" sensor** — was a duplicate of Humidity Variation incorrectly labeled as watts

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
