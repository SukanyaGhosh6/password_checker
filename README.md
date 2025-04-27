# Password Strength Checker in Python

## What's This All About?

So, I’ve built this super simple Python script to help you check the strength of your passwords. It’s a basic tool, but it’s got some cool functionality. It checks things like:
- How long your password is.
- Whether it has uppercase, lowercase, numbers, and special characters.
- Whether you’re using any of those terrible common passwords like `123456` (because, trust me, that's the first thing hackers try).

It's a fun project to get your feet wet in the world of cybersecurity. Plus, it’s a good way to learn a few basic concepts like **password policies**, **hashing**, and **salting** (if you want to take it up a notch).

## How Does It Work?

This script looks at a few key things when checking a password:

1. **Length**: Your password has to be at least 8 characters long to be considered "strong."
2. **Character Diversity**: It needs a mix of:
   - Uppercase letters (`A-Z`)
   - Lowercase letters (`a-z`)
   - Numbers (`0-9`)
   - Special characters (e.g., `!@#$%^&*`)
3. **Common Password Check**: It checks if your password is one of the most used, like `password123` or `qwerty`, and lets you know if it's too easy to guess.

Also, if you're feeling adventurous, there are extra features like **password hashing** and **salting** (for those who want to get more technical about securing passwords).

## Features

- **Password Strength Check**: It gives you feedback on whether your password is strong or weak.
- **Common Password Detection**: It warns you if your password is too easy to guess.
- **Hashing** (Optional): You can hash your password (SHA-256) to see how passwords are stored securely.
- **Salting** (Optional): You can add a random salt to your password before hashing, making it harder for hackers to crack.

## Getting Started

### What Do You Need?

You’ll need:
- Python (3.x version). You can get it from [here](https://www.python.org/downloads/).
- A code editor. I recommend using **VS Code**, but anything works.

### How to Run It

1. **Clone or download the repo**:
   ```bash
   git clone https://github.com/SukanyaGhosh6/password_checker.git
   ```
   
2. **Navigate to the project folder**:
   ```bash
   cd password-strength-checker
   ```

3. **Run the script**:
   - Open the terminal in VS Code (or use your system terminal).
   - Run the script by typing:
     ```bash
     python password_checker.py
     ```

4. **Test it out**: Enter a password when prompted, and the script will analyze how strong (or weak) it is.

### Sample Output

```bash
Enter a password to check its strength: password123
Password is weak due to the following reasons:
Password should contain at least one uppercase letter.
Password should contain at least one special character.
Password is too common and easy to guess.
```

## Extra Stuff You Can Try

- **Hashing**: Want to see how passwords are actually stored securely? The script lets you hash the password using SHA-256.
  
- **Salting**: You can also add a random "salt" (a random string) to your password before hashing. It’s a neat trick to make your password harder to crack.

## Some Cool Things to Research

While you’re messing around with this project, here are some things to research that will help you understand why this stuff matters:

1. **Password Complexity**:
   - Strong passwords need a mix of characters. This makes it harder for someone to guess it using brute force.
   - Avoid passwords that are easy to guess or based on dictionary words. The script checks for that and gives you a heads-up if your password is too common.

2. **Password Hashing**:
   - When you create an account on a website, your password isn’t stored directly. Instead, it’s usually **hashed** using algorithms like SHA-256, which makes it unreadable (even if someone hacks the database).
   - You can try out **salting** — this is where a random string (the "salt") is added to your password before hashing. It makes it way harder for hackers to use precomputed hash-cracking methods (like rainbow tables).

3. **Why Common Passwords Are a Bad Idea**:
   - Common passwords (like `password123` or `qwerty`) are super easy to guess. Hackers will always try those first. That’s why this script checks for them and warns you if you’re using one.

## Final Thoughts

This project is a simple intro to the world of **password security**. It covers the basics, but there’s plenty of room to dive deeper into more advanced stuff like **password hashing**, **salting**, and **encryption**. 

So go ahead, play around with the script, try modifying it, and maybe even add some features of your own. At the end of the day, the goal is to get you thinking about how we can protect our data and why strong passwords matter.

## License

Feel free to use, tweak, and share this project under the MIT License. Fork it, make it better, and maybe share what you come up with!
