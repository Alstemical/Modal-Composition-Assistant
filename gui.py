import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
from scales import NOTES, MODES, IONIAN_INTERVALS, get_scale_notes, get_wh_pattern, get_ionian_relation
from chords import get_diatonic_chords
from progressions import suggest_progressions, EMOTIONS
from mode_context import MODE_CHARACTER

def generate_results():
    key=key_var.get()
    mode=mode_var.get()
    emotion=emotion_var.get()
    if emotion=="None":
        emotion=""
    result_text.delete(1.0,tk.END)
    notes,error=get_scale_notes(key,mode)
    if error:
        messagebox.showerror("Error",error)
        return
    mode_lower=mode.lower()
    start_pos=MODES[mode_lower]
    intervals=IONIAN_INTERVALS[start_pos:]+IONIAN_INTERVALS[:start_pos]
    wh_pattern=get_wh_pattern(intervals)
    ionian_relation=get_ionian_relation(key,mode)
    mode_context=MODE_CHARACTER.get(mode_lower,"No context available.")
    diatonic_chords=get_diatonic_chords(notes,mode)
    progressions=suggest_progressions(mode,diatonic_chords,emotion)
    result_text.insert(tk.END,f"Notes in {key} {mode}:\n")
    result_text.insert(tk.END,' -> '.join(notes)+"\n\n")
    result_text.insert(tk.END,f"Interval Pattern (W=whole step, H=half step): {wh_pattern}\n\n")
    result_text.insert(tk.END,"Relation to Ionian Scale:\n")
    result_text.insert(tk.END,ionian_relation+"\n\n")
    result_text.insert(tk.END,"Context and Usage:\n")
    result_text.insert(tk.END,mode_context+"\n\n")
    result_text.insert(tk.END,"Diatonic Chords:\n")
    result_text.insert(tk.END,'\n'.join(diatonic_chords)+"\n\n")
    result_text.insert(tk.END,"Suggested Progressions:\n")
    result_text.insert(tk.END,'\n'.join(progressions)+"\n")

# Create Tkinter window
root=tk.Tk()
root.title("Music Theory Generator")
root.geometry("600x500")
root.configure(bg="#FF9999")  # Salmon pink background

# Style for ttk widgets
style=ttk.Style()
style.theme_use('default')
style.configure("Custom.TMenubutton",background="#ADD8E6",foreground="#000000")
style.map("Custom.TMenubutton",background=[("active","#87CEEB")])
style.configure("Custom.TOptionMenu",background="#ADD8E6",foreground="#000000")
style.configure("Custom.TButton",background="#ADD8E6",foreground="#000000")
style.map("Custom.TButton",background=[("active","#87CEEB")])

# Key selection
tk.Label(root,text="Select Key:",bg="#FF9999",fg="#000000").pack(pady=2)
key_var=tk.StringVar(root,NOTES[0])
key_menu=ttk.OptionMenu(root,key_var,"",*NOTES,style="Custom.TMenubutton")
key_menu.pack(pady=2)
key_menu['menu'].configure(background="#ADD8E6",foreground="#000000")

# Mode selection
tk.Label(root,text="Select Mode:",bg="#FF9999",fg="#000000").pack(pady=2)
mode_var=tk.StringVar(root,"Ionian")
mode_menu=ttk.OptionMenu(root,mode_var,"",*[m.capitalize() for m in MODES.keys()],style="Custom.TMenubutton")
mode_menu.pack(pady=2)
mode_menu['menu'].configure(background="#ADD8E6",foreground="#000000")

# Emotion selection
tk.Label(root,text="Select Emotion (optional):",bg="#FF9999",fg="#000000").pack(pady=2)
emotions=["None"]+[e.capitalize() for e in EMOTIONS.keys()]
emotion_var=tk.StringVar(root,"None")
emotion_menu=ttk.OptionMenu(root,emotion_var,"",*emotions,style="Custom.TMenubutton")
emotion_menu.pack(pady=2)
emotion_menu['menu'].configure(background="#ADD8E6",foreground="#000000")

# Generate button
button_frame=tk.Frame(root,bg="#FF9999")
button_frame.pack(pady=2)
ttk.Button(button_frame,text="Generate",style="Custom.TButton",command=generate_results).pack()

# Results display
result_text=scrolledtext.ScrolledText(root,wrap=tk.WORD,height=20,width=70,bg="#ADD8E6",fg="#000000")
result_text.pack(pady=2)

root.mainloop()