import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(): #Open files for editing
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file(): #Save AS the file.
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Word Lite")

window.columnconfigure(1, weight=1, minsize=800)
window.rowconfigure(0, weight=1, minsize=800)

txt_edit = tk.Text(window)
frm_button = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_button, text="Open", command=open_file)
btn_save = tk.Button(frm_button, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky=tk.EW, padx=5)

frm_button.grid(row=0, column=0, sticky=tk.NS)
txt_edit.grid(row=0, column=1, sticky=tk.NSEW)

window.mainloop()