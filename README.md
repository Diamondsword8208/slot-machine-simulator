# Slot Machine Simulator

## Overview
The Slot Machine Simulator is a simple graphical user interface (GUI) application that simulates a classic slot machine experience. It features three reels, each displaying one of six symbols: cherry, lemon, orange, plum, bell, and 7. The application allows users to spin the reels and see the results, along with potential payouts based on the symbols displayed.

## Features
- Three spinning reels
- Six unique symbols
- Randomized symbol selection
- Payout calculation based on the results

## Getting Started

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Diamondsword8208/slot-machine-simulator.git
   ```
2. Navigate to the project directory:
   ```
   cd slot-machine-simulator
   ```
3. Install the required dependencies:
   You can use pip to install the necessary packages. It's recommended to create a virtual environment for this project.
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   pip install -r requirements.txt
   ```

### Running the Simulator
To run the slot machine simulator, execute the following command:
```
python src/main.py
```

## File Structure
```
slot-machine-simulator
├── src
│   ├── main.py
│   ├── gui
│   │   ├── __init__.py
│   │   ├── reels.py
│   │   └── symbols.py
│   ├── logic
│   │   ├── __init__.py
│   │   ├── slot_machine.py
│   │   └── payout_calculator.py
│   └── assets
│       └── symbols
│           ├── cherry.txt
│           ├── lemon.txt
│           ├── orange.txt
│           ├── plum.txt
│           ├── bell.txt
│           └── seven.txt
├── requirements.txt
└── README.md
```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.