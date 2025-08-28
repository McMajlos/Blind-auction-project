# Blind Auction Project

This is a simple command-line Python project simulating a blind auction. Participants enter their names and bids, and the program determines the highest bidder at the end. The auction continues until no more participants wish to bid.

## How It Works
- Each participant enters their name and bid amount.
- The program asks if there are more bidders; if so, the screen is cleared and the next participant can enter their bid.
- Once all bids are collected, the program announces the winner with the highest bid.

## Usage
Run the script using Python:

```pwsh
python main.py
```

Follow the prompts to enter names and bids. The winner will be displayed at the end.

## Requirements
- Python 3.x
- Works on Windows, macOS, and Linux (uses `os.system` to clear the screen)

## License
This project is for educational purposes.
