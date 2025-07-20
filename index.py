from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import os

# --- Paths ---
BRAVE_PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# This folder will be created automatically to store a fresh profile
NEW_PROFILE_DIR = r"C:\Users\Manuj\BraveSeleniumNewProfile"

# Ensure the folder exists
os.makedirs(NEW_PROFILE_DIR, exist_ok=True)

options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH
options.add_argument(f"--user-data-dir={NEW_PROFILE_DIR}")
options.add_argument("--profile-directory=Default")

# --- Launch Brave with the new profile ---
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

# --- First‑time setup: scan QR here ---
input("📲 Please scan the QR code in this Brave window, then press Enter here…")

# --- Your automation settings ---
contact_name = "akshay ji"  # EXACT chat name
message_count = 50  # Total messages to send

# --- Your message bank (67 emotional lines) ---
messages = [
    "hello baby",
    "sorry na baby",
    "I am so sorry baby please lets talk na",
    "i am sorry bachha",
    "I love you baby 😘",
    "Aik na darling please talk na",
    "i didnt do it intentionally na baby aika na",
    "please talk baby",
    "mujhe aapki yaad aarhi hai yaar please talk na",
    "baby bola na please",
    "hello baby please talk na",
    "hello baby",
    "hello darling",
    "kay kartay",
    "hellooooooo",
    "please talk na darling aika na",
    "baby please listen to me na",
    "I miss you so much",
    "My heart aches without you",
    "Can't stop thinking about you",
    "Please forgive me",
    "I need you here",
    "I feel lost without you",
    "You mean everything to me",
    "Come back to me",
    "I'm nothing without you",
    "My world is dark without you",
    "Please don’t go",
    "I’m hurting inside",
    "My heart belongs to you",
    "I’m begging you",
    "You’re my everything",
    "Please stay with me",
    "I can’t live like this",
    "I regret my mistake",
    "I want to make things right",
    "I’m sorry from the bottom of my heart",
    "I feel empty without you",
    "I’m drowning in guilt",
    "You’re all I think about",
    "I miss your smile",
    "I wish I could turn back time",
    "My love for you is endless",
    "Please give me another chance",
    "I’m craving your touch",
    "I promise I’ll change",
    "I can’t breathe without you",
    "I’m sorry for the pain I caused",
    "My heart screams your name",
    "Please let me fix this",
    "You’re the reason I smile",
    "I’m lost in memories of us",
    "I ache for your voice",
    "I’m sorry I hurt you",
    "I’m desperate for your love",
    "You’re my one and only",
    "I’m incomplete without you",
    "I need your forgiveness",
    "I’m sorry for everything",
    "My soul longs for you",
    "I miss our talks",
    "I can’t imagine life without you",
    "I’m sorry for the silence",
    "You’re the beat in my heart",
    "I’m longing for you",
    "Please come back",
    "I love you more every day",
]

# --- Open the chat ---
search_box = driver.find_element(
    By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"
)
search_box.click()
time.sleep(1)
search_box.send_keys(contact_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# --- Send messages with random delays ---
message_box = driver.find_element(
    By.XPATH, "//div[@contenteditable='true'][@data-tab='10']"
)
for i in range(message_count):
    msg = random.choice(messages)
    message_box.send_keys(msg)
    message_box.send_keys(Keys.ENTER)
    print(f"[{i+1}/{message_count}] Sent: {msg}")

    delay = random.uniform(2, 40)
    print(f"   → Waiting {delay:.1f}s")
    time.sleep(delay)

print("✅ All done!")
driver.quit()
