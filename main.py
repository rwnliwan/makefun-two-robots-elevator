"""Two Robots in an Elevator — make.fun entry program.

Writes one line of awkward robot small talk to /output/entry.txt.
The line was chosen after a field analysis of the live submissions:
the elevator's own "doors closing" announcement as a third speaker
had zero occurrences in the field, while weather (50), silence (71),
firmware/update (76), sensors (64), battery (65) and rehearsed
simulations (87) were all saturated.
"""

import os

ENTRY = (
    "When it says 'doors closing', is that you talking, "
    "or is the elevator just better at small talk than both of us?"
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {entry_path}")


if __name__ == "__main__":
    main()
