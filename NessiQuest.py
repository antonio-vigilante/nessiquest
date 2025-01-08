import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class TestGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NessiTest")
        self.questions = []
        self.selected_question_index = None  # Indice della domanda selezionata per la modifica

        # Layout
        self.create_ui()

    def create_ui(self):
        # Titolo del questionario
        self.title_label = tk.Label(self.root, text="Titolo del questionario:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

        # Footer
        self.footer_label = tk.Label(self.root, text="Footer (opzionale):")
        self.footer_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.footer_entry = tk.Entry(self.root, width=50)
        self.footer_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

        # Domanda
        self.question_label = tk.Label(self.root, text="Domanda:")
        self.question_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.question_entry = tk.Entry(self.root, width=50)
        self.question_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

        # Risposte
        self.options_frame = tk.Frame(self.root)
        self.options_frame.grid(row=3, column=0, columnspan=4, pady=10)

        self.add_option_button = tk.Button(self.root, text="Aggiungi opzione", command=self.add_option)
        self.add_option_button.grid(row=4, column=0, padx=5, pady=5)

        self.save_question_button = tk.Button(self.root, text="Salva domanda", command=self.save_question)
        self.save_question_button.grid(row=4, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(self.root, text="Genera HTML", command=self.generate_html)
        self.generate_button.grid(row=4, column=2, padx=5, pady=5)

        # Elenco domande
        self.questions_frame = tk.Frame(self.root, borderwidth=2, relief="sunken")
        self.questions_frame.grid(row=5, column=0, columnspan=4, pady=10, sticky="nsew")

        self.questions_list_label = tk.Label(self.questions_frame, text="Domande salvate:", anchor="w")
        self.questions_list_label.pack(fill="x")

        self.questions_listbox = tk.Listbox(self.questions_frame, height=10, width=80)
        self.questions_listbox.pack(fill="both", expand=True)
        self.questions_listbox.bind("<<ListboxSelect>>", self.load_selected_question)

        self.options = []
        self.add_option()  # Aggiungi una prima opzione iniziale

    def add_option(self):
        option_frame = tk.Frame(self.options_frame)
        option_frame.pack(fill="x", pady=2)

        var = tk.StringVar()
        option_entry = tk.Entry(option_frame, textvariable=var, width=40)
        option_entry.pack(side="left", padx=5)

        correct_var = tk.BooleanVar()
        correct_checkbox = tk.Checkbutton(option_frame, text="Corretta", variable=correct_var)
        correct_checkbox.pack(side="right", padx=5)

        self.options.append((var, correct_var))

    def save_question(self):
        question_text = self.question_entry.get().strip()
        if not question_text:
            messagebox.showerror("Errore", "Inserisci il testo della domanda.")
            return

        options = []
        for var, correct_var in self.options:
            option_text = var.get().strip()
            if option_text:
                options.append({"text": option_text, "correct": correct_var.get()})

        if not options:
            messagebox.showerror("Errore", "Inserisci almeno un'opzione di risposta.")
            return

        if self.selected_question_index is not None:
            # Modifica domanda esistente
            self.questions[self.selected_question_index] = {"question": question_text, "options": options}
            messagebox.showinfo("Successo", "Domanda modificata con successo.")
            self.selected_question_index = None  # Resetta l'indice
        else:
            # Aggiungi nuova domanda
            self.questions.append({"question": question_text, "options": options})
            messagebox.showinfo("Successo", "Domanda salvata con successo.")

        # Aggiorna la lista delle domande
        self.update_questions_listbox()

        # Resetta i campi
        self.reset_fields()

    def reset_fields(self):
        self.question_entry.delete(0, tk.END)
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.options = []
        self.add_option()

    def update_questions_listbox(self):
        self.questions_listbox.delete(0, tk.END)
        for i, q in enumerate(self.questions, 1):
            self.questions_listbox.insert(tk.END, f"{i}. {q['question']}")

    def load_selected_question(self, event):
        try:
            selection = self.questions_listbox.curselection()
            if not selection:
                return
            index = selection[0]
            self.selected_question_index = index

            question = self.questions[index]
            self.question_entry.delete(0, tk.END)
            self.question_entry.insert(0, question["question"])

            for widget in self.options_frame.winfo_children():
                widget.destroy()
            self.options = []

            for option in question["options"]:
                option_frame = tk.Frame(self.options_frame)
                option_frame.pack(fill="x", pady=2)

                var = tk.StringVar(value=option["text"])
                option_entry = tk.Entry(option_frame, textvariable=var, width=40)
                option_entry.pack(side="left", padx=5)

                correct_var = tk.BooleanVar(value=option["correct"])
                correct_checkbox = tk.Checkbutton(option_frame, text="Corretta", variable=correct_var)
                correct_checkbox.pack(side="right", padx=5)

                self.options.append((var, correct_var))
        except IndexError:
            pass

    def generate_html(self):
        if not self.questions:
            messagebox.showerror("Errore", "Non ci sono domande salvate.")
            return

        title = self.title_entry.get().strip()
        footer = self.footer_entry.get().strip()
        if not title:
            messagebox.showerror("Errore", "Inserisci il titolo del questionario.")
            return

        html_content = f"""<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        h1, h3 {{
            text-align: center;
        }}
        .correct {{
            color: green;
            font-weight: bold;
        }}
        .incorrect {{
            color: red;
            font-weight: bold;
        }}
        footer {{
            font-size: 0.8em;
            text-align: center;
            margin-top: 20px;
            color: #555;
        }}
    </style>
    <script>
        function controllaRisposte() {{
            var risposteCorrette = [{",".join(
                [str(next(i for i, opt in enumerate(q["options"]) if opt["correct"])) for q in self.questions]
            )}];
            var tutteLeOpzioni = document.querySelectorAll('input[type="radio"]');
            var risposteDate = document.querySelectorAll('input[type="radio"]:checked');
            var punteggio = 0;

            tutteLeOpzioni.forEach(function(opzione) {{
                var label = opzione.parentNode;
                label.classList.remove('correct', 'incorrect');
            }});

            risposteDate.forEach(function(risposta) {{
                var indiceDomanda = parseInt(risposta.name.replace('domanda', '')) - 1;
                var indiceRisposta = parseInt(risposta.value);
                var label = risposta.parentNode;

                if (indiceRisposta === risposteCorrette[indiceDomanda]) {{
                    label.classList.add('correct');
                    punteggio++;
                }} else {{
                    label.classList.add('incorrect');
                }}
            }});

            tutteLeOpzioni.forEach(function(opzione) {{
                var indiceDomanda = parseInt(opzione.name.replace('domanda', '')) - 1;
                var indiceRisposta = parseInt(opzione.value);
                var label = opzione.parentNode;

                if (indiceRisposta === risposteCorrette[indiceDomanda]) {{
                    label.classList.add('correct');
                }}
            }});

            alert('Punteggio: ' + punteggio + '/' + risposteCorrette.length);
        }}
    </script>
</head>
<body>
    <h1>{title}</h1>
    <form>
"""

        for i, q in enumerate(self.questions, 1):
            html_content += f"<h3>{i}. {q['question']}</h3>\n"
            for j, option in enumerate(q["options"]):
                html_content += f'<label><input type="radio" name="domanda{i}" value="{j}"> {option["text"]}</label><br>\n'

        html_content += """<br>
        <input type="button" value="Controlla Risposte" onclick="controllaRisposte()">
    </form>"""

        if footer:
            html_content += f"<footer>{footer}</footer>"

        html_content += """</body>
</html>
"""

        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("File HTML", "*.html")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            messagebox.showinfo("Successo", f"File HTML salvato con successo in {file_path}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TestGeneratorApp(root)
    root.mainloop()
