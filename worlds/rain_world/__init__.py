import settings
import typing
from .Options import rainworld_options  # the options we defined earlier
from .Items import rainworld_items  # data used below to add items to the World
from .Locations import rainworld_locations  # same as above
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

from Items import RainWorldItem


class RainWorldLocation(Location):  # or from Locations import RainWorldLocation
    game = "Rain World"  # name of the game/world this location is in


class RainWorldSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""


class RainWorldWorld(World):
    """Insert description of the world/game here."""
    game = "Rain World"  # name of the game/world
    option_definitions = rainworld_options  # options the player can set
    settings: typing.ClassVar[RainWorldSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # Instead of dynamic numbering, IDs could be part of data.

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(rainworld_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(rainworld_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "Perks": {"Neuron glow", "High Agility"},
    }