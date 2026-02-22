"""Support for the Aldes selects."""
import logging

from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, FRIENDLY_NAMES, MODES_TEXT, TEXT_MODES
from .entity import AldesEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add Aldes selects from a config_entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    selects: list[AldesSelectEntity] = []

    for product in coordinator.data:
        for data_line in product.get("indicators", []):
            if data_line.get("type") == "MODE":
                mode_value = data_line.get("value")
                mode_text = MODES_TEXT.get(mode_value)
                if mode_text is None:
                    _LOGGER.warning("Unknown Aldes mode value: %s", mode_value)
                    mode_text = "Daily"
                selects.append(
                    AldesSelectEntity(
                        coordinator,
                        entry,
                        product["serial_number"],
                        product["reference"],
                        product["modem"],
                        mode_text,
                    )
                )

    async_add_entities(selects)


class AldesSelectEntity(AldesEntity, SelectEntity):
    """Define an Aldes select."""

    _attr_entity_category = EntityCategory.CONFIG

    def __init__(
        self,
        coordinator,
        config_entry,
        product_serial_number,
        reference,
        modem,
        mode,
    ) -> None:
        super().__init__(
            coordinator, config_entry, product_serial_number, reference, modem
        )
        self._attr_icon = "mdi:tune"
        self._attr_options = list(TEXT_MODES.keys())
        self._mode = mode

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{FRIENDLY_NAMES[self.reference]}_{self.product_serial_number}_mode"

    @property
    def name(self):
        """Return a name to use for this entity."""
        return f"{FRIENDLY_NAMES[self.reference]} {self.product_serial_number} mode"

    @property
    def current_option(self) -> str:
        return self._mode

    async def async_select_option(self, option: str) -> None:
        """Set mode."""
        await self.coordinator.api.set_mode(self.modem, option)
        self._mode = option
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update attributes when the coordinator updates."""
        for product in self.coordinator.data:
            if product["serial_number"] == self.product_serial_number:
                for data_line in product.get("indicators", []):
                    if data_line.get("type") == "MODE":
                        mode_text = MODES_TEXT.get(data_line.get("value"))
                        if mode_text is not None:
                            self._mode = mode_text
                break
        super()._handle_coordinator_update()
