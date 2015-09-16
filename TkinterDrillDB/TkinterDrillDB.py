#!/usr/bin/python3
# this is python drill 11 - using python 3.4, tkinter, sqlite
#   add functionality to python drill 10 - create a gui using tkinter and visual studio
#       - add database to store the user text 
#       - asdd controls to display the stored text  
#
# gail hedberg - August 4th, 2015


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from write_html_file import *
import abc_db_utility


class CreateHTML:

    def __init__(self, root):

        #create the top frame and labels
        root.title('ABC Company')

        self.frame_top = ttk.Frame(root, padding = "3 3 12 12")
        self.frame_top.grid(column = 0, row = 0, sticky = (N, E, S, W))
        self.frame_top.columnconfigure(0, weight = 1)
        self.frame_top.rowconfigure(0, weight = 1)

        ttk.Label(self.frame_top, text = 'Create a Web Page', 
                  foreground = 'blue').grid(row = 0, column = 0, padx = 5, pady = 5)
        
        ttk.Label(self.frame_top, 
                  text = 'Select (or Add new) text for your web page').grid(row = 1, column = 0, padx = 5, pady = 5)
        
        # create the combobox
        self.cb_text = ttk.Combobox(self.frame_top, width = 30)
        self.cb_text.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.cb_text.bind('<<ComboboxSelected>>', self.item_selected)

        # load the combobox from the database
        #self.db_list = ['line 1', 'line 2', 'line 3', 'line 4', 'line 5', 'line 6', 'line 7']
        self.db_list = []
        self.db_list = abc_db_utility.get_web_text()
        self.db_list.sort()
        self.cb_text.config(values = self.db_list)

        #create the buttons and place them in their own frame
        self.frame_btns = ttk.Frame(root, padding = "3 3 12 12")
        self.frame_btns.grid(row = 2, column = 0)

        btn_submit = ttk.Button(self.frame_btns, text = 'Submit', command = self.submit)
        btn_clear = ttk.Button(self.frame_btns, text = 'Clear', command = self.clear)
        btn_exit = ttk.Button(self.frame_btns, text = 'Exit', command = self.exit)

        btn_submit.grid(row = 0, column = 0, padx = 5, sticky = 'e')
        btn_clear.grid(row = 0, column = 1, padx = 5, sticky = 'e')
        btn_exit.grid(row = 0, column = 2, padx = 5, sticky = 'e')
   
    # define some class methods
    def write_the_file(self):
        #print('write the file')
        write_it = WriteHtmlFile()
        write_it.set_html_text('{}'.format(self.cb_text.get()))
        write_it.format_html()
        write_it.write_the_file()

    def update_list(self):
        self.db_list.append(self.cb_text.get())
        self.cb_text.config(values = self.db_list)

    def show_new_item(self):
        new_index = len(self.db_list) - 1
        self.cb_text.current(new_index)

    def update_db(self):
        #print('in update_db with {}'.format(self.cb_text.get()))
        abc_db_utility.update_web_text(self.cb_text.get())

    #define event handlers
    def item_selected(self, event):
        pass
        #print('current selected {} text is {}'.format(self.cb_text.current(), self.cb_text.get()))
         
    def submit(self):
        #print('current selected {}'.format(self.cb_text.current()))
        #print ('self.cb_text.get() = {}'. format(self.cb_text.get()))
        #print('current() is {}'.format(self.cb_text.current()))

                 
        if len(self.cb_text.get()) == 0:
            messagebox.showwarning(title = 'Error', message = 'Please select an item or \nenter new text')
        else:
            # add new text item to the list, reset the cb, update the database and write the file
            if self.cb_text.current() == -1:
                self.update_list()
                self.show_new_item()
                self.update_db()

            self.write_the_file()
            messagebox.showinfo(title = 'Success!', message = 'Your web page abcsale.html is\nready for use!')



    def clear(self):
       #print('about to clear {} '.format(self.cb_text.get()))
       #print ('about to clear entry # {}'.format(self.cb_text.current()))
       self.cb_text.set('')
  
    def exit(self):
       sys.exit()
 
    def OnCloseWindow(self, event):
        self.Destroy()
     
def main():
    root = Tk()
    createhtml = CreateHTML(root)
    root.mainloop()
    
if __name__ == "__main__": main()