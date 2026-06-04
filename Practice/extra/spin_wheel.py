import tkinter as tk
import random
import math

# Window setup
root = tk.Tk()
root.title("Spin the Wheel")
root.geometry("700x700")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack(pady=20)

# Wheel options (9 sections)
options = [
    "Winner",
    "Try Again",
    "Better Luck Next Time",
    "Winner",
    "Try Again",
    "Better Luck Next Time",
    "Winner",
    "Try Again",
    "Better Luck Next Time"
]

colors = [
    "red", "blue", "green",
    "orange", "purple", "cyan",
    "yellow", "pink", "lightgreen"
]

center_x = 300
center_y = 300
radius = 250
current_angle = 0

# Draw pointer
canvas.create_polygon(
    290, 20,
    310, 20,
    300, 60,
    fill="black"
)

result_label = tk.Label(root, text="", font=("Arial", 18, "bold"))
result_label.pack()


def draw_wheel(start_angle):
    canvas.delete("wheel")

    angle_per_section = 360 / len(options)

    for i in range(len(options)):
        start = start_angle + (i * angle_per_section)
        end = angle_per_section

        # Draw section
        canvas.create_arc(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            start=start,
            extent=end,
            fill=colors[i],
            tags="wheel"
        )

        # Text positioning
        text_angle = math.radians(start + angle_per_section / 2)

        text_x = center_x + (radius * 0.6) * math.cos(text_angle)
        text_y = center_y - (radius * 0.6) * math.sin(text_angle)

        canvas.create_text(
            text_x,
            text_y,
            text=options[i],
            font=("Arial", 10, "bold"),
            angle=-(start + angle_per_section / 2),
            tags="wheel"
        )


def spin():
    global current_angle

    spin_angle = random.randint(720, 1440)
    final_angle = current_angle + spin_angle

    for angle in range(current_angle, final_angle, 10):
        draw_wheel(angle)
        root.update()

    current_angle = final_angle % 360

    # Determine winning section
    angle_per_section = 360 / len(options)

    pointer_angle = (360 - current_angle + 90) % 360
    index = int(pointer_angle // angle_per_section)

    result = options[index]

    result_label.config(text=f"Result: {result}")


# Initial wheel
draw_wheel(current_angle)

# Spin button
spin_button = tk.Button(
    root,
    text="SPIN",
    font=("Arial", 16, "bold"),
    command=spin,
    bg="black",
    fg="white"
)

spin_button.pack(pady=20)

root.mainloop()