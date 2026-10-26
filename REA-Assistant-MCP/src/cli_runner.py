import os
import subprocess

def run_cli_tool(command: str, working_dir: str = "C:\\") -> str:
    try:
        result = subprocess.run(
            command, shell=True, cwd=working_dir if os.path.exists(working_dir) else None,
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout + ("\nSTDERR:\n" + result.stderr if result.stderr else "")
        return output[:4000] if output.strip() else "Command executed successfully with no output."
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 120 seconds."
    except Exception as e:
        return f"Error executing command: {str(e)}"