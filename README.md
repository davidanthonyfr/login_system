# User Login Systen
I built a simple login system that allows a maximum of 3 attempts. Each failed attempt decreases a counter, and if it reaches zero, the system locks the account. This demonstrates brute-force protection, which is a core security concept to prevent attackers from endlessly guessing passwords.


- User tries to log in → entered username David and password password.
- The program compared it to the correct credentials (probably admin + 1234 from our example).
- Since they didn’t match → it printed ❌ Wrong credentials.
- Each failed attempt reduced the counter (Attempts left: 2, then 1, then 0).
- After 3 failed attempts → the program locked the account and showed ⛔ “Account locked.”
<img width="782" height="160" alt="image" src="https://github.com/user-attachments/assets/461bb4d2-615c-49c5-8dd0-b170a1dd0f5d" />
