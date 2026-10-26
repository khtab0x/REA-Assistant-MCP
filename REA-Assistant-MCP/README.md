REA-Assistant MCP Server (Local Reverse Engineering AI)

A powerful, 100% local, and free Model Context Protocol (MCP) server that transforms your local Large Language Models (LLMs) into a fully equipped Reverse Engineering Assistant.

By integrating this server with an AI client like LM Studio, your local model gains the ability to dynamically inspect binaries, extract strings, read hex dumps, and execute command-line reverse engineering tools—all without your sensitive files ever leaving your machine.

Key Features

Binary Analysis (analyze_file_basic): Fetches basic binary information including size, SHA256 hashes, and magic bytes to quickly identify Windows PE or Linux ELF files.

String Extraction (extract_binary_strings): Quickly dumps and filters readable ASCII strings from executables to uncover hidden paths, URLs, or hardcoded credentials.

Hex Inspector (read_hex_chunk): Reads chunks of bytes from binaries at specific offsets, returning cleanly formatted hex dumps directly to the AI's context.

CLI Tool Runner (run_cli_tool): A secure subprocess layer that allows the AI to execute standard reverse engineering CLI commands (e.g., radare2, objdump, or Ghidra headless scripts) and read the output.

Prerequisites

Python 3.10+ installed on your system.

LM Studio (latest version with MCP support).

Clone this repository and install the dependencies:

git clone https://github.com/YOUR_USERNAME/REA-Assistant-MCP.git
cd REA-Assistant-MCP
pip install -r requirements.txt


Step-by-Step GUI Setup (LM Studio)

Connecting the REA-Assistant to LM Studio is incredibly easy using the built-in MCP configuration UI. Follow these visual steps:

Step 1: Open Settings

Open LM Studio and click on the Settings (gear icon) located at the bottom left of the window.

Step 2: Navigate to MCP Integrations

In the left sidebar, scroll down to the Integrations section and click on MCP.

Step 3: Add Custom MCP Server

Scroll down to the "Manual MCP server setup" section and click the + Add custom MCP button.

Step 4: Configure the Server

Fill out the configuration fields exactly as shown below:

Name: REA

Command: python (Ensure Python is in your system PATH, or provide the absolute path to your virtual environment's python.exe)

Arguments:

Add argument 1: -m

Add argument 2: src.server

Working directory: The absolute path to where you downloaded this project (e.g., C:\REA-Assistant-MCP).

Step 5: Verify Connection

Save the settings. Within a few seconds, the status should turn Green and display Connected · 4 tools ready.

You are all set! Open a chat with any local model in LM Studio, and it will now have access to your reverse engineering tools.

Usage Examples

Once connected, simply talk to your local AI. Try giving it prompts like:

"Can you use the analyze_file_basic tool on C:\malware_samples\suspicious.exe?"

"Run the extract_binary_strings tool on that executable and tell me if you see any suspicious IP addresses or web URLs."

"Read a hex chunk at offset 0x1000 from the DLL using read_hex_chunk and analyze the header."

Project Architecture

The project is highly modular to ensure clean code and easy expansion for future reverse engineering tools:

REA-Assistant-MCP/
│
├── src/
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── server.py               # Main entry point; initializes FastMCP and registers tools
│   ├── binary_tools.py         # Core logic for hashing, string extraction, and hex analysis
│   └── cli_runner.py           # Subprocess execution layer for external CLI tools
│
├── .gitignore                  
├── requirements.txt            # Project dependencies (mcp, pydantic)
└── README.md                   


License

This project is licensed under the MIT License.