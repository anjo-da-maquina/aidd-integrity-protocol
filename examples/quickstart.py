"""
Quickstart Example for The SHISEI Protocol
Demonstrates integration of algorithmic integrity checking.
"""

from shisei_protocol import ShiseiGuard

def main():
    print("Initializing The SHISEI Protocol Quickstart...")
    
    # Initialize guard with unique project identifier
    guard = ShiseiGuard(project_id="quickstart-demo-01")
    
    # Execute integrity enforcement check
    receipt = guard.enforce_integrity()
    
    print("Audit Receipt Generated Successfully:")
    for key, value in receipt.items():
        print(f"  - {key}: {value}")

if __name__ == "__main__":
    main()
