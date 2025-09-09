# Email Reconnaissance Simulation: Tracking User Interaction with Remote Images  

## 📌 Overview
This project demonstrates how phishing can be used as a **reconnaissance tool**.  
A harmless-looking email with an embedded tracking pixel is crafted and sent to a target.  
Simply opening the email can leak information to the attacker.  

## 🛠 How It Works
1. A simple email is sent containing a **remote image link** (tracking pixel).  
2. When the recipient opens the email, their client requests the image from the attacker’s server.  
3. The server logs valuable reconnaissance data such as:  
   - IP / network (where you are)  
   - User-Agent string (OS, email client, version)  
   - Timestamp (when you’re active)  

### Example log
```
127.0.0.1 - [08/Sep/2025 23:44:06] "GET /tracking_pixel.jpeg HTTP/1.1" 200 - 
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:140.0) Gecko/20100101 Thunderbird/140.2.0
```

## 📊 Real-World Context
Researchers at **Barracuda** confirmed that attackers send non-malicious “bait” emails as precursors to targeted phishing attacks.  

- Example: A Barracuda employee replied to a blank “Hi” email on **Aug 15, 2021**.  
- Within 48 hours, they received a targeted phishing attempt.  

These emails help attackers verify:  
- If the mailbox is active  
- If the recipient responds to messages  

## 🛡 Blue Team Defense
- Block or disable **automatic loading of remote content** in email clients.  
- Deploy **Secure Email Gateways** to filter suspicious messages.  
- Conduct **security awareness training** to reduce curiosity-driven clicks.  

## ⚠️ Disclaimer
This project is for **educational and defensive research purposes only**.  
Do not use these techniques in real-world attacks.  
