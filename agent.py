class ReflectionAgent:
    def __init__(self):
        self.valid_moods = ["happy", "sad", "confused", "stressed"]

    def normalize_input(self, mood):
        return mood.strip().lower()

    def validate_mood(self, mood):
        return mood in self.valid_moods

    def get_questions(self, mood):
        if mood == "happy":
            return [
                "What went well today?",
                "Why do you think it went well?"
            ]

        elif mood == "sad":
            return [
                "What caused this feeling?",
                "Is it temporary or something recurring?"
            ]

        elif mood == "confused":
            return [
                "What exactly is confusing you?",
                "What options are you considering?"
            ]

        elif mood == "stressed":
            return [
                "What is causing the stress?",
                "Can you break it into smaller parts?"
            ]

    def get_suggestion(self, mood):
        suggestions = {
            "happy": "Write 2-3 things you are grateful for.",
            "sad": "Consider talking to someone or journaling your thoughts.",
            "confused": "List pros and cons of each option before deciding.",
            "stressed": "Take a short break and focus on one small task at a time."
        }
        return suggestions.get(mood)

    def run(self):
        print("=== Daily Reflection ===")
        mood_input = input("How are you feeling today? ").strip()

        mood = self.normalize_input(mood_input)

        if not self.validate_mood(mood):
            print("\nInvalid input.")
            print("Please choose from:", ", ".join(self.valid_moods))
            return

        print("\nLet's reflect a bit:\n")

        questions = self.get_questions(mood)
        for q in questions:
            input(f"- {q} ")

        suggestion = self.get_suggestion(mood)

        print("\n--- Summary ---")
        print(f"Mood: {mood.capitalize()}")
        print(f"Suggestion: {suggestion}")
        print("----------------")


if __name__ == "__main__":
    agent = ReflectionAgent()
    agent.run()
