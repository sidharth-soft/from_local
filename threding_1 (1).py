import threading
import time

def first_thread():
    print('first_thread started')
    print('first_thread name is :::::', threading.currentThread().getName())
    time.sleep(5)
    print(' first_thread is exit')

def second_thread(a,b):
    print('second_thread started', a , b)
    print('second_thread name is :::::', threading.currentThread().getName())
    print('count is :', threading.active_count())
    print('second_thread is exit')




ft = threading.Thread(name='uday', target=first_thread)
st = threading.Thread(name='jayakrishna', target=second_thread, args=('jaya','krishna'))


ft.start()
# ft.join()
st.start()





#modules
# PDB