# Aldes integration for Home Assistant

This integration allows Home Assistant to interact with **Aldes EASYHOME PureAir Compact CONNECT** ventilation units (VMC simple flux) through an **Aldes Connect Box**.

Setup validated with **2 VMCs linked to the same Aldes account**.

## Supported features

- Binary sensor to check product connectivity to Aldes cloud
- Temperature sensors for each room (kitchen, bathrooms)
- Humidity sensors for each room
- CO2 sensor
- Air Quality Index (QAI) sensor
- Dominant pollutant sensor
- Humidity variation sensor
- Current mode power sensor
- Climate entities for rooms with target temperature control (T.One AIR)
- Select entity to change VMC mode: Holidays, Daily, Boost, Guest, Air Prog

## Installation

Available through [HACS](https://hacs.xyz/) as a custom repository.

1. In HACS, go to **Integrations** > **3 dots menu** > **Custom repositories**
2. Add `https://github.com/denisvinciguerra/homeassistant-aldes` with category **Integration**
3. Install the integration, restart Home Assistant
4. Go to **Settings** > **Integrations** > **Add Integration** > search **Aldes**
5. Enter your Aldes account credentials (same as the Aldes mobile app)

## About this fork

This is a fork of [homeassistant-aldes](https://github.com/guix77/homeassistant-aldes/) by [guix77](https://github.com/guix77), debugged via vibe coding with Claude.

The original author archived his repository. Other existing forks appear to focus on different Aldes products (T.One AIR, InspirAIR, etc.) rather than the single-flow EASYHOME PureAir Compact CONNECT VMCs.

### Changes from the original

- Fixed multi-device support (multiple VMCs on the same account)
- Fixed sensors not being linked to their device in Home Assistant
- Fixed sensor value reading (loop exiting after first product)
- Fixed select entity mode detection
- Fixed missing `await` on API auth retry
- Moved `device_info` to base entity class for proper device grouping
- Modernized code (`asyncio.timeout`, enum device classes, removed deprecated APIs)

## Credits

- Original integration by [guix77](https://github.com/guix77)
- Some code inspired from [hassio_aldes](https://github.com/aalmazanarbs/hassio_aldes)
- Based on [integration_blueprint](https://github.com/custom-components/integration_blueprint)
