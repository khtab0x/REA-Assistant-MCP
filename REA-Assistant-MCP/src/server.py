from mcp.server.fastmcp import FastMCP
from .binary_tools import analyze_file_basic, extract_binary_strings, read_hex_chunk
from .cli_runner import run_cli_tool

mcp = FastMCP("RE_Assistant")

mcp.tool()(analyze_file_basic)
mcp.tool()(extract_binary_strings)
mcp.tool()(read_hex_chunk)
mcp.tool()(run_cli_tool)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()