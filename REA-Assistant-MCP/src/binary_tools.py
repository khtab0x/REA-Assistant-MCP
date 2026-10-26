import os
import re
import hashlib

def analyze_file_basic(file_path: str) -> str:
    if not os.path.exists(file_path): return f"Error: File not found at {file_path}"
    try:
        size = os.path.getsize(file_path)
        with open(file_path, "rb") as f:
            header = f.read(64)
            f.seek(0)
            sha256 = hashlib.sha256(f.read()).hexdigest()
        magic_hex = header[:16].hex(" ")
        is_pe = header.startswith(b"MZ")
        is_elf = header.startswith(b"\x7fELF")
        file_type = "Windows PE (EXE/DLL)" if is_pe else ("Linux ELF" if is_elf else "Unknown/Raw Binary")
        return f"File: {file_path}\nType: {file_type}\nSize: {size} bytes\nSHA256: {sha256}\nHeader (first 16 bytes): {magic_hex}"
    except Exception as e:
        return f"Error analyzing file: {str(e)}"

def extract_binary_strings(file_path: str, min_length: int = 5, max_results: int = 100) -> str:
    if not os.path.exists(file_path): return f"Error: File not found at {file_path}"
    try:
        with open(file_path, "rb") as f: data = f.read()
        pattern = rb"[\x20-\x7E]{" + str(min_length).encode() + rb",}"
        matches = [m.decode("ascii", errors="ignore") for m in re.findall(pattern, data)]
        sample = matches[:max_results]
        return f"Found {len(matches)} strings (showing first {len(sample)}):\n" + "\n".join(sample)
    except Exception as e:
        return f"Error extracting strings: {str(e)}"

def read_hex_chunk(file_path: str, offset: int = 0, length: int = 256) -> str:
    if not os.path.exists(file_path): return f"Error: File not found at {file_path}"
    try:
        length = min(length, 1024)
        with open(file_path, "rb") as f:
            f.seek(offset)
            chunk = f.read(length)
        lines = []
        for i in range(0, len(chunk), 16):
            sub = chunk[i:i+16]
            hex_part = " ".join(f"{b:02X}" for b in sub)
            ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in sub)
            lines.append(f"{offset + i:08X}  {hex_part:<48}  |{ascii_part}|")
        return "\n".join(lines) if lines else "End of file reached."
    except Exception as e:
        return f"Error reading hex: {str(e)}"