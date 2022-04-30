import json
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from state_class import *
from functions import *
import os
import copy


def del_lab():
    label.after(1000,label.destroy())





def makelist():
    scrollbar=Scrollbar(window)
    scrollbar.pack(side=RIGHT,fill=Y)
#Read File
    desired=begin.get()
    f=open(desired)
    sc=json.load(f)
    
    NAME= list()
    SEQ = list()
    PART = list()
    for i in sc['parts']:
        NAME.append(i["name"])
        SEQ.append(i["sequence"])
        PART.append(i["part"])
      
#Break Initial Window    
    begin.destroy()
    beginbtn.destroy()
    beginlbl.destroy()

#Make List
    entered=str("BurritoLy, Using Parts Library: "+ desired)
    window.title(entered)
    partlist=NAME
    seqlist=SEQ
    parts=tk.StringVar(value=partlist)
    saved_partlist = copy.deepcopy(partlist)
    parts_list=Listbox(window,listvariable=parts,height=6,selectmode='browse')
    sequence=list()
    amino=list()    
    #Removing the individual bad parts
    temp_amino = copy.deepcopy(amino)
    temp_sequence = copy.deepcopy(sequence)
    burritoly.on_event('search database') 
    print('i am here')
    print(parts_list)
    bad_stuff = []
    for i, part in enumerate(parts_list.get(0, END)):
        print('part is ' + part)
        path = 'queries/query_future.fsa'
        fid = open(path,'w')
        idx = NAME.index(part)
        print(SEQ[idx])
        p = ''.join(temp_amino) + SEQ[idx]
        temp_amino.append(SEQ[idx])
        temp_sequence.append(NAME[idx])
        fid.write(p)
        fid.close()
        Kyra.search_bad_db(query_in = 'query_future')
        Kyra.readBadOutput()
        if (Kyra.bad_found):
        #remove the last thing
            print ("future part found", temp_sequence)
            bad_part = temp_sequence[-1]
            temp_sequence.pop()
            temp_amino.pop()
            bad_stuff.append(bad_part)
    for bad in bad_stuff:
        idx = parts_list.get(0, tk.END).index(bad)
        partlist.pop(idx)
        parts=tk.StringVar(value=partlist)
        parts_list.config(listvariable= parts)

#Shift Parts
    def writeseq():
        amino.clear()
        for i in sequence:
            for j in range(len(partlist)):
                partiboi = partlist[j]
                if i == partiboi:
                    amino.append(seqlist[j])
                
    
    def change_seq():
        def changeseq(self):
            def movepart(self):
                pos=move_list.curselection()
                dest=int(pos[0])
                the_guy=click
                old_seq.pop((clicked[0]))
                old_seq.insert(dest,the_guy)
                sequence=old_seq
                writeseq()
                #print(sequence)
                loca.destroy()
            seqlength=len(old_seq)
            ran=list(range(seqlength))
            rang=tk.StringVar(value=ran)
            clicked=change_list.curselection()
            #print("clicked is", clicked)
            click=change_list.get(clicked)
            #print("click is", click)
            loca=Toplevel(window)
            loca.geometry("800x250+200+300")
            loca.title("Move Where?")
            move_list=Listbox(loca,listvariable=rang,height=6,selectmode='browse')
            move_list.bind('<<ListboxSelect>>',movepart)
            move_list.pack(fill=Y)
            top.destroy()
        old_seq=sequence
        #print(len(old_seq))
        top=Toplevel(window)
        top.geometry("800x250+200+300")
        top.title("Which part would you like to move?")
        seq_list=tk.StringVar(value=old_seq)
        change_list=Listbox(top,listvariable=seq_list,height=6,selectmode='browse')
        change_list.bind('<<ListboxSelect>>',changeseq)
        change_list.pack(fill=Y)
        # future_sight()


        
        
        
        
        
    #Remove Part
 

    def rmv_part():
        def poptart(self):
            finish_him=break_list.curselection()
            old_seq.pop(finish_him[0])
            sequence=old_seq
            writeseq()
            top.destroy()
        old_seq=sequence
        #print(len(old_seq))
        top=Toplevel(window)
        top.geometry("800x250+200+300")
        top.title("Which part would you like to move?")
        seq_list=tk.StringVar(value=old_seq)
        break_list=Listbox(top,listvariable=seq_list,height=6,selectmode='browse')
        break_list.bind('<<ListboxSelect>>',poptart)
        break_list.pack(fill=Y)

        # partlist = copy.deepcopy(saved_partlist)
        # parts=tk.StringVar(value=partlist)
        # parts_list.config(listvariable= parts)

    # def future_sight():
    #     temp_amino = copy.deepcopy(amino)
    #     temp_sequence = copy.deepcopy(sequence)
    #     burritoly.on_event('search database') 
    #     print('i am here')
    #     print(parts_list)
    #     bad_stuff = []
    #     for i, part in enumerate(parts_list.get(0, END)):
    #         print('part is ' + part)
    #         path = 'queries/query_future.fsa'
    #         fid = open(path,'w')
    #         idx = NAME.index(part)
    #         print(SEQ[idx])
    #         p = ''.join(temp_amino) + SEQ[idx]
    #         temp_amino.append(SEQ[idx])
    #         temp_sequence.append(NAME[idx])
    #         fid.write(p)
    #         fid.close()
    #         Kyra.search_bad_db(query_in = 'query_future')
    #         Kyra.readBadOutput()
    #         if (Kyra.bad_found):
    #         #remove the last thing
    #             print ("future part found", temp_sequence)
    #             bad_part = temp_sequence[-1]

    #             temp_sequence.pop()
    #             temp_amino.pop()
    #             bad_stuff.append(bad_part)
    #     for bad in bad_stuff:
    #         idx = parts_list.get(0, tk.END).index(bad)
    #         partlist.pop(idx)
    #         parts=tk.StringVar(value=partlist)
    #         parts_list.config(listvariable= parts)
            
    #Jon's Function. Can replace this and the name of it.
    def chk_part():
        #Replace this function
        path = 'queries/query_seq.fsa'
        fid = open(path,'w')
        fid.write(''.join(amino))
        fid.close()
        burritoly.on_event('search database')
        # Jon.search_good_db(query_in = 'query_seq')
        # Jon.readGoodOutput()
        Jon.search_bad_db(query_in = 'query_seq')
        Jon.readBadOutput()
        if (Jon.banned_status):
            top=Toplevel(window)
            top.geometry("800x250+200+300")
            top.title("YOU ARE BANNED. IGSC IS COMING FOR YOU.")

        if (Jon.bad_found ):
            #remove the last thing
            bad_part = sequence[-1]
            sequence.pop()
            amino.pop()
            idx = parts_list.get(0, tk.END).index(bad_part)
            partlist.pop(idx)
            parts=tk.StringVar(value=partlist)
            parts_list.config(listvariable= parts)
        
        Label(window,text="Running search...").pack(side=TOP)

        
    #Summon Command
    def onselect(event):
        select=parts_list.curselection()
        selected=",".join([parts_list.get(i) for i in select])
        sequence.append(selected)
        for item in sequence:
            if item==(""):
                sequence.remove("")
        writeseq()
        show_seq()
        # future_sight()
        
        
        #print(sequence)

    def show_seq():
        sequen=Toplevel(window)
        sequen.geometry("450x100+200+300")
        sequen.title("Current Sequence")
        part=Label(sequen, text=sequence)
        part.pack(side=LEFT)
        print(sequence)
        print(''.join(amino))
#Back to Function Window
    parts_list.bind('<<ListboxSelect>>', onselect)
    parts_list.pack(side=RIGHT,fill=Y, anchor=W)
    parts_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=parts_list.yview)
    Change=Button(window,text="Move Part",command=change_seq)
    remove=Button(window,text="Remove Part", command=rmv_part)
    check=Button(window,text="Check Viability", command=chk_part)
    show=Button(window, text="Show Sequence", command=show_seq)
    Change.pack(side=TOP)
    remove.pack(side=TOP)
    check.pack(side=TOP)
    show.pack(side=BOTTOM)
    

#Initial Window
window=Tk()
window.title('BurritoLy')
window.geometry('1200x1000')
burritoly = toolDeviceThing()
Jon = userPerson(user_id = '191')
Kyra = userPerson(user_id = '111')
begin=Entry(window,width=100,textvariable= input)
beginbtn=Button(window,text= 'Submit', command=makelist)
beginlbl=Label(window,text='Enter File Name')
beginlbl.place(relx=0.065,rely=0.5, anchor=CENTER)
begin.place(relx=0.5, rely=0.5,anchor=CENTER)
beginbtn.place(relx=0.5, rely=0.55,anchor=CENTER)
window.mainloop()



