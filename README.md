# WhatsApp Student Q/A Chatbot

A real-time **WhatsApp-based Question & Answer chatbot** for students, powered by **Flask**, **Twilio WhatsApp API**, and **OpenAI GPT models**. The bot receives any student doubt or academic question on WhatsApp and replies instantly with accurate, clear explanations.

---

## 🚀 Features

* 📱 **WhatsApp Integration** using Twilio Sandbox
* 🤖 **AI-powered answers** using OpenAI GPT (gpt-4o-mini)
* ⚡ Responds to *any* academic question: programming, maths, physics, engineering, aptitude, etc.
* 🔐 Secure setup using `.env` (API keys never exposed)
* 🧩 Lightweight Flask backend
* 🌐 Can be deployed or run via ngrok

---

## 📂 Project Structure

```
whatsapp_chatbot/
│── app.py
│── .env                 # (ignored in Git)
│── .gitignore
│── intents.json         # optional (if using NLP version)
│── utils/
│    └── (support scripts)
│── model/
│    └── (trained ML models, optional)
│── .venv/              # (ignored)
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/Whatsapp_chatbot.git
cd Whatsapp_chatbot
```

### 2. Create Virtual Environment

```
python -m venv .venv
```

Activate it:

* **Windows:**

  ```
  .venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a file named `.env`:

```
OPENAI_API_KEY=sk-xxxx-your-key
```

> ⚠️ **Never commit your `.env` file!** (Already protected by `.gitignore`)

---

## 🔧 Configure Twilio WhatsApp Sandbox

1. Go to **Twilio Console → Messaging → Try it Out → WhatsApp Sandbox**
2. Join the sandbox by sending your "join keyword" from WhatsApp
3. Run ngrok:

   ```
   ngrok http 5000
   ```
4. Take your ngrok HTTPS URL and set it as your webhook:

   ```
   https://your-ngrok-url.ngrok-free.dev/whatsapp
   ```
5. Set method to **POST**
6. Save

---

## ▶️ Running the App

Start Flask:

```
python app.py
```

Keep ngrok running in another terminal.

Send a question on WhatsApp:

```
Explain polymorphism
```

The bot will reply instantly.

---

## 🧠 How It Works

1. User sends any question → WhatsApp
2. Twilio forwards the message → Flask `/whatsapp` endpoint
3. Flask sends message → OpenAI GPT
4. GPT returns answer
5. Flask sends reply → Twilio → WhatsApp

---

## 📦 Deployment Options

* Render (free)
* Railway
* AWS EC2 / Lightsail
* PythonAnywhere

---

## 🙌 Contributions

Feel free to open issues or submit PRs.

---

## 📜 License

See the `LICENSE` file.

---

## ⭐ Acknowledgments

Built with ❤️ using:

* Flask
* Twilio API
* OpenAI GPT Models
* ngrok

---

Happy building! 🚀
