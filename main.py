import tkinter as tk
import time
import math

def update_clock():
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min
    second = now.tm_sec
    hour_angle = (hour%12 + minute/60) * 30
    minute_angle = minute * 6
    second_angle = second * 6
    hour_x = 150 + 80 * math.sin(math.radians(hour_angle))
    hour_y = 150 - 80 * math.cos(math.radians(hour_angle))
    minute_x = 150 + 100 * math.sin(math.radians(minute_angle))
    minute_y = 150 - 100 * math.cos(math.radians(minute_angle))
    second_x = 150 + 120 * math.sin(math.radians(second_angle))
    second_y = 150 - 120 * math.cos(math.radians(second_angle))
    canvas.coords(hour_hand, 150, 150, hour_x, hour_y)
    canvas.coords(minute_hand, 150, 150, minute_x, minute_y)
    canvas.coords(second_hand, 150, 150, second_x, second_y)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Relógio Analógico")

canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

# Desenha as marcações das horas
for i in range(12):
    hour = i + 1
    angle = i * 30
    x1 = 150 + 100 * math.sin(math.radians(angle))
    y1 = 150 - 100 * math.cos(math.radians(angle))
    x2 = 150 + 120 * math.sin(math.radians(angle))
    y2 = 150 - 120 * math.cos(math.radians(angle))
    canvas.create_line(x1, y1, x2, y2, width=4, fill='black')
    x = 150 + 90 * math.sin(math.radians(angle))
    y = 150 - 90 * math.cos(math.radians(angle))
    canvas.create_text(x, y, text=str(hour), font=('Arial', 12))

# Desenha as marcações dos minutos
for i in range(60):
    angle = i * 6
    x1 = 150 + 110 * math.sin(math.radians(angle))
    y1 = 150 - 110 * math.cos(math.radians(angle))
    x2 = 150 + 120 * math.sin(math.radians(angle))
    y2 = 150 - 120 * math.cos(math.radians(angle))
    canvas.create_line(x1, y1, x2, y2, width=1, fill='gray')

clock_frame = canvas.create_oval(30, 30, 270, 270, width=4, outline='black')
hour_hand = canvas.create_line(150, 150, 150, 70, width=6, fill='black')
minute_hand = canvas.create_line(150, 150, 150, 50, width=4, fill='black')
second_hand = canvas.create_line(150, 150, 150, 40, width=2, fill='red')

update_clock()

root.mainloop()
