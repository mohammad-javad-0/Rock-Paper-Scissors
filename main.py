from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QTextBrowser, QMessageBox
from PyQt6.QtGui import QFont, QIcon, QCursor
from PyQt6.QtCore import Qt, QSize
from random import choice
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 700)
        self.setWindowTitle("Rock-Paper-scissors")
        self.setWindowIcon(QIcon("image/icon_title.png"))
        self.setStyleSheet("background-color:#FFAE00;color:black")

        # create label heading
        lbl_heading = QLabel("Rock Paper Scissors", self)
        lbl_heading.setFont(QFont("arial", 20))
        lbl_heading.setFixedSize(700, 50)
        lbl_heading.setIndent(225)
        lbl_heading.setStyleSheet("background-color:#fff;color:#7E1D1D")
        lbl_heading.move(0, 20)

        # create label and combobox of game round
        lbl_game_round = QLabel("Game round:", self)
        lbl_game_round.setFont(QFont("arial", 15))
        lbl_game_round.move(50, 100)

        self.combo_game_round = QComboBox(self)
        self.combo_game_round.addItems(["3", "5", "10"])
        self.combo_game_round.setFont(QFont("arial", 15))
        self.combo_game_round.setFixedSize(120, 20)
        self.combo_game_round.setStyleSheet("background-color:#fff")
        self.combo_game_round.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combo_game_round.move(180, 100)

        # create start button and history button
        self.btn_start = QPushButton("START", self)
        self.btn_start.setFont(QFont("arial", 15))
        self.btn_start.setFixedSize(130, 40)
        self.btn_start.setStyleSheet("background-color:#FF0000")
        self.btn_start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_start.move(350, 90)
        self.btn_start.clicked.connect(self.start)

        self.btn_history = QPushButton("HISTORY", self)
        self.btn_history.setFont(QFont("arial", 15))
        self.btn_history.setFixedSize(130, 40)
        self.btn_history.setStyleSheet("background-color:#0078FF")
        self.btn_history.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_history.move(500, 90)
        self.btn_history.clicked.connect(self.show_history)

        # create scoreboard
        user_scoreboard = QLabel("Your score", alignment=Qt.AlignmentFlag.AlignCenter, parent=self)
        user_scoreboard.setFont(QFont("arial", 20))
        user_scoreboard.setFixedSize(180, 30)
        user_scoreboard.setStyleSheet("background-color:#fff;border: 2px solid black")
        user_scoreboard.move(100, 180)

        self.user_score = QLabel("0", self)
        self.user_score.setFont(QFont("arial", 17))
        self.user_score.setStyleSheet("background-color:#fff;border: 2px solid black")
        self.user_score.move(280, 180)

        AI_scoreboard = QLabel("AI score", alignment=Qt.AlignmentFlag.AlignCenter, parent=self)
        AI_scoreboard.setFont(QFont("arial", 20))
        AI_scoreboard.setFixedSize(180, 30)
        AI_scoreboard.setStyleSheet("background-color:#fff;border: 2px solid black")
        AI_scoreboard.move(390, 180)

        self.AI_score = QLabel("0", self)
        self.AI_score.setFont(QFont("arial", 17))
        self.AI_score.setStyleSheet("background-color:#fff;border: 2px solid black")
        self.AI_score.move(570, 180)

        # create Playground
        self.Playground = QTextBrowser(self)
        self.Playground.setText(f"\n\n\t{'- '*10}".expandtabs(20) * 3)
        self.Playground.setFont(QFont("arial", 20))
        self.Playground.setFixedSize(500, 300)
        self.Playground.setStyleSheet("background-color:#fff;border: 3px solid black")
        self.Playground.move(100, 230)

        # create game buttons
        self.btn_rock = QPushButton(self)
        self.btn_rock.setFixedSize(100, 100)
        self.btn_rock.setDisabled(True)
        self.btn_rock.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_rock.setIcon(QIcon("image/rock.png"))
        self.btn_rock.setStyleSheet("border: 0px")
        self.btn_rock.setIconSize(QSize(100, 100))
        self.btn_rock.move(100, 570)
        self.btn_rock.clicked.connect(lambda: self.play_game("rock"))

        self.btn_paper = QPushButton(self)
        self.btn_paper.setDisabled(True)
        self.btn_paper.setFixedSize(100, 100)
        self.btn_paper.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_paper.setIcon(QIcon("image/paper.png"))
        self.btn_paper.setStyleSheet("border: 0px")
        self.btn_paper.setIconSize(QSize(100, 100))
        self.btn_paper.move(300, 570)
        self.btn_paper.clicked.connect(lambda: self.play_game("paper"))

        self.btn_scissors = QPushButton(self)
        self.btn_scissors.setDisabled(True)
        self.btn_scissors.setFixedSize(100, 100)
        self.btn_scissors.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_scissors.setIcon(QIcon("image/scissors.png"))
        self.btn_scissors.setStyleSheet("border: 0px")
        self.btn_scissors.setIconSize(QSize(100, 100))
        self.btn_scissors.move(500, 570)
        self.btn_scissors.clicked.connect(lambda: self.play_game("scissors"))


    def reset_game(self):
        self.user_score.setText("0")
        self.AI_score.setText("0")
        self.Playground.setText(f"\n\n\t{'- '*10}".expandtabs(20) * 3)
        self.state_buttons(False)


    def show_result_message(self, message):
        message_box = QMessageBox(parent=self, text=message)
        message_box.setWindowTitle("Game Result")
        message_box.setStyleSheet("background-color:white")
        message_box.show()
        if message_box.exec() == QMessageBox.StandardButton.Ok:
            self.reset_game()


    def game_result(self):
        user_score = int(self.user_score.text())
        AI_score = int(self.AI_score.text())
        if user_score > AI_score:
            result = "You Won"
        elif AI_score > user_score:
            result = "AI won"
        else:
            result = "Equal"
        
        message = f"your score : {user_score}  AI score : {AI_score}\n\t{result}"
        self.show_result_message(message)
        self.writ_history(message)


    def play_game(self, user_choice):
        AI_choice = choice(["rock", "paper", "scissors"])

        if AI_choice == user_choice:
            pass
        elif (
        (AI_choice == "rock" and user_choice == "paper")
        or (AI_choice == "paper" and user_choice == "scissors")
        or (AI_choice == "scissors" and user_choice == "rock")):
            self.user_score.setNum(int(self.user_score.text()) + 1)
        else:
            self.AI_score.setNum(int(self.AI_score.text()) + 1)
        
        message = f"\t----- Round {self.game_round} -----\n\n\
            \tYour choice: {user_choice}\n\n{'- ' * 28}\n\n\tAI choice: {AI_choice}".expandtabs(17)
        self.Playground.setText(message)
        
        if self.game_round == int(self.combo_game_round.currentText()):
            return self.game_result()
        self.game_round += 1


    def state_buttons(self, bool):
        """bool (bool): if True, the buttons activated if False, the buttons deactivated"""

        self.btn_start.setDisabled(bool)
        self.btn_history.setDisabled(bool)
        self.combo_game_round.setDisabled(bool)
        self.btn_rock.setEnabled(bool)
        self.btn_paper.setEnabled(bool)
        self.btn_scissors.setEnabled(bool)


    def start(self):
        self.game_round = 1
        self.state_buttons(True)
        text = "The game begins\n\n\tPlease select a button".center(75).expandtabs(15)
        self.Playground.setText(text)
        

    def writ_history(self, text):
        with open("history.txt", "a") as writer:
            writer.write(text + "\n" + "- " * 25 + "\n")


    def show_history(self):
        with open("history.txt", "r") as reader:
            text = reader.read()
            self.Playground.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    root = Window()
    root.show()

    sys.exit(app.exec())