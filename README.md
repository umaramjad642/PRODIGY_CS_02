Image Encryption ToolProdigy InfoTech 

Cyber Security Internship | Task 02

A Python tool that uses pixel manipulation for image encryption and decryption. This demonstrates how to secure visual data by modifying its underlying RGB values.

🚀 Key Features

* RGB Modification: Uses a numeric key to mathematically shift pixel values.
* Lossless Output: Saves files in .png format to ensure perfect decryption.
* Validation: includes error handling for file paths and input keys.
* Continuous Flow: Interface allows for repeated tasks without restarting.

🛠️ How It Works

* Each pixel's Red, Green, and Blue values are altered using the formula:
* Encryption: $(Value + Key) \mod 256$
* Decryption: $(Value - Key) \mod 256$
  
📋 Quick Start

* Install Library: pip install Pillow
* Run Script: python image_tool.py
* Follow Prompts: Choose mode (E/D), enter the image path, and provide your secret key.
