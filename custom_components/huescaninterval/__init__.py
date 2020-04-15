from datetime import timedelta
import logging
from homeassistant.components.hue import DOMAIN as HUE_DOMAIN
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.const import CONF_SCAN_INTERVAL

DOMAIN = "huescaninterval"
DEFAULT_SCAN_INTERVAL = timedelta(seconds=0.5)
_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up remote platform by registering it on each Hue Bridge."""
    for bridge_entry_id, bridge in hass.data[HUE_DOMAIN].items():
        # Set up updates at scan_interval
        async def _update_remotes(now=None):
            """Request a bridge data refresh so remote states are updated."""
            await bridge.sensor_manager.coordinator.async_refresh()
            _LOGGER.debug("Update requested at %s", now)

        remote_sc = max(
            DEFAULT_SCAN_INTERVAL, config.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
        )
        if remote_sc < bridge.sensor_manager.coordinator.update_interval:
            # Add listener to update remotes at high rate
            # TODO change sm.coordinator.update_interval instead.
            #  It can be done right here, but any bridge.reset event
            #  would re-write it, so we maintain our own scheduler meanwhile
            async_track_time_interval(
                hass, _update_remotes, remote_sc,
            )
    return True
