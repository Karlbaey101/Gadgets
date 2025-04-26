# -*- coding: utf-8 -*-

__author__ = 'Karlbaey'

import tkinter as tk
from tkinter import messagebox
import json
import random

class LotteryApp:
    def __init__(self, master):
        self.master = master
        master.title("Lottery v1")
        master.geometry("450x350")
        
        # Initialize variables
        self.is_running = False
        self.update_interval = 33  # 33ms ≈ 30 times/sec
        self.current_animation = None

        # Load list from index.json
        try:
            with open("index.json", "r", encoding="utf-8") as f:
                self.members = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "index.json does not exist")
            self.members = []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "index.json is not formatted correctly")
            self.members = []

        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        self.title_label = tk.Label(
            self.master,
            text="Lottery Gadget",
            font=("", 24, "bold"),
            fg="#2c3e50"
        )
        self.title_label.pack(pady=10)

        # Result frame
        self.result_frame = tk.Frame(
            self.master,
            bg="#ecf0f1",
            padx=20,
            pady=30
        )
        self.result_frame.pack(pady=20)
        
        self.result_label = tk.Label(
            self.result_frame,
            text="Everything is ready",
            font=("", 20, "bold"),
            bg="#ecf0f1",
            fg="#e74c3c",
            width=28
        )
        self.result_label.pack()

        # Button frame
        self.btn_frame = tk.Frame(self.master)
        self.btn_frame.pack(pady=15)

        # Start button
        self.start_btn = tk.Button(
            self.btn_frame,
            text="Start",
            command=self.start_drawing,
            font=("", 12),
            bg="#27ae60",
            fg="white",
            width=10
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)

        # Stop button
        self.stop_btn = tk.Button(
            self.btn_frame,
            text="Stop",
            command=self.stop_drawing,
            font=("", 12),
            bg="#e74c3c",
            fg="white",
            state=tk.DISABLED,
            width=10
        )
        self.stop_btn.pack(side=tk.LEFT, padx=10)

        # Status bar
        self.status_bar = tk.Label(
            self.master,
            text=f"The number of people on list: {len(self.members)}",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_drawing(self):
        if not self.members:
            messagebox.showwarning("Warning", "The list is empty. Please check the index.json")
            return
            
        self.is_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.result_label.config(fg="#e74c3c")
        self.update_result()

    def stop_drawing(self):
        self.is_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.show_final_result()

    def update_result(self):
        if self.is_running:
            # Randomly select and update the display
            selected = random.choice(self.members)
            self.result_label.config(text=selected)
            # Set the next update
            self.current_animation = self.master.after(
                self.update_interval, 
                self.update_result
            )

    def show_final_result(self):
        # Cancel a timer that may exist
        if self.current_animation:
            self.master.after_cancel(self.current_animation)
        
        # Final selection effect
        selected = random.choice(self.members)
        self.result_label.config(text=selected, fg="#2ecc71")
        
        # Add a flickering animation
        for i in range(3):
            self.master.after(100*i, 
                lambda: self.result_label.config(
                    fg="#2ecc71" if i%2==0 else "#e74c3c"
                )
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()