# Setup ESP2866(NodeMcu)

Board info : NodemMcu V3

## Steps

1. Clone this repo
1. Create venv + install requirements
1. Find out the connected board name in /dev/tty.
1. Erase flash

    ```
    esptool.py --port /dev/tty.usbserial-14240 erase_flash
    ```
1. Flash new firmware
    ```
    esptool.py --port /dev/tty.usbserial-14240 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20190125-v1.10.bin
    ```

1. Plug/unplug device
1. Test connection
    ``` 
    picocom /dev/tty.usbserial-14240 -b115200
    
    or
    
    screen /dev/tty.usbserial-14240 -b115200 
    ``` 

- Connect with rshell

``` 
rshell -p /dev/tty.usbserial-14240 
```

- Run example(from rshell)

```
cp /examples/blink /pyboard
repl
import blink
```


