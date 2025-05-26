import tkinter as tk
from random import choice
from gui.reels import Reel

# Symbols for the slot machine
SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "🔔", "7"]

# Default probabilities (percentages, must sum to 100)
DEFAULT_PROBABILITIES = {
    "🍒": 20,
    "🍋": 20,
    "🍊": 20,
    "🍇": 15,
    "🔔": 15,
    "7": 10
}

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Simulator")
        self.root.geometry("400x400")  # Set a fixed window size (adjust as needed)
        self.root.resizable(False, False)  # Make window fixed size
        self.symbol_probabilities = DEFAULT_PROBABILITIES.copy()
        self.score = 0
        
        # Create the reels
        self.reel1 = tk.Label(root, text="🍒", font=("Helvetica", 48))
        self.reel2 = tk.Label(root, text="🍋", font=("Helvetica", 48))
        self.reel3 = tk.Label(root, text="🍊", font=("Helvetica", 48))
        
        # Place the reels in the grid
        self.reel1.grid(row=0, column=0, padx=10, pady=10)
        self.reel2.grid(row=0, column=1, padx=10, pady=10)
        self.reel3.grid(row=0, column=2, padx=10, pady=10)
        
        # Create the spin button
        self.spin_button = tk.Button(root, text="Spin", command=self.spin_reels, font=("Helvetica", 16))
        self.spin_button.grid(row=1, column=0, columnspan=3, pady=20)
        
        # Config button
        self.config_button = tk.Button(root, text="Config", command=self.open_config_panel, font=("Helvetica", 12))
        self.config_button.grid(row=2, column=0, pady=5)
        
        # Create a label for the result
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Score label
        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16))
        self.score_label.grid(row=4, column=0, columnspan=3, pady=10)

    def spin_reels(self):
        # Disable spin button during animation
        self.root.resizable(False, False)  # Prevent resizing while spinning
        self.spin_button.config(state=tk.DISABLED)
        self.result_label.config(text="", fg="red")
        self._spin_animation(0, [], 10)

    def _spin_animation(self, step, symbols, max_steps):
        import random
        # Show random symbols for animation effect
        temp1 = random.choice(SYMBOLS)
        temp2 = random.choice(SYMBOLS)
        temp3 = random.choice(SYMBOLS)
        self.reel1.config(text=temp1)
        self.reel2.config(text=temp2)
        self.reel3.config(text=temp3)
        if step < max_steps:
            self.root.after(80, lambda: self._spin_animation(step+1, symbols, max_steps))
        else:
            # Use the probabilities to select symbols
            reel1_symbol = Reel.weighted_choice(self.symbol_probabilities)
            reel2_symbol = Reel.weighted_choice(self.symbol_probabilities)
            reel3_symbol = Reel.weighted_choice(self.symbol_probabilities)
            self.reel1.config(text=reel1_symbol)
            self.reel2.config(text=reel2_symbol)
            self.reel3.config(text=reel3_symbol)
            if reel1_symbol == reel2_symbol == reel3_symbol:
                self.result_label.config(text="You Win!", fg="green")
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
            else:
                self.result_label.config(text="", fg="red")
            self.spin_button.config(state=tk.NORMAL)
            self.root.resizable(False, False)  # Keep window fixed after spinning

    def open_config_panel(self):     
        config_win = tk.Toplevel(self.root)
        config_win.title("Configure Symbol Probabilities")
        entries = {}
        row = 0
        for symbol in SYMBOLS:
            tk.Label(config_win, text=symbol, font=("Helvetica", 24)).grid(row=row, column=0, padx=10, pady=5)
            var = tk.StringVar(value=str(self.symbol_probabilities[symbol]))
            entry = tk.Entry(config_win, textvariable=var, width=5)
            entry.grid(row=row, column=1, padx=10, pady=5)
            entries[symbol] = var
            row += 1
        def save():
            total = 0
            new_probs = {}
            for symbol in SYMBOLS:
                try:
                    val = int(entries[symbol].get())
                except ValueError:
                    val = 0
                new_probs[symbol] = val
                total += val
            if total != 100:
                tk.messagebox.showerror("Error", "Total probability must be 100%!")
                return
            self.symbol_probabilities = new_probs
            config_win.destroy()
        save_btn = tk.Button(config_win, text="Save", command=save)
        save_btn.grid(row=row, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()