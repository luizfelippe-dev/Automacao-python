from typing import Tuple
import customtkinter as ctk 
from tkinter import filedialog,DoubleVar,Variable
from tkinter import ttk
from execute import VerifyFile
from time import sleep

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('dark')

class AppMain(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.count_bar =0

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Configurando a geometria da janela
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.title('Automação de exclusão de Backup de arquivos')

        self.tab_main = ctk.CTkTabview(self)
        self.tab_main.pack(expand=True, fill='both', anchor = 'center')

        self.tab_main.add("Execusão")
        self.tab_main.add("Tabela ativos")
        self.tab_main.add("Tabela Excluidos")

        #self.frame_top = ctk.CTkFrame(self.tab_main.tab("Execusão"),height=(window_height/2))
        #self.frame_top.pack( fill='x',side='top', anchor='ne' )

        self.frame_client = ctk.CTkFrame(self.tab_main.tab("Execusão"))
        self.frame_client.pack(expand=True,fill='both')

        self.text_exec = ctk.CTkTextbox(self.frame_client,text_color="Orange",state='disable')
        self.text_exec.pack(expand=True,fill='both')
        
        self.var_barra = DoubleVar()
        self.var_barra.set(0)

        self.progressbar = ctk.CTkProgressBar(self.frame_client,variable=self.var_barra,orientation="horizontal")
        self.progressbar.pack(expand=True,fill='x',ipady=0)

        self.label_progressbar = ctk.CTkLabel(self.frame_client,text="0", font=('Arial',15),text_color='orange')
        self.label_progressbar.pack(anchor='center',after=self.progressbar)

        self.button_start = ctk.CTkButton(self.frame_client,text='Start Process', command=self._start_process)
        self.button_start.pack()

    def _start_process(self):
        self.progressbar.start()
        self.var_barra.set(0)
        self.update()
        opendire = filedialog.askdirectory()
        very = VerifyFile(opendire)._start_process()
        self.button_start.configure(state='disabled')
        
        for i in very:
            self._insert_text(i)
            
        self.button_start.configure(state='normal')
        self.progressbar.stop()            
            
            


  
    def _insert_text(self, text:str = ''):
        
        self.var_barra.set(self.count_bar+1)
        self.label_progressbar.configure(text=self.count_bar+1)
        self.count_bar+=1
        
        if text != '':
            try:
                texto = f"Nome:{text['nome_arquivo']},caminhho:{text['caminho_completo']},Data no Arquivo: {text['data_arquivo']} {text['hora_arquivo']}"
                self.text_exec.configure(state='normal')
                self.text_exec.insert('end',text=f"{texto}\n")
                self.text_exec.configure(state='disable')
            except:
                pass    

        self.update()
        pass             

        
        

        

if __name__=='__main__':
    app =AppMain()
    app.mainloop()