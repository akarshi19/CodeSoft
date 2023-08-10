import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Password Generator")
        self.root.configure(bg="#f7f7f7")
        
        self.header_label = tk.Label(root, text="Creative Password Generator", font=("Helvetica", 16, "bold"), bg="#f7f7f7")
        self.header_label.pack(pady=10)

        self.name_label = tk.Label(root, text="Enter Your Name:", font=("Helvetica", 12), bg="#f7f7f7")
        self.name_label.pack()

        self.name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.name_entry.pack()

        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg="#f7f7f7")
        self.length_label.pack()

        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Complexity Level:", font=("Helvetica", 12), bg="#f7f7f7")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("1")

        self.complexity_radio1 = tk.Radiobutton(root, text="Letters (lowercase and uppercase)", variable=self.complexity_var, value="1", font=("Helvetica", 10), bg="#f7f7f7")
        self.complexity_radio2 = tk.Radiobutton(root, text="Letters and Digits", variable=self.complexity_var, value="2", font=("Helvetica", 10), bg="#f7f7f7")
        self.complexity_radio3 = tk.Radiobutton(root, text="Letters, Digits, and Special Characters", variable=self.complexity_var, value="3", font=("Helvetica", 10), bg="#f7f7f7")
        
        self.complexity_radio1.pack()
        self.complexity_radio2.pack()
        self.complexity_radio3.pack()

        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), command=self.generate_password, bg="#ffc107", fg="#fff")
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f7f7f7")
        self.password_label.pack()

    def generate_password(self):
        name = self.name_entry.get()
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        characters = ""
        if complexity == "1":
            characters = string.ascii_letters
        elif complexity == "2":
            characters = string.ascii_letters + string.digits
        elif complexity == "3":
            characters = string.ascii_letters + string.digits + string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Hello {name}! Your Creative Password is: {password}", fg="#007bff")
        else:
            self.password_label.config(text="Invalid complexity choice", fg="#dc3545")

def main():
    root = tk.Tk()
    h,w=root.winfo_screenheight(),root.winfo_screenwidth()
    root.geometry('%dx%d+0+0'%(w,h))
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
