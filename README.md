# 🌀 Aldes CMV integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

This integration brings **Aldes CMV (Controlled Mechanical Ventilation) units equipped with an Aldes Connect Box** into Home Assistant, giving you full visibility and control over your ventilation system.

✅ Validated with **2 single-flow EASYHOME PureAir Compact CONNECT units on the same Aldes account**

> **⚠️ Looking for T.One heat pump support?**
> This integration is focused on CMV units only. Using T.One with this integration is **untested and not recommended**.
> For the **T.One AIR heat pump**, I recommend having a look at [this fork by tiagfernandes](https://github.com/tiagfernandes/homeassistant-aldes) instead. 

---

## 🔎 Supported features

| Entity | Description |
|--------|-------------|
| 📡 Binary sensor | Product connectivity to Aldes cloud |
| 🌡️ Temperature | Per-room sensors (kitchen, bathrooms) |
| 💧 Humidity | Per-room sensors (kitchen, bathrooms) |
| 💨 CO2 | Carbon dioxide concentration (ppm) |
| 🍃 Air Quality Index | QAI value from the unit |
| 🌿 Dominant pollutant | Currently dominant pollutant |
| 📊 Humidity variation | Humidity variation rate |
| 🌀 Fan speed | Fan speed (RPM) |
| ⚡ 0-10V Input | External input voltage setpoint (V) |
| ⏲️ Kitchen Timer | Kitchen boost timer state |
| 🔄 Effective Ventilation Mode | Actual ventilation mode reported by the unit |
| 🎛️ Mode selector | Switch between Holidays, Daily, Boost, Guest, Air Prog |

---

## 📦 Installation

Available through [HACS](https://hacs.xyz/) as a custom repository.

1. In HACS, go to **Integrations** → ⋮ **Custom repositories**
2. Add `https://github.com/denisvinciguerra/homeassistant-aldes-cmv-easyhome-connect` with category **Integration**
3. Install the integration and restart Home Assistant
4. Go to **Settings** → **Integrations** → **Add Integration** → search **Aldes**
5. Enter your Aldes account credentials (same as the Aldes mobile app) 🔑

---

## 🔀 About this fork

This is a fork of [homeassistant-aldes](https://github.com/guix77/homeassistant-aldes/) by [guix77](https://github.com/guix77), debugged via vibe coding with Claude 🤖

The original author archived his repository. Other existing forks appear to focus on different Aldes products (T.One AIR, InspirAIR, etc.) rather than the single-flow **EASYHOME PureAir Compact CONNECT** CMV units.

### 🛠️ Changes from the original

- 🐛 Fixed multi-device support (multiple units on the same account)
- 🔗 Fixed sensors not being linked to their device in Home Assistant
- 🔄 Fixed sensor value reading (loop exiting after first product)
- 🎚️ Fixed select entity mode detection
- ⏳ Fixed missing `await` on API auth retry
- 📦 Moved `device_info` to base entity class for proper device grouping
- 🏷️ Cleaner entity names with `has_entity_name`
- 🔄 Reconfigure flow to update credentials without reinstalling
- ✨ Modernized code (`asyncio.timeout`, enum device classes, removed deprecated APIs)

---

## 🙏 Credits

- Original integration by [guix77](https://github.com/guix77)
- Some code inspired from [hassio_aldes](https://github.com/aalmazanarbs/hassio_aldes)
- Based on [integration_blueprint](https://github.com/custom-components/integration_blueprint)
