from tkinter import *

from matplotlib.widgets import TextBox
import tools

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.master.geometry("1000x1000")
        # self.master.resizable(False, False)

    def count_it(self):
        text = self.text_box.get("1.0", "end").replace("\n", "")
        self.word_count['text'] = tools.count_the_number_of_words(text)
        self.curilic_symbols_count['text'] = tools.count_the_number_of_curilic_characters(text)
        self.symbols_count['text'] = tools.count_the_number_of_symbols(text)
        self.latin_symbols_count['text'] = tools.count_the_number_of_latin_characters(text)
        self.symbols_without_spaces_count['text'] = tools.count_the_number_of_symbols_without_spaces(text)
        self.digits_count['text'] = tools.count_the_number_of_digits(text)
        self.spaces_count['text'] = tools.count_the_number_of_spaces(text)
        self.other_symbols_count['text'] = tools.count_the_number_of_special_symbols(text)
    
    def create_widgets(self):
        title_label = Label(text="Подсчет количества символов и слов", font=("Arial", 20))
        title_label.pack()
        self.create_textbox()

        count_btn = Button(text="Посчитать", font=("Arial", 20), bg="#1E90FF", command=self.count_it)
        count_btn.pack(fill=X, padx=80)
        self.create_result_labels()

    def create_textbox(self):
        self.text_frame = Frame(self.master)
        self.text_frame.pack()

        self.text_box = Text(self.text_frame, wrap='word', font=("Ubuntu Mono", 15))
        self.text_box.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=40)

        self.scroll = Scrollbar(self.text_frame)
        self.scroll.pack(side=RIGHT, fill=BOTH)
        self.text_box.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text_box.yview) # благодаря этому можно мышкой нажать на скролл и опустить его

    def create_result_labels(self):
        result_frame = Frame(self.master)
        result_frame.pack()

        self.word = Label(result_frame, text='Всего слов', font=("Ubuntu Mono", 14)).grid(row=0, column=0)
        self.word_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.word_count.grid(row=0, column=1, padx=100)

        self.curilic_symbols = Label(result_frame, text='Всего кириллических символов', font=("Ubuntu Mono", 14)).grid(row=0, column=2)
        self.curilic_symbols_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.curilic_symbols_count.grid(row=0, column=3, padx=100)

        self.symbols = Label(result_frame, text='Всего символов', font=("Ubuntu Mono", 14)).grid(row=1, column=0)
        self.symbols_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.symbols_count.grid(row=1, column=1, padx=100)

        self.latin_symbols = Label(result_frame, text='Всего латинских символов', font=("Ubuntu Mono", 14)).grid(row=1, column=2)
        self.latin_symbols_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.latin_symbols_count.grid(row=1, column=3, padx=100)

        self.symbols_without_spaces = Label(result_frame, text='Всего символов без пробелов', font=("Ubuntu Mono", 14)).grid(row=2, column=0)
        self.symbols_without_spaces_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.symbols_without_spaces_count.grid(row=2, column=1, padx=100)

        self.digits = Label(result_frame, text='Всего цифр', font=("Ubuntu Mono", 14)).grid(row=2, column=2)
        self.digits_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.digits_count.grid(row=2, column=3, padx=100)

        self.spaces = Label(result_frame, text='Пробелов', font=("Ubuntu Mono", 14)).grid(row=3, column=0)
        self.spaces_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.spaces_count.grid(row=3, column=1, padx=100)

        self.other_symbols = Label(result_frame, text='Остальных символов', font=("Ubuntu Mono", 14)).grid(row=3, column=2)
        self.other_symbols_count = Label(result_frame, text='0',  font=("Ubuntu Mono", 20))
        self.other_symbols_count.grid(row=3, column=3, padx=100)

if __name__ == "__main__":
    tk = Tk()
    app = Application(tk)
    app.mainloop()