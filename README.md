# 🌬️ Aldes integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Home Assistant custom integration for **Aldes EASYHOME PureAir Compact CONNECT** single-flow controlled mechanical ventilation (CMV) units via the **Aldes Connect Box**.

✅ Setup validated with **2 units linked to the same Aldes account**

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
| ⚡ Current mode power | Active mode power level |
| 🎛️ Mode selector | Switch between Holidays, Daily, Boost, Guest, Air Prog |
| 🏠 Climate | Target temperature control (T.One AIR) |

---

## 📦 Installation

Available through [HACS](https://hacs.xyz/) as a custom repository.

1. In HACS, go to **Integrations** → ⋮ **Custom repositories**
2. Add `https://github.com/denisvinciguerra/homeassistant-aldes` with category **Integration**
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
- ✨ Modernized code (`asyncio.timeout`, enum device classes, removed deprecated APIs)

---

## 🙏 Credits

- Original integration by [guix77](https://github.com/guix77)
- Some code inspired from [hassio_aldes](https://github.com/aalmazanarbs/hassio_aldes)
- Based on [integration_blueprint](https://github.com/custom-components/integration_blueprint)
