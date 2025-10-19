import random
from fastmcp import FastMCP

mcp=FastMCP(name="demo-mcp",version="1.0.0")

@mcp.tool
def roll_dice(n_sides: int) -> int:
    """Roll a dice with n sides and return the result."""
    return random.randint(1, n_sides)

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    mcp.run()