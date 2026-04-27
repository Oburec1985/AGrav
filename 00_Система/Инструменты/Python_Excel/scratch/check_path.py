import os
import ctypes

def get_short_path_name(long_name):
    output_buf_size = 0
    while True:
        output_buf = ctypes.create_unicode_buffer(output_buf_size)
        needed = ctypes.windll.kernel32.GetShortPathNameW(long_name, output_buf, output_buf_size)
        if output_buf_size >= needed:
            return output_buf.value
        output_buf_size = needed

path = os.path.dirname(os.path.abspath(__file__))
print(f"Long path: {path}")
try:
    short_path = get_short_path_name(path)
    print(f"Short path: {short_path}")
except Exception as e:
    print(f"Error getting short path: {e}")
