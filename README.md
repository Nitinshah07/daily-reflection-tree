# daily-reflection-tree
A lightweight reflection tool that converts thoughts into structured insights using a deterministic decision tree approach.
# Daily Reflection Tree

This project is a simple yet structured system designed to help users reflect on their daily experiences.

It uses a deterministic decision tree to guide users based on their mood and provide meaningful suggestions.

---

## 💡 Idea

The goal is to convert unstructured thoughts into clear and actionable reflections.

Instead of giving random advice, the system follows predefined paths to ensure consistency.

---

## ⚙️ How It Works

1. User inputs their mood  
2. The system identifies the emotional state  
3. A fixed decision path is followed  
4. A reflection and suggestion is generated  

---

## 🌿 Example

Input:
> stressed

Output:
> Break your tasks into smaller steps and take a short break.

---

## 🚧 Guardrails

- Only predefined moods are accepted  
- No random or unpredictable responses  
- Input validation included  
- Fully deterministic logic  

---

## 📂 Project Structure

- decision-tree.md → core logic  
- agent.py → simple implementation  

---

## 🛠 Tech Used

- Python  
- Markdown  
## Example Run

Input:
stressed

Output:
Take a short break and focus on one small task at a time.
---

## ▶️ How to Run

1. Clone the repository  
2. Open terminal in project folder  
3. Run:

```bash
python agent.py


---



```md
## 💬 Example Interaction

Input:
How are you feeling today? stressed

Output:
Let's reflect a bit:

- What is causing the stress?
- Can you break it into smaller parts?

Suggestion:
Take a short break and focus on one small task at a time.


Happy → Reflection → Gratitude  
Sad → Support → Journaling  
Confused → Clarity → Decision making  
Stressed → Action → Task breakdown
## 👤 Author

Nitin Shah
This project was built as part of the DeepThought CultureTech role simulation assignment.
