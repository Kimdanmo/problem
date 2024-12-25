import tkinter as tk
import pygame

# 정답 데이터
answers = [
    "12250000",
    "11110",
    "난쟁이"
]

class EscapeRoomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("방탈출 게임")
        self.current_question = 0
        self.create_widgets()

        pygame.mixer.init()
        self.correct_sound = pygame.mixer.Sound("성공.wav")
        self.wrong_sound = pygame.mixer.Sound("실패.wav") 

    def create_widgets(self):
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True, fill='both')

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 14), wraplength=450, justify="left")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.frame, text="완료", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        # 세 번째 문제 힌트 라벨 (초기에는 숨김)
        self.hint_label = tk.Label(self.master, text="정답은 난쟁이", fg="red", font=("Arial", 10))
        self.hint_label.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # 창의 오른쪽 상단 모서리에 위치

        self.show_question()

    def show_question(self):
        if self.current_question == 0:
            self.question_label.config(text="첫번째 문제\n지금까지 산타가 죽인 난쟁이의 수는?")
            self.answer_entry.delete(0, tk.END)
            self.hint_label.place_forget()
        elif self.current_question == 1:
            self.correct_sound.play()
            self.question_label.config(text="두번째 문제\n12와 25의 곱을 10으로 나눈 값을 이진수로 구하시오")
            self.answer_entry.delete(0, tk.END)
            self.hint_label.place_forget()
        elif self.current_question == 2:
            self.correct_sound.play()
            self.question_label.config(text="세번째 문제\n만 6세부터 12세 이하의 어린이가 일정 수치 이상 울었을 때 산타에게 들키면 어떻게 될까요?")
            self.answer_entry.delete(0, tk.END)
            self.hint_label.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # 힌트 표시
        else:
            # 모든 문제를 맞춘 경우
            self.correct_sound.play()
            self.display_message("문제 맞추기 성공", success=True)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = answers[self.current_question]

        if user_answer == correct_answer:
            self.current_question += 1
            if self.current_question < len(answers):
                self.show_question()
            else:
                self.correct_sound.play()
                self.display_message("문제 맞추기 성공", success=True)
        else:
            self.wrong_sound.play()
            self.display_message("탈출에 실패하였습니다", success=False)

    def display_message(self, message, success=True):
        # 기존 위젯 숨기기
        self.frame.pack_forget()
        self.hint_label.place_forget()

        # 메시지 표시
        msg_color = "green" if success else "red"
        self.message_label = tk.Label(self.master, text=message, font=("Arial", 24), fg=msg_color)
        self.message_label.pack(expand=True)

    def reset_game(self):
        # 게임을 초기 상태로 리셋 (필요 시 구현)
        pass

def main():
    root = tk.Tk()
    root.geometry("500x300")  # 창 크기 설정
    app = EscapeRoomApp(root)
    root.mainloop()

if __name__ == "__main__":
        main()
