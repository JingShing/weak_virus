import win32api, win32con

title = "病毒警告！"
nation = "口國"
a = f"嗨,我是個來自{nation}的病毒,但很不幸的,因為我的國家的科技實在太落後了,我沒辦法對您的電腦做出任何傷害。請您行行好, 幫我把您電腦上其中一個重要檔案刪掉,然後再把我傳給下一個使用者。 非常感謝您的配合!\n{nation}病毒 敬上"

win32api.MessageBox(0, a, title, win32con.MB_YESNOCANCEL)
