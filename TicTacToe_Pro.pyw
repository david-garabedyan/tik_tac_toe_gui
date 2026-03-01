import customtkinter as ctk
from tkinter import messagebox

class TicTacToe(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tic-Tac-Toe Pro")
        self.geometry("400x500")
        self.resizable(False, False)
        
        # Настройка на темата
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.game_active = True

        self.setup_ui()

    def setup_ui(self):
        # Заглавие
        self.label = ctk.CTkLabel(self, text="На ход е: X", font=("Outfit", 24, "bold"))
        self.label.pack(pady=20)

        # Контейнер за мрежата
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(pady=10, padx=20)

        # Създаване на бутоните
        for i in range(9):
            btn = ctk.CTkButton(
                self.grid_frame, 
                text="", 
                width=100, 
                height=100, 
                font=("Outfit", 40, "bold"),
                fg_color="#2b2b2b",
                hover_color="#3d3d3d",
                corner_radius=15,
                command=lambda i=i: self.make_move(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Бутон за рестарт
        self.reset_button = ctk.CTkButton(
            self, 
            text="Нова игра", 
            font=("Outfit", 16, "bold"),
            command=self.reset_game,
            fg_color="#1f538d",
            hover_color="#14375e"
        )
        self.reset_button.pack(pady=30)

    def make_move(self, index):
        if self.board[index] == "" and self.game_active:
            # Запис на хода
            self.board[index] = self.current_player
            color = "#3a7ebf" if self.current_player == "X" else "#bf3a3a"
            self.buttons[index].configure(text=self.current_player, text_color=color)
            
            # Проверка за победител
            winner_indices = self.check_winner()
            if winner_indices:
                self.end_game(f"Победител е {self.current_player}!", winner_indices)
            elif "" not in self.board:
                self.end_game("Равенство!", [])
            else:
                # Смяна на играча
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.configure(text=f"На ход е: {self.current_player}")

    def check_winner(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # хоризонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикали
            (0, 4, 8), (2, 4, 6)             # диагонали
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return combo
        return None

    def end_game(self, message, winner_indices):
        self.game_active = False
        self.label.configure(text=message, text_color="#2ecc71")
        
        # Маркиране на печелившата линия
        for idx in winner_indices:
            self.buttons[idx].configure(fg_color="#2ecc71", text_color="white")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        self.label.configure(text="На ход е: X", text_color="white")
        for btn in self.buttons:
            btn.configure(text="", fg_color="#2b2b2b")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
