import tkinter as tk
from tkinter import ttk, messagebox
import gui
from alg import nearest_neighbor, annealing, ant_alg

def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"): root.destroy()

root = tk.Tk()
root.geometry("1000x500")
root.protocol("WM_DELETE_WINDOW", on_closing)

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
notebook.add(tab1, text='Метод ближайшего соседа')
notebook.add(tab2, text='Имитация отжига')
notebook.add(tab3, text='Муравьиный алгоритм')

neighbor_window = gui.myWindow(tab1,'#cad7e8')
neighbor_table = gui.myTable(neighbor_window.middle_left_frame,['Вершина 1', 'Вершина 2', 'Вес'])
neighbor_result = gui.myResult(neighbor_window.bottom_left_frame)
neighbor_canvas = gui.canvas(neighbor_window.top_right_frame,neighbor_table,neighbor_result)
neighbor_startButton = gui.Button(neighbor_window.top_left_frame,'Начать алгоритм', nearest_neighbor.nearest_neighbor, neighbor_canvas)
neighbor_clearButton = gui.Button(neighbor_window.top_left_frame,'Стереть данные',neighbor_canvas.clear_canvas,True)

annealing_window = gui.myWindow(tab2,'#d7e8d5')
annealing_table = gui.myTable(annealing_window.middle_left_frame,['Вершина 1', 'Вершина 2', 'Вес'])
annealing_result = gui.myResult(annealing_window.bottom_left_frame)
annealing_canvas = gui.canvas(annealing_window.top_right_frame,annealing_table,annealing_result)
annealing_stemp = gui.labeledSpinbox(annealing_window.top_left_frame,"Начальная температура",10,1000,1000,10)
annealing_fTemp = gui.labeledSpinbox(annealing_window.top_left_frame,"Конечная температура",0,1000,1e-8,1)
annealing_coolVal = gui.labeledSpinbox(annealing_window.top_left_frame,"Коэффициент охлаждения",0,1,0.003,0.001)
annealing_startButton = gui.Button(annealing_window.top_left_frame,'Начать алгоритм',annealing.solve_tsp_with_simulated_annealing,[annealing_canvas,annealing_stemp,annealing_fTemp,annealing_coolVal])
annealing_clearButton = gui.Button(annealing_window.top_left_frame,'Стереть данные',annealing_canvas.clear_canvas,True)

ant_window = gui.myWindow(tab3,'#e8caca')
ant_table = gui.myTable(ant_window.middle_left_frame,['Вершина 1', 'Вершина 2', 'Вес'])
ant_result = gui.myResult(ant_window.bottom_left_frame)
ant_canvas = gui.canvas(ant_window.top_right_frame,ant_table,ant_result)
ant_value = gui.labeledSpinbox(ant_window.top_left_frame,'Количество муравьев',1,1000,10,5)
ant_iter = gui.labeledSpinbox(ant_window.top_left_frame,'Количество поколений',1,1000,45,5)
ant_alpha = gui.labeledSpinbox(ant_window.top_left_frame,'Альфа значение',1,10,1,1)
ant_beta = gui.labeledSpinbox(ant_window.top_left_frame,'Бета значение',1,10,5,1)
ant_decay = gui.labeledSpinbox(ant_window.top_left_frame,'Скорость распада феромона',0,10,0.1,0.1)
ant_pherconst = gui.labeledSpinbox(ant_window.top_left_frame,'Мощность феромона',0,10,2,1)
ant_startButton = gui.Button(ant_window.top_left_frame,'Начать алгоритм',ant_alg.ant_alg,[ant_canvas,ant_value,ant_iter,ant_decay,ant_alpha,ant_beta,ant_pherconst])
ant_clearButton = gui.Button(ant_window.top_left_frame,'Стереть данные',ant_canvas.clear_canvas,True)

root.mainloop()