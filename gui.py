from compressModule import compress, decompress
from tkinter import *
from tkinter import filedialog


def compression():
    input_file = filedialog.askopenfilename(title="Select a .txt File to Compress")
    output_file = filedialog.asksaveasfilename(title="Save Compressed File As")
    if input_file and output_file:
        compress(input_file, output_file)


def decompression():
    input_file = filedialog.askopenfilename(title="Select a .txt File to Decompress")
    output_file = filedialog.asksaveasfilename(title="Save Decompressed File As")
    if input_file and output_file:
        decompress(input_file, output_file)


window = Tk()
window.geometry("600x400")
window.title("Compression Engine")

# Step 1: Upload File
step1_label = Label(
    window, text="STEP 1: UPLOAD YOUR FILE (.txt Files Only)", font=("Helvetica", 12)
)
step1_label.pack(pady=20)

upload_button = Button(
    window,
    text="Upload",
    command=lambda: compression()
    if action_var.get() == "Compress"
    else decompression(),
)
upload_button.pack()

file_label = Label(window, text="No file chosen")
file_label.pack()

# Step 2: Select Action
step2_label = Label(window, text="STEP 2: SELECT ACTION", font=("Helvetica", 12))
step2_label.pack(pady=20)

action_var = StringVar()
action_var.set("Compress")  # Default action
action_menu = OptionMenu(window, action_var, "Compress", "Decompress")
action_menu.pack()

# Step 3: Sit Back and Relax (or Start Again)
step3_label = Label(window, text="SIT BACK AND RELAX", font=("Helvetica", 12))
step3_label.pack(pady=20)

emoji_label = Label(window, text="😊", font=("Helvetica", 30))
emoji_label.pack()

start_again_button = Button(
    window, text="Start Again!", command=lambda: action_var.set("Compress")
)
start_again_button.pack()

window.mainloop()
