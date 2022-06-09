import uart

def receive_uart():
    uart.init()
    while True:
        uart.send(uart.receive())