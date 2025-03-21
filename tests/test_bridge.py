from enum import Enum

from bridge import ToolsBridge


class Units(str, Enum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"


@ToolsBridge.register()
def get_weather_a(location: str, units: Units) -> float:
    """Retrieves current weather for the given location.

    Args:
        location: City and country e.g. Silicon Valley, United States.
        units: Units the temperature will be returned in.

    Returns:
        foobar
    """
    pass


@ToolsBridge.register(description="Retrieves current weather for the given location.")
def get_weather_b(location: str, units: Units) -> float:
    """
    Parameters
    ----------
    location :
        City and country e.g. Silicon Valley, United States.
    units :
        Units the temperature will be returned in.

    Returns
    -------
        foobar
    """


@ToolsBridge.register(
    description="Retrieves current weather for the given location.",
    param_descriptions={
        "location": "City and country e.g. Silicon Valley, United States.",
        "units": "Units the temperature will be returned in.",
    },
)
def get_weather_c(location: str, units: Units) -> float:
    pass


def test_register_and_get():
    for t in ToolsBridge.get_tools():
        assert (
            t["function"]["description"]
            == "Retrieves current weather for the given location."
        )
        assert "location" in t["function"]["parameters"]["required"]
        assert "units" in t["function"]["parameters"]["required"]

    a = ToolsBridge.get_tool("get_weather_a")
    assert (
        a["function"]["parameters"]["properties"]["location"]["description"]
        == "City and country e.g. Silicon Valley, United States."
    )

    b = ToolsBridge.get_tool("get_weather_b")
    assert (
        b["function"]["parameters"]["properties"]["units"]["description"]
        == "Units the temperature will be returned in."
    )

    c = ToolsBridge.get_tool("get_weather_c")
    assert "celsius" in c["function"]["parameters"]["properties"]["units"]["enum"]
    assert "fahrenheit" in c["function"]["parameters"]["properties"]["units"]["enum"]
