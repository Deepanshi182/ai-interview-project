import os
import json
from typing import Dict, Any

from groq import Groq

from dotenv import load_dotenv
load_dotenv()

class LLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not set in environment")

        self.client = Groq(api_key=api_key)

        # 🔥 Best model (fast + free)
        self.model="llama-3.1-8b-instant"

    def _build_prompt(self, context: str) -> str:
        return f"""
You are a senior Amazon interviewer.
IMPORTANT RULE:
- Generate questions ONLY from the resume content
- DO NOT add external or generic DSA questions
- If a concept is not mentioned, DO NOT ask about it
Generate:
- 5 technical questions
- 3 HR questions
- 2 project questions

Each question MUST include:
- question
- difficulty (Easy/Medium/Hard)
- topic

Resume:
{context}

Return ONLY JSON:
{{
  "technical": [
    {{
      "question": "",
      "difficulty": "",
      "topic": ""
    }}
  ],
  "hr": [],
  "project": []
}}
"""

    def generate_questions(self, context: str) -> Dict[str, Any]:
        prompt = self._build_prompt(context)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            raw_text = response.choices[0].message.content.strip()

            # 🔥 Clean JSON (important)
            cleaned = raw_text.replace("```json", "").replace("```", "").strip()

            try:
                return json.loads(cleaned)
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON from LLM",
                    "raw_response": raw_text
                }

        except Exception as e:
            return {
                "error": "LLM generation failed",
                "details": str(e)
            }


# Singleton instance
llm_service = LLMService()