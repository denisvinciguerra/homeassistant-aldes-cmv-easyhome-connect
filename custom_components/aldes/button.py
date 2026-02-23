"""Support for the Aldes buttons."""
import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, FRIENDLY_NAMES
from .entity import AldesEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add Aldes buttons from a config_entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    buttons: list[AldesRefreshButton] = []

    for product in coordinator.data:
        buttons.append(
            AldesRefreshButton(
                coordinator,
                entry,
                product["serial_number"],
                product["reference"],
                product["modem"],
            )
        )

    async_add_entities(buttons)


class AldesRefreshButton(AldesEntity, ButtonEntity):
    """Button to manually refresh data from Aldes cloud."""

    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_translation_key = "refresh"

    def __init__(
        self,
        coordinator,
        config_entry,
        product_serial_number,
        reference,
        modem,
    ) -> None:
        super().__init__(
            coordinator, config_entry, product_serial_number, reference, modem
        )
        self._attr_icon = "mdi:refresh"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{FRIENDLY_NAMES[self.reference]}_{self.product_serial_number}_refresh"

    async def async_press(self) -> None:
        """Handle the button press."""
        refreshed = await self.coordinator.async_manual_refresh()
        if not refreshed:
            _LOGGER.warning(
                "Refresh ignored for %s — cooldown active (30s)",
                self.product_serial_number,
            )
