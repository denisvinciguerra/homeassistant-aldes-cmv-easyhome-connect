"""Aldes data coordinator."""
from __future__ import annotations

import asyncio
from datetime import timedelta
import logging
import time
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import AldesApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

MANUAL_REFRESH_COOLDOWN = 30


class AldesDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Aldes data coordinator."""

    _API_TIMEOUT = 10

    def __init__(self, hass: HomeAssistant, api: AldesApi) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=5),
        )
        self.api = api
        self._last_manual_refresh: float = 0

    async def async_manual_refresh(self) -> bool:
        """Request a manual refresh with cooldown protection.

        Returns True if refresh was triggered, False if cooldown blocked it.
        """
        now = time.monotonic()
        elapsed = now - self._last_manual_refresh
        if elapsed < MANUAL_REFRESH_COOLDOWN:
            remaining = round(MANUAL_REFRESH_COOLDOWN - elapsed)
            _LOGGER.debug(
                "Manual refresh blocked — cooldown active, %ds remaining", remaining
            )
            return False
        _LOGGER.debug("Manual refresh triggered")
        self._last_manual_refresh = now
        await self.async_request_refresh()
        return True

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        try:
            async with asyncio.timeout(self._API_TIMEOUT):
                data = await self.api.fetch_data()
                for product in data:
                    _LOGGER.debug(
                        "Aldes API response for %s: indicator keys = %s",
                        product.get("serial_number"),
                        list(product.get("indicator", {}).keys()) if isinstance(product.get("indicator"), dict) else "N/A",
                    )
                    _LOGGER.debug(
                        "Aldes API full indicator for %s: %s",
                        product.get("serial_number"),
                        product.get("indicator"),
                    )
                return data
        except Exception as exception:
            raise UpdateFailed(exception) from exception
