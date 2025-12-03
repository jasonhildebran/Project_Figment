from vision_system import map_range

def test_map_range():
    # Test cases: (input, expected_output)
    test_cases = [
        (0, 135),    # Leftmost
        (640, 45),   # Rightmost
        (320, 90),   # Center
        (160, 112),  # Quarter left (approx)
        (480, 67)    # Quarter right (approx)
    ]

    print("Testing map_range function...")
    for x, expected in test_cases:
        result = map_range(x, 0, 640, 135, 45)
        print(f"Input: {x}, Expected: {expected}, Got: {result}")
        # Allow for small integer division differences
        assert abs(result - expected) <= 1, f"Failed for {x}: expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_map_range()
