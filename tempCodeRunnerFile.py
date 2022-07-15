btn_trans = Button(window, text="Translate", width=15, height=2, command=trans)
btn_trans.place(x=300, y=150)

btn_clear = Button(window, text="Clear Text",
                   width=17, height=2, command=clear)
btn_clear.place(x=430, y=150)

btn_copy = Button(window, text="Copy to clipboard",
                  width=15, height=2, command=hadleCopy)
btn_copy.place(x=300, y=200)

btn_pasteToClipboard = Button(window, text="Paste from clipboard",
                              width=17, height=2, command=hadlePaste)
btn_pasteToClipboard.place(x=430, y=200)