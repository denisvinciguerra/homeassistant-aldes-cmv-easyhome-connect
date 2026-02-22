"""Support for the Aldes sensors."""
from __future__ import annotations
from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfTemperature,
    PERCENTAGE,
    CONCENTRATION_PARTS_PER_MILLION,
    EntityCategory,
)
from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorEntityDescription,
)
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, FRIENDLY_NAMES, POLLUANTS
from .entity import AldesEntity

from collections.abc import Callable
from dataclasses import dataclass

ATTR_HUMIDITY = "humidity"
ATTR_TEMPERATURE = "temperature"
ATTR_THERMOSTAT = "thermostat"
ATTR_CO2 = "CO2"
ATTR_QAI = "Air Quality Index"
ATTR_POLLUANT = "Polluant Dominant"
ATTR_VARHR = "Humidity Variation"
ATTR_PWRQAI = "Actual mode"


@dataclass
class AldesSensorDescription(SensorEntityDescription):
    """A class that describes sensor entities."""

    attributes: tuple = ()
    keys: list[str] = None
    value: Callable = None
    path1: str = None
    path2: str = None
    path3: str = None
    path2recursive: bool = False
    path2id: str = None
    path2value: str = None


EASY_HOME_SENSORS = {
    f"Kitchen_{ATTR_HUMIDITY}": AldesSensorDescription(
        key="status",
        icon="mdi:water-percent",
        name="Kitchen Humidity",
        translation_key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="HrCuCo",
    ),
    f"Kitchen_{ATTR_TEMPERATURE}": AldesSensorDescription(
        key="status",
        icon="mdi:thermometer",
        name="Kitchen Temperature",
        translation_key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="TmpCu",
        value=lambda value: value / 10,
    ),
    f"Bathroom_1_{ATTR_HUMIDITY}": AldesSensorDescription(
        key="status",
        icon="mdi:water-percent",
        name="Bathroom 1 Humidity",
        translation_key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="HrBa1Co",
    ),
    f"Bathroom_1_{ATTR_TEMPERATURE}": AldesSensorDescription(
        key="status",
        icon="mdi:thermometer",
        name="Bathroom 1 Temperature",
        translation_key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="TmpBa1",
        value=lambda value: value / 10,
    ),
    f"Bathroom_2_{ATTR_HUMIDITY}": AldesSensorDescription(
        key="status",
        icon="mdi:water-percent",
        name="Bathroom 2 Humidity",
        translation_key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="HrBa2Co",
    ),
    f"Bathroom_2_{ATTR_TEMPERATURE}": AldesSensorDescription(
        key="status",
        icon="mdi:thermometer",
        name="Bathroom 2 Temperature",
        translation_key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="TmpBa2",
        value=lambda value: value / 10,
    ),
    f"{ATTR_CO2}": AldesSensorDescription(
        key="status",
        icon="mdi:molecule-co2",
        name="Carbon dioxyde",
        translation_key="co2",
        device_class=SensorDeviceClass.CO2,
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="CO2",
    ),
    f"{ATTR_QAI}": AldesSensorDescription(
        key="status",
        icon="mdi:air-filter",
        name="Air Quality Index",
        translation_key="qai",
        device_class=SensorDeviceClass.AQI,
        native_unit_of_measurement=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="Qai",
        path3="actualValue",
    ),
    f"{ATTR_POLLUANT}": AldesSensorDescription(
        key="status",
        icon="mdi:flower-pollen",
        name="Polluant Dominant",
        translation_key="qai",
        native_unit_of_measurement=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="Qai",
        path3="polluantDominant",
        value=lambda value: POLLUANTS[value],
    ),
    f"{ATTR_VARHR}": AldesSensorDescription(
        key="status",
        icon="mdi:cloud-percent",
        name="Humidity Variation",
        translation_key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="VarHR",
    ),
    f"{ATTR_PWRQAI}": AldesSensorDescription(
        key="status",
        icon="mdi:wind-power",
        name="Current Mode Power",
        translation_key="mode",
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="VarHR",
    ),
}

TONE_AIR_SENSORS = {
    f"{ATTR_THERMOSTAT}": AldesSensorDescription(
        key="status",
        icon="mdi:thermometer",
        name="Thermostat",
        translation_key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        path1="indicator",
        path2="thermostats",
        path2recursive=True,
        path2id="ThermostatId",
        path2value="CurrentTemperature",
        value=lambda value: round(value, 1),
    ),
}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add Aldes sensors from a config_entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[AldesSensorEntity] = []
    for product in coordinator.data:
        if product["reference"] == "EASY_HOME_CONNECT":
            sensors = EASY_HOME_SENSORS
        elif product["reference"] == "TONE_AIR":
            sensors = TONE_AIR_SENSORS
        for sensor, description in sensors.items():
            if description.path2recursive:
                for thermostat in product[description.path1][description.path2]:
                    entities.append(
                        AldesSensorEntity(
                            coordinator,
                            entry,
                            product["serial_number"],
                            product["reference"],
                            product["modem"],
                            thermostat["ThermostatId"],
                            description,
                        )
                    )
            else:
                entities.append(
                    AldesSensorEntity(
                        coordinator,
                        entry,
                        product["serial_number"],
                        product["reference"],
                        product["modem"],
                        sensor,
                        description,
                    )
                )

    async_add_entities(entities)


class AldesSensorEntity(AldesEntity, SensorEntity):
    """Define an Aldes sensor."""

    def __init__(
        self,
        coordinator,
        config_entry,
        product_serial_number,
        reference,
        modem,
        probe_id,
        description,
    ) -> None:
        super().__init__(
            coordinator, config_entry, product_serial_number, reference, modem
        )
        self.probe_id = probe_id
        self.entity_description = description
        self._attr_native_value = self._determine_native_value()

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{FRIENDLY_NAMES[self.reference]}_{self.product_serial_number}_{self.entity_description.name}"

    @property
    def name(self):
        """Return a name to use for this entity."""
        for product in self.coordinator.data:
            if product["serial_number"] == self.product_serial_number:
                if self.entity_description.path2 == "thermostats":
                    for thermostat in product["indicator"]["thermostats"]:
                        if thermostat["ThermostatId"] == self.probe_id:
                            return f"{FRIENDLY_NAMES[self.reference]} {self.product_serial_number} {thermostat['Name']} temperature"
                else:
                    return f"{FRIENDLY_NAMES[self.reference]} {self.product_serial_number} {self.entity_description.name}"
        return None

    def _determine_native_value(self):
        """Determine native value."""
        product = self._find_product()
        if product is None or not product.get("isConnected"):
            return None

        try:
            desc = self.entity_description
            if desc.path2recursive:
                for item in product[desc.path1][desc.path2]:
                    if item[desc.path2id] == self.probe_id:
                        value = item[desc.path2value]
                        break
                else:
                    return None
            elif desc.path3 is None:
                value = product[desc.path1][desc.path2]
            else:
                value = product[desc.path1][desc.path2][desc.path3]
        except (KeyError, TypeError, IndexError):
            return None

        if value is not None and desc.value:
            value = desc.value(value)
        return value

    def _find_product(self):
        """Find this sensor's product in coordinator data."""
        for product in self.coordinator.data:
            if product["serial_number"] == self.product_serial_number:
                return product
        return None

    @callback
    def _handle_coordinator_update(self):
        """Fetch state from the device."""
        native_value = self._determine_native_value()
        if native_value is not None:
            self._attr_native_value = native_value
        super()._handle_coordinator_update()
