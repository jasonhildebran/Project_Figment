import time
import sys

# Simulation of the robot logic
def wake_up_sequence():
    print(f"[{time.strftime('%H:%M:%S')}] SYSTEM: Figment Core Active.")
    print(f"[{time.strftime('%H:%M:%S')}] CHECK: Python Version {sys.version.split()[0]} OK.")
    
    parts = ["Neck Pan", "Neck Tilt", "Jaw", "Left Eye", "Right Eye"]
    
    print("\n--- BEGINNING MOTOR SELF-TEST (MOCK) ---")
    for part in parts:
        print(f" -> Pinging {part} servo... ", end="")
        time.sleep(0.3) # Simulate hardware latency
        print("ONLINE.")
    
    print("\n--- SENSORY CHECK ---")
    print(" -> Camera... DETECTED (Virtual)")
    print(" -> Microphone... DETECTED (Virtual)")
    
    print("\nSYSTEM READY. Waiting for OpenAI API Key...")

if __name__ == "__main__":
    wake_up_sequence()