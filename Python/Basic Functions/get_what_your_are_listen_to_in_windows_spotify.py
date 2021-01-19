import win32gui,win32con,win32process,win32api
import time
import sys
l_janelas = []
def enumerador_de_janelas(x,no_topo):
    l_janelas.append((x,win32gui.GetWindowText(x)))
l_janelas_final = []
def construir_l_final_de_janelas():
    global l_janelas_final
    global l_janelas
    l_janelas = []
    l_janelas_final = []
    win32gui.EnumWindows(enumerador_de_janelas,l_janelas)
    for j in l_janelas:
        if len(j[1]) > 0:l_janelas_final.append(j)
construir_l_final_de_janelas()
def retornar_musica():
    construir_l_final_de_janelas()
    for x in l_janelas_final:
        try:
            pid = win32process.GetWindowThreadProcessId(x[0])
            handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid[1])
            proc_name = win32process.GetModuleFileNameEx(handle, 0)
            if 'Spotify' in proc_name:
                if '-' in x[1]:
                    print(x[1])
                    return x[1]
        except:pass
t = 0
while True:
    retornar_musica()
    time.sleep(1)