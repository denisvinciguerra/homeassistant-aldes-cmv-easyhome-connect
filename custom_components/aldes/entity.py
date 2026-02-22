"""AldesEntity class."""
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, FRIENDLY_NAMES, MANUFACTURER


class AldesEntity(CoordinatorEntity):
    """Base Aldes entity."""

    _attr_has_entity_name = True

    def __init__(
        self, coordinator, config_entry, product_serial_number, reference, modem
    ) -> None:
        super().__init__(coordinator)
        self._attr_config_entry = config_entry
        self.product_serial_number = product_serial_number
        self.reference = reference
        self.modem = modem

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info — groups all entities under one device per product."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.product_serial_number)},
            manufacturer=MANUFACTURER,
            name=f"{FRIENDLY_NAMES.get(self.reference, self.reference)} {self.product_serial_number}",
            model=FRIENDLY_NAMES.get(self.reference, self.reference),
        )
